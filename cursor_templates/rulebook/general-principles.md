# General Coding Principles

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
