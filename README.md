# Employee Management System API

A FastAPI-based REST API for managing employees and departments with authentication and logging capabilities.

## Features

- User authentication with JWT tokens
- Employee management (CRUD operations)
- Department management (CRUD operations)
- Health check endpoint
- Comprehensive logging system
- File-based JSON storage
- Password encryption with salt

## Project Structure

```
.
├── app
│   ├── config
│   │   ├── config.json
│   │   ├── database.py
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── data
│   │   ├── departments.json
│   │   ├── employees.json
│   │   └── users.json
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── department.py
│   │   ├── employee.py
│   │   ├── __init__.py
│   │   └── user.py
│   ├── routers
│   │   ├── auth.py
│   │   ├── departments.py
│   │   ├── employees.py
│   │   ├── health.py
│   │   └── __init__.py
│   └── utils
│       ├── auth.py
│       ├── __init__.py
│       └── logger.py
├── docker-compose.yml
├── Dockerfile
├── logs/
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd employee-management-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server with:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

After starting the server, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

### Available Endpoints

#### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get access token

#### Health Check
- `GET /health` - Check API health status (no authentication required)

#### Employees
- `GET /employees` - List all employees
- `POST /employees` - Create a new employee
- `PUT /employees/{employee_id}` - Update an employee (full update)
- `PATCH /employees/{employee_id}` - Update an employee (partial update)
- `DELETE /employees/{employee_id}` - Delete an employee
- `GET /employees/current-user` - Get current user information

#### Departments
- `GET /departments` - List all departments
- `POST /departments` - Create a new department
- `PUT /departments/{department_id}` - Update a department (full update)
- `PATCH /departments/{department_id}` - Update a department (partial update)
- `DELETE /departments/{department_id}` - Delete a department

## Authentication

The API uses JWT tokens for authentication. To access protected endpoints:
1. Register a user using `/auth/register`
2. Login using `/auth/login` to get an access token
3. Include the token in the Authorization header: `Bearer <token>`

## Logging

Logs are stored in the `logs` directory with the following format:
- File naming: `log-{HOUR}-{DAY}-{MONTH}-{YEAR}.log`
- Log format:
```
TIMESTAMP - Event or operation Name
LOG
-------------------------------------
```

## Data Storage

The application uses JSON files for data storage:
- `data/users.json` - User information
- `data/employees.json` - Employee records
- `data/departments.json` - Department information

## Security Features

- Password hashing with bcrypt
- JWT token-based authentication
- Salted password storage
- Protected endpoints requiring authentication

## Error Handling

The API implements proper error handling with appropriate HTTP status codes and error messages for:
- Authentication failures
- Resource not found
- Invalid input data
- Duplicate entries
- Server errors

## Development

To contribute to the project:
1. Create a new branch for your feature
2. Implement your changes
3. Write or update tests if necessary
4. Submit a pull request

## Watch dev container logs

As the application is running in a dev container that starts the server automatically, the logs can be watched from another terminal using docker:

```sh
docker logs -f <CONTAINER_ID> | <CONTAINER_NAME>
```

## Dev Container

Python base image is available [here](https://mcr.microsoft.com/en-us/artifact/mar/devcontainers/python/about)

## Swarm

```sh
# build first
docker build -t fast-api:1 .

# stack
docker stack deploy fast-web --compose-file docker-compose.yml

# or a single service
docker service create --name web-1 \
--publish 8001:8000 --replicas 1 fast-api:1
```
