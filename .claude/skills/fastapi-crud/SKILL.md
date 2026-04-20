---
name: fastapi-crud
description: This skill provides automated generation of CRUD (Create, Read, Update, Delete) operations for FastAPI applications. It creates complete router modules with proper error handling, validation, and database integration. Use when you need to:

- Add new resource endpoints to a FastAPI application
- Generate boilerplate CRUD operations for new models
- Ensure consistent API patterns across resources
- Create rapid prototyping of RESTful APIs
---
## Workflow Steps

### 1. Model Analysis
- Analyze the SQLAlchemy model to understand fields and relationships
- Identify primary keys and foreign keys
- Determine required vs optional fields

### 2. Schema Generation
- Create Pydantic schemas for request/response
- Generate Create, Update, and Response schemas
- Include proper validation rules

### 3. Router Creation
- Generate FastAPI router with all CRUD endpoints
- Implement dependency injection for database sessions
- Add authentication dependencies where needed

### 4. Error Handling
- Implement proper HTTP status codes
- Add validation error responses
- Include not found error handling

## Output Structure
```
app/routers/{resource}.py
app/schemas/{resource}.py (if not exists)
```

## Example Usage
When asked to "create CRUD endpoints for User model", this skill will:
1. Read the User model from models.py
2. Generate appropriate schemas in schemas.py
3. Create a complete router with GET, POST, PUT, DELETE endpoints
4. Ensure proper database session handling and error responses

## Best Practices
- Always use dependency injection for database sessions
- Include proper type hints
- Add comprehensive docstrings
- Follow RESTful naming conventions
- Implement user-scoped queries for multi-tenant apps