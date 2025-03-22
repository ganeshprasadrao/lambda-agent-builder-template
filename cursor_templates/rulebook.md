# Master Coding Rulebook

## 1. General Coding Principles

- **Working With Plan**: Always work according to the plan and don't deviate, if you have ideas then we can discuss. After making any significant changes, progress, or faced with issues, made assumptions, in the codebase, then update the plan.md document accordingly to be always in sync
- **Prefer Simplicity:** Choose the simplest solution that gets the job done without unnecessary complexity.
- **Avoid Duplication:** Reuse existing logic where possible instead of duplicating functionality.
- **Environment Awareness:** Ensure compatibility across dev, test, and production environments.
- **Change Discipline:** Make only necessary changes that are well understood and directly related to the task.
- **Bug Fixing Practices:** Prioritize fixing issues using existing implementations before introducing new patterns.
- **Maintain Cleanliness & Organization:** Keep code modular, well-structured, and avoid overly long files (limit to 200-300 lines if possible).
- **Script Management:** Avoid one-off scripts; keep script usage minimal and necessary. If you write any one-off script delete them after use.
- **Data Handling:** Use mocking only in tests; avoid stubbing or fake data patterns in dev/prod.
- **Environment Files:** Never overwrite the `.env` file without confirmation.
- **Consistent Naming Conventions:** Follow PEP8 and use clear, descriptive, and consistent naming.

## 2. Documentation & Testing

- **Working With Plan**: Always work according to the plan and don't deviate, if you have ideas then we can discuss. After making any significant changes, progress, or faced with issues, made assumptions, in the codebase, then update the plan.md document accordingly to be always in sync
- **Documentation & Comments:** Provide meaningful docstrings and comments, especially for complex logic.
- **Unit Testing:** Write comprehensive tests using `pytest`, ensuring all tests are CI-integrated.
- **Error Handling & Logging:** Implement robust error handling and structured logging.
- **Modular Design & Separation of Concerns:** Keep code modular, refactor common logic into reusable components.
- **Type Annotations:** Use type hints to improve code clarity and enable static checking.
- **Performance & Optimization:** Optimize code only when necessary; premature optimization is discouraged.

## 3. Security & Best Practices

- **Security Best Practices:** Use environment variables for sensitive data; never hardcode credentials.
- **Version Control Practices:** Commit frequently with descriptive messages; use feature branches.
- **Code Formatting & Linting:** Enforce code style using `Black` and `Flake8`.
- **Continuous Integration & Delivery:** Ensure all tests pass in CI/CD before merging.
- **Scalability & Future-Proofing:** Design for scalability while maintaining backward compatibility.
- **Dependency Management:** Keep dependencies updated and document their purpose; avoid unnecessary packages.

## 4. Coding Workflow Preferences

- **Focus on Relevant Code:** Modify only areas directly related to the task.
- **Isolate Changes:** Do not touch unrelated parts of the codebase.
- **Test Thoroughly:** Ensure functionality is well-tested before finalizing changes.
- **Minimize Architectural Disruptions:** Avoid major refactors unless explicitly required.
- **Consider the Impact:** Evaluate how changes affect other parts of the system.
- **Commit with Clarity:** Keep commits concise, clear, and well-scoped.
- **Document Assumptions:** Note any assumptions or potential side effects.
- **Preserve Established Patterns:** Stick to existing best practices unless justified.
- **Avoid Overengineering:** Prioritize maintainability over unnecessary complexity.
- **Working With Plan**: Always work according to the plan and don't deviate, if you have ideas then we can discuss. After making any significant changes, progress, or faced with issues, made assumptions, in the codebase, then update the plan.md document accordingly to be always in sync

## 5. Execution Priorities & Mindset

1. **Fewer lines of code = Better code.**
2. **Work like a senior developer (10x engineer mindset).**
3. **Fully complete the feature before stopping.**
4. **When debugging, analyze the problem deeply before jumping to conclusions.**
5. **Do not remove existing comments.**

## 6. Project Execution Guidelines

- Keep the terminal open to monitor logs and API behavior dynamically.

## 7. Tech Stack Preferences

- **API Backend:** FastAPI (async, high-performance endpoints).
- **Relational Data:** Supabase + SQLModel ORM.
- **Knowledge Graph & Vector Storage:** Neo4j for semantic relationships and vector search.
- **AI Orchestration:** LangChain + LangGraph for multi-agent workflows.
- **Configuration:** Use environment variables for all settings.
- **Consistency:** Follow established tools and patterns unless necessary changes are justified.

## 8. Testing Workflow

### Test-Driven Development (TDD) Process

1. **Write tests first:**
   - Ensure tests cover success and failure cases.
   - Test agent tools independently before integrating them.
2. **Run tests frequently:**
   ```sh
   python -m pytest
   ```
   - Use `-k "test_name"` to run specific tests.
3. **Manual testing:**
   - Run API locally, test scripts, and inspect logs.

### Test Monitoring

1. **Log Analysis:**
   - Check agent initialization and tool execution logs.
   - Identify patterns in errors for systemic issues.
2. **Performance Metrics:**
   - Analyze API response times and optimize bottlenecks.
