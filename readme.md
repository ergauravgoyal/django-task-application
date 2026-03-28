## Task Management System

A comprehensive task management system built with Django, featuring user authentication, task management, and project organization.

### Features

- **User Authentication**: Secure login and registration system.
- **Task Management**: Create, update, delete, and filter tasks.
- **Project Organization**: Group tasks into projects.
- **Responsive Design**: Built with Bootstrap for a seamless mobile and desktop experience.

### Prerequisites

- Python 3.6+
- pip (Python package installer)
- Docker
- Docker Compose

### Installation

1. **Clone the repository** (or download the source code).

2. **Navigate to the project directory**:
   ```bash
   cd django-task-application
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create environment file**:
   ```bash
   cp .env.example .env
   ```

6. **Start PostgreSQL with Docker**:
   ```bash
   docker run --name task_management_postgres \
     -e POSTGRES_DB=task_management_db \
     -e POSTGRES_USER=task_user \
     -e POSTGRES_PASSWORD=task_password \
     -p 5433:5432 \
     -d postgres:16
   ```

7. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

8. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

### Running the Server

Run the development server using the following command:

```bash
python manage.py runserver
```

Open your browser and navigate to `http://localhost:8000/` to access the application.

### Database Configuration

The project is configured to use PostgreSQL via environment variables.

Example values in `.env`:

```env
POSTGRES_DB=task_management_db
POSTGRES_USER=task_user
POSTGRES_PASSWORD=task_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
```

### Usage

- **Login**: Use the credentials created during the superuser setup or register a new account.
- **Dashboard**: View all your tasks.
- **Projects**: Create and manage projects to organize your tasks.
- **Tasks**: Add new tasks, set due dates, and mark them as complete.

### License

This project is licensed under the terms of the MIT license.

## lets define the steps to create an api route

1. define the route in urls.py
    path("task/add/", add_task),
2. define the view in views.py
    define the action add_task(request: Request):
3. define the model in models.py
    class Task(models.Model):
