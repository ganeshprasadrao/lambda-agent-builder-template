# Lambda Agent Builder Template

A powerful template for building AI agents using Python, AWS Lambda, FastAPI, and LangChain/LangGraph. This template provides a production-ready foundation for deploying AI agents as serverless functions.

## Features

- 🚀 FastAPI for high-performance API endpoints
- ☁️ AWS Lambda deployment using Zappa
- 🤖 LangChain/LangGraph for building sophisticated AI agents
- 🔒 Environment management and security best practices
- 📝 Comprehensive logging and monitoring setup
- ⚡ Serverless architecture for scalability
- 💻 Local development environment

## Requirements

- Python 3.12+
- AWS Account and configured credentials
- OpenAI API key (or other LLM provider)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd lambda-agent-builder-template
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -e .
```

4. Set up your environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration
```

## Project Structure

```
lambda-agent-builder-template/
├── core/                    # Core agent logic and components
│   ├── agent.py            # Agent implementation
│   ├── chains/             # LangChain chains
│   ├── tools/              # Custom tools
│   └── utils/              # Utility functions
├── main.py                 # FastAPI application
├── lambda_handler.py       # AWS Lambda handler
├── zappa_settings.json     # Zappa deployment configuration
├── pyproject.toml         # Project dependencies
└── tests/                 # Test suite
```

## Local Development

1. Start the local development server:

```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`
3. Access the API documentation at `http://localhost:8000/docs`

## Deployment

This template uses Zappa for deploying to AWS Lambda. Make sure you have your AWS credentials configured.

1. Initialize your deployment:

```bash
zappa init
```

2. Deploy to AWS Lambda:

```bash
zappa deploy production
```

3. Update an existing deployment:

```bash
zappa update production
```

## Creating Your Agent

1. Define your agent's behavior in `core/agent.py`
2. Add custom tools in `core/tools/`
3. Configure your agent's chain in `core/chains/`
4. Update the API endpoints in `main.py`

Example agent configuration:

```python
from langchain_core.agents import AgentExecutor
from core.tools import your_custom_tools
from core.chains import your_custom_chain

def create_agent():
    tools = your_custom_tools()
    chain = your_custom_chain()
    return AgentExecutor(tools=tools, chain=chain)
```

## Environment Variables

Required environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key
- `AWS_PROFILE`: AWS profile for deployment
- `ENVIRONMENT`: Development environment (dev/prod)
- Additional variables as needed for your agent

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
