---
name: api-testing

description: This skill provides comprehensive API testing capabilities for FastAPI applications. It generates test suites, mocks, and validation scripts to ensure API endpoints work correctly. Use when you need to:
- Test new API endpoints
- Perform regression testing after changes
- Validate authentication and authorization
- Performance testing API responses
- Integrate testing with database
---
## Workflow Steps

### 1. Endpoint Discovery
- Analyze router files to identify all endpoints
- Extract HTTP methods, paths, and parameters
- Identify authentication requirements

### 2. Test Case Generation
- Create unit tests for each endpoint
- Generate integration tests with database
- Include edge cases and error scenarios

### 3. Mock Setup
- Create mock data for testing
- Set up test database fixtures
- Configure authentication mocks

### 4. Test Execution
- Run tests with pytest
- Generate coverage reports
- Validate response schemas

## Output Structure
```
tests/
├── test_{resource}.py
├── conftest.py
├── fixtures/
└── __init__.py
```

## Example Usage
When asked to "test the user authentication endpoints", this skill will:
1. Analyze auth.py router
2. Generate test cases for login, registration, token validation
3. Create mock users and test database
4. Run tests and report results

## Best Practices
- Use pytest fixtures for database setup
- Test both success and failure scenarios
- Include authentication testing
- Validate response data types
- Use descriptive test names
- Mock external dependencies
- Test rate limiting and validation