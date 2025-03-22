"""
ASGI to WSGI conversion utility.

This file provides a utility function to convert an ASGI application (like FastAPI)
to a WSGI application. This allows greater compatibility with some deployment
platforms that may not fully support ASGI yet.

Common use cases:
- Legacy WSGI server compatibility
- Integration with WSGI middleware
- Deployment on platforms requiring WSGI
- Custom deployment scenarios where ASGI isn't supported

Note: This utility is provided for compatibility but Mangum is the preferred
method for AWS Lambda deployment of FastAPI applications.
"""

from typing import Callable, Dict, List, Tuple, Union
import asyncio


def asgi_to_wsgi(asgi_app):
    """Convert an ASGI application to a WSGI application"""

    def wsgi_app(environ, start_response):
        """WSGI application"""
        # Convert environ to scope
        scope = {
            "type": "http",
            "asgi": {
                "version": "3.0",
                "spec_version": "2.1",
            },
            "http_version": environ["SERVER_PROTOCOL"].split("/")[1],
            "method": environ["REQUEST_METHOD"],
            "scheme": environ["wsgi.url_scheme"],
            "path": environ["PATH_INFO"],
            "raw_path": environ["PATH_INFO"].encode("utf8"),
            "query_string": environ["QUERY_STRING"].encode("utf8"),
            "root_path": environ.get("SCRIPT_NAME", ""),
            "headers": [
                (key.decode("latin1").lower().encode("latin1"), value.encode("latin1"))
                for key, value in (
                    (k[5:], v) for k, v in environ.items() if k.startswith("HTTP_")
                )
            ],
            "server": (environ["SERVER_NAME"], int(environ["SERVER_PORT"])),
            "client": (
                environ["REMOTE_ADDR"],
                int(environ["REMOTE_PORT"]) if "REMOTE_PORT" in environ else 0,
            ),
        }

        # Add special case headers
        if "CONTENT_TYPE" in environ:
            scope["headers"].append(
                (b"content-type", environ["CONTENT_TYPE"].encode("latin1"))
            )
        if "CONTENT_LENGTH" in environ:
            scope["headers"].append(
                (b"content-length", environ["CONTENT_LENGTH"].encode("latin1"))
            )

        # Create response variables
        status = None
        headers = None
        exc_info = None
        body = []

        async def receive():
            """ASGI receive function"""
            nonlocal body
            if body is not None:
                chunk = environ["wsgi.input"].read(
                    int(environ.get("CONTENT_LENGTH", 0))
                )
                body = None
                return {"type": "http.request", "body": chunk, "more_body": False}
            return {"type": "http.disconnect"}

        async def send(message):
            """ASGI send function"""
            nonlocal status, headers
            if message["type"] == "http.response.start":
                status = message["status"]
                headers = [
                    (name.decode("latin1"), value.decode("latin1"))
                    for name, value in message["headers"]
                ]
            elif message["type"] == "http.response.body":
                body = message.get("body", b"")
                more_body = message.get("more_body", False)
                if not more_body:
                    start_response(
                        f"{status} ",
                        headers,
                        exc_info,
                    )
                    return [body]

        # Call the ASGI app
        asgi_coroutine = asgi_app(scope, receive, send)
        asgi_task = asyncio.ensure_future(asgi_coroutine)
        asyncio.get_event_loop().run_until_complete(asgi_task)

        # Return the response body
        return [b""]

    return wsgi_app
