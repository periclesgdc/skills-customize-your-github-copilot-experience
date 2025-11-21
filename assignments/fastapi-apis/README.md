# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build RESTful APIs using the FastAPI framework. Students will create endpoints to handle CRUD operations for a simple resource, such as a to-do list or a user database.

## 📝 Tasks

### 🛠️ Task 1: Setup FastAPI Project

#### Description
Set up a new FastAPI project and create the basic structure for the application.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn.
- Create a main application file (e.g., `main.py`).
- Run the FastAPI development server.

### 🛠️ Task 2: Create CRUD Endpoints

#### Description
Implement endpoints for Create, Read, Update, and Delete operations for a resource (e.g., tasks, users).

#### Requirements
Completed program should:

- Define a Pydantic model for the resource.
- Create endpoints for:
  - Adding a new resource.
  - Retrieving all resources.
  - Retrieving a resource by ID.
  - Updating a resource by ID.
  - Deleting a resource by ID.

### 🛠️ Task 3: Add Validation and Error Handling

#### Description
Enhance the API with input validation and proper error handling.

#### Requirements
Completed program should:

- Validate input data using Pydantic.
- Return appropriate HTTP status codes for success and error cases.
- Handle cases where a resource is not found.

### 🛠️ Task 4: Test the API

#### Description
Write tests to ensure the API works as expected.

#### Requirements
Completed program should:

- Use a testing library (e.g., `pytest`).
- Test all CRUD endpoints for expected behavior.
- Include edge cases in the tests.