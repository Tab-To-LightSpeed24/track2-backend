# ProU API – Employee & Task Management

A clean and well-documented RESTful API for managing employees and their assigned tasks. Built with FastAPI, this project demonstrates a logically solid relational schema and a clean API design.

The API provides endpoints to create, read, update, and delete employees and tasks, link tasks to employees, and view summary statistics.

## Tech Stack

*   **Backend:** [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
*   **Database:** [SQLite](https://www.sqlite.org/index.html) - A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
*   **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL Toolkit and Object Relational Mapper.
*   **Data Validation:** [Pydantic](https://docs.pydantic.dev/) - Data validation and settings management using Python type annotations.
*   **Web Server:** [Uvicorn](https://www.uvicorn.org/) - An ASGI web server implementation for Python.

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository (Optional)

If you haven't already, clone the repository to your local machine.

```bash
git clone <your-repository-url>
cd track2-backend
```

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

*   **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

*   **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3. Install Dependencies

Create a `requirements.txt` file in the root of your project with the content below, and then install the packages using pip.

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the FastAPI application using the Uvicorn server.

```bash
uvicorn app.main:app --reload
```

The `--reload` flag ensures that the server will automatically restart whenever you make a code change.

### 5. Access the API

Once the server is running, you can access the API at `http://127.0.0.1:8000`.

The interactive API documentation (Swagger UI) is available at:
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

## API Endpoints

A brief overview of the available endpoints. For detailed information and to try them out, please visit the [/docs](http://127.0.0.1:8000/docs) page.

### Employees
*   `POST /employees/`: Create a new employee.
*   `GET /employees/`: List all employees. Supports filtering by `?active=true`.
*   `GET /employees/{id}`: Retrieve a single employee by their ID.
*   `PUT /employees/{id}`: Update an employee's details.
*   `DELETE /employees/{id}`: Soft delete an employee by setting them as inactive.

### Tasks
*   `POST /tasks/`: Create a new task.
*   `GET /tasks/`: List all tasks. Supports filtering by `?status=`, `?priority=`, and `?employee_id=`.
*   `GET /tasks/{id}`: Retrieve a single task by its ID.
*   `PUT /tasks/{id}`: Update a task's details.
*   `DELETE /tasks/{id}`: Permanently delete a task.

### Bonus Endpoints
*   `GET /employees/{id}/tasks`: Get all tasks assigned to a specific employee.
*   `GET /stats/overview`: Provides a summary of key statistics:
    ```json
    {
      "total_tasks": 0,
      "completed_tasks": 0,
      "overdue_tasks": 0,
      "unassigned_tasks": 0
    }
    ```

## Screenshots

### Interactive API Documentation (Swagger UI)
You can test all endpoints directly from your browser.

<img width="1919" height="904" alt="image" src="https://github.com/user-attachments/assets/e815f82f-540a-4e15-af00-00b8cbb65c8c" />

### Example: Creating an Employee

<img width="1919" height="905" alt="image" src="https://github.com/user-attachments/assets/31b83780-2652-4413-8266-132fbb1054d8" />

### Get a Specific Employee

<img width="1919" height="901" alt="image" src="https://github.com/user-attachments/assets/63a6a439-83d6-4734-927a-775dcd5d75ac" />

### Update an Employee

<img width="1919" height="912" alt="image" src="https://github.com/user-attachments/assets/0d9112c0-a965-4366-80e8-ffdb7acd39b6" />

## Delete an Employee

<img width="1919" height="904" alt="image" src="https://github.com/user-attachments/assets/f18101a4-2f72-4e56-801c-723deabadb8f" />

## Create a Task

<img width="1919" height="905" alt="image" src="https://github.com/user-attachments/assets/a8e61c7e-90f5-4b46-9537-ac8eaa15d0c3" />

## List all Tasks

<img width="1919" height="909" alt="image" src="https://github.com/user-attachments/assets/675a6ff9-a42a-4911-a2d4-aea19a7de469" />

## Update a Task info

<img width="1919" height="909" alt="image" src="https://github.com/user-attachments/assets/7096aeac-a611-47a6-9fe6-77fb24b3a433" />

## Bonus Endpoints: Get Tasks for an Employee

<img width="1919" height="920" alt="image" src="https://github.com/user-attachments/assets/db8d3b9a-0885-450a-a093-c223de9b0900" />

## Assumptions & Bonus Features

*   **Soft Deletes for Employees**: When an employee is "deleted" via the `DELETE /employees/{id}` endpoint, their record is not removed from the database. Instead, their `is_active` flag is set to `false`. This preserves data integrity, ensuring that tasks previously assigned to that employee retain their historical context.
*   **Hard Deletes for Tasks**: Tasks are considered more ephemeral. The `DELETE /tasks/{id}` endpoint performs a hard delete, permanently removing the task from the database.
*   **Root Endpoint**: A welcoming root endpoint at `/` has been added for a better user experience.
*   **Enum-based Fields**: The `status` and `priority` fields on the `Task` model use Python's `Enum` for better data consistency and validation.
*   **Automatic Documentation**: The use of FastAPI and Pydantic provides rich, automatic, and interactive API documentation, which was a key goal of the project.
