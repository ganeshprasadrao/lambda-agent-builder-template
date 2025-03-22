# Templates HQ

Templates HQ is a centralized repository of production-ready templates for various programming languages, frameworks, and use cases. It follows a monorepo approach to maintain all templates in one place for easier discovery, maintenance, and consistency.

## 🚀 Available Templates

### Python Templates

| Template                                                           | Description                                                                                           | Tech Stack                                                    | Use Cases                                                     |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| [lambda-agent-builder](python_templates/aws_lambda_agent_builder/) | A powerful template for building AI agents using Python, AWS Lambda, FastAPI, and LangChain/LangGraph | Python 3.12+, FastAPI, AWS Lambda, Zappa, LangChain/LangGraph | Conversational AI agents, Serverless LLM-powered applications |
| [lambda-fastapi](python_templates/aws_lambda_fast_api/)            | A lightweight template for building FastAPI applications deployed on AWS Lambda                       | Python 3.12+, FastAPI, AWS Lambda, Zappa, Mangum              | RESTful APIs, Microservices, Serverless web applications      |

## 📂 Repository Structure

```
templates-hq/
├── .cursor/             # Cursor IDE configuration and rules
├── metadata/            # Metadata files for template discovery and information
│   └── python.json      # Metadata for Python templates
├── python_templates/    # Python template implementations
│   ├── aws_lambda_agent_builder/   # AI agent on AWS Lambda template
│   └── aws_lambda_fast_api/        # FastAPI on AWS Lambda template
└── README.md            # This file
```

## 🧩 Features

- **Production-Ready**: Templates are designed following best practices and patterns
- **Well-Documented**: Each template includes comprehensive documentation
- **Organized Structure**: Consistent organization of templates by language
- **Metadata**: JSON files provide structured information about each template
- **Serverless**: Focus on serverless architectures for scalability and cost-efficiency

## 🛠️ Using Templates

Each template folder contains a comprehensive README.md with specific instructions, but here's the general process:

1. Clone this repository:

   ```bash
   git clone https://github.com/ganeshprasadrao/templates-hq.git
   ```

2. Navigate to the template directory you want to use:

   ```bash
   cd templates-hq/python_templates/aws_lambda_fast_api
   ```

3. Follow the template-specific README.md for setup and usage instructions

## 🔍 Finding Templates

Look through the table above or browse the repository structure to find the right template for your needs. Each template directory contains a detailed README.md with information about features, setup, and usage.

You can also check the metadata JSON files in the `metadata/` directory for structured information about each template.

## 🤝 Contributing

Contributions are welcome! If you'd like to add a new template or improve an existing one:

1. Fork this repository
2. Create your template in the appropriate language directory
3. Add metadata information to the relevant JSON file
4. Submit a pull request with a detailed description of your template

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
