# Templates HQ

Templates HQ is a centralized repository of production-ready templates for various programming languages, frameworks, and use cases. It follows a monorepo approach to maintain all templates in one place for easier discovery, maintenance, and consistency.

## 🚀 Available Templates

### Python Templates

| Template                                                           | Description                                                                                           | Tech Stack                                                    | Use Cases                                                     |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| [lambda-agent-builder](python_templates/aws_lambda_agent_builder/) | A powerful template for building AI agents using Python, AWS Lambda, FastAPI, and LangChain/LangGraph | Python 3.12+, FastAPI, AWS Lambda, Zappa, LangChain/LangGraph | Conversational AI agents, Serverless LLM-powered applications |
| [lambda-fastapi](python_templates/aws_lambda_fast_api/)            | A lightweight template for building FastAPI applications deployed on AWS Lambda                       | Python 3.12+, FastAPI, AWS Lambda, Zappa, Mangum              | RESTful APIs, Microservices, Serverless web applications      |

### Cursor Templates

| Template                            | Description                                                            | Tech Stack                   | Use Cases                                                      |
| ----------------------------------- | ---------------------------------------------------------------------- | ---------------------------- | -------------------------------------------------------------- |
| [agent-rulebook](cursor_templates/) | A comprehensive template for Cursor AI agent development with rulebook | Cursor, Claude/GPT, Markdown | Custom AI coding assistants, Specialized development workflows |

## 📂 Repository Structure

```
templates-hq/
├── .cursor/             # Cursor IDE configuration and rules
├── metadata/            # Metadata files for template discovery and information
│   ├── python.json      # Metadata for Python templates with detailed implementation info
│   └── cursor.json      # Metadata for Cursor templates with detailed implementation info
├── python_templates/    # Python template implementations
│   ├── aws_lambda_agent_builder/   # AI agent on AWS Lambda template
│   └── aws_lambda_fast_api/        # FastAPI on AWS Lambda template
├── cursor_templates/    # Cursor AI agent templates
│   ├── agent.md         # Agent persona definition
│   └── rulebook.md      # Agent rulebook and guidelines
└── README.md            # This file
```

## 🧩 Features

- **Production-Ready**: Templates are designed following best practices and patterns
- **Well-Documented**: Each template includes comprehensive documentation with contextual comments
- **Organized Structure**: Consistent organization of templates by language
- **Metadata**: JSON files provide structured information about each template with implementation details
- **Serverless**: Focus on serverless architectures for scalability and cost-efficiency
- **Developer-Friendly**: Designed for easy understanding with detailed docstrings and usage guidance

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

Look through the table above or browse the repository structure to find the right template for your needs. Each template directory contains:

- Detailed README.md with information about features, setup, and usage
- Well-commented code files with contextual information for easier understanding
- Example implementations to help you get started quickly

You can also check the metadata JSON files in the `metadata/` directory for structured information about each template, including:

- Detailed structure information
- Key files and their purposes
- Implementation details
- Common modification patterns

## 👨‍💻 Template Features

### lambda-agent-builder

- LangChain/LangGraph integration for building AI agents
- Tool and chain architecture for extensible agent capabilities
- Context management for conversational applications
- System prompt customization
- Function calling capabilities for external integrations

### lambda-fastapi

- API versioning and structured route organization
- Standardized error handling for consistent API responses
- Comprehensive logging with Loguru
- Environment-specific configuration
- AWS Lambda deployment via Zappa

### agent-rulebook

- Structured agent persona definition
- Comprehensive rulebook for consistent behavior
- Clear guidelines for AI coding assistant behavior
- Customizable domains of expertise
- Integration with Cursor's context system

## 🤝 Contributing

Contributions are welcome! If you'd like to add a new template or improve an existing one:

1. Fork this repository
2. Create your template in the appropriate language directory
3. Add metadata information to the relevant JSON file
4. Add comprehensive docstrings and contextual comments
5. Submit a pull request with a detailed description of your template

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
