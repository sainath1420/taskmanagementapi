## Task Management System
This project is a FastAPI and PostgresSQL based application for task management, where users can register, login, and perform CRUD operations on tasks.
The application is secured with user authentication, and tasks are encrypted for privacy. The backend is containerized using Docker, making it easy to run locally or deploy.

## Prerequisites

Docker

## Setting Up the Project Locally
### Clone the repository:

**bash**:

git clone repository_url

### Build and start the application:

docker-compose up --build

## Local Swagger URL:

http://localhost:9000/docs

**Register a User:** Use the /auth/register endpoint to create a new user by providing a valid email and password.

**Log In:** Once the user is registered, use the /auth/login endpoint to authenticate and obtain a token. The token will be required to perform any operations on tasks.

**Task Operations:** After logging in with valid credentials, use the following endpoints to manage tasks:

**Create Task:** POST /tasks/create

**Get All Tasks:** GET /tasks

**Update Task:** PUT /tasks/{task_id}

**Delete Task:** DELETE /tasks/{task_id}

## Postman Collection

A Postman collection containing all API endpoints, example requests, and responses is included in this repository. You can import the collection to your Postman app and use it for testing.

**Postman Collection**: [Download Postman Collection](./postman/TaskManagementAPI.postman_collection.json)

### Deployment
i have deployed this in Render platform

**Live URL** : https://taskmanagementapi-5za5.onrender.com/docs#/


## Stopping and Managing Containers
### Stop containers:

docker-compose stop
### Start or resume containers:

docker-compose start
### Remove containers:

docker-compose down
### Delete containers and all database data:

docker-compose down -v
