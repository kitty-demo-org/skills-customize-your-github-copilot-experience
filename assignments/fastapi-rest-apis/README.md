# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, high-performance REST APIs using the FastAPI framework. You'll create endpoints that handle HTTP requests, work with request/response models, and understand the fundamentals of API design.

## 📝 Tasks

### 🛠️ Create a Basic REST API with FastAPI

#### Description
Build a REST API with FastAPI that manages a collection of items. Implement endpoints for creating, reading, updating, and deleting items (CRUD operations). Use Pydantic models for request/response validation.

#### Requirements
Completed program should:

- Create a FastAPI application with a root endpoint that returns a welcome message
- Implement GET endpoint to retrieve all items from a list or database
- Implement POST endpoint to create a new item with proper validation using Pydantic models
- Implement GET endpoint with path parameter to retrieve a specific item by ID
- Implement PUT endpoint to update an existing item by ID
- Implement DELETE endpoint to remove an item by ID
- Include proper HTTP status codes (200, 201, 404, 400) for different responses

### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance your API with robust data validation and meaningful error messages. Use Pydantic models to define the structure of your data and handle edge cases gracefully.

#### Requirements
Completed program should:

- Define Pydantic models for request and response data validation
- Validate query parameters and path parameters appropriately
- Return meaningful error responses when items are not found (404)
- Return validation error responses for invalid input (400)
- Include descriptive error messages that help clients understand what went wrong
