# Task Management System

A comprehensive task management system built with Django and Django Rest Framework (DRF), featuring user authentication, task management, and project organization.

## 🚀 Learning Path & Project Evolution

This project serves as a step-by-step learning guide for mastering Django and DRF. Below are the key milestones implemented:

### 1. Basic API Lifecycle

The foundation of any Django API:

- **Routes**: Configuring `urls.py` to map paths to logic.
- **Views**: Creating functional views in `views.py` to handle `GET` and `POST` requests.
- **Models**: Designing the database schema in `models.py`.

### 2. Manual Data Handling vs. Serializers

We moved from manual dictionary construction to using **DRF Serializers**:

- **Validation**: Automatically validating incoming JSON data.
- **Serialization**: Effortlessly converting complex Model instances into JSON.
- **Pattern**: `serializer = TaskSerializer(data=request.data)` followed by `serializer.is_valid()`.

### 3. Intercepting Requests with Middleware

To gain better visibility into our system, we added custom **Middleware**:

- **Purpose**: Logging every request's method, path, and processing time.
- **Location**: `task_app/middleware.py`.
- **Registration**: Added to the `MIDDLEWARE` list in `settings.py`.

### 4. Scaling with ViewSets & Routers

As the project grew, we adopted **ViewSets** for the `job_app`:

- **Consistency**: Grouping `list`, `create`, `retrieve`, `update`, and `delete` logic.
- **Automation**: Using a `DefaultRouter` to automatically generate standard RESTful URL patterns.

### 5. Architectural Refactoring

We improved the project structure by nesting apps:

- **Nesting**: Moved `job_app` inside `task_app` to keep the root directory clean.
- **Configuration**: Updated `INSTALLED_APPS` and URL includes to recognize the new hierarchy.

---

## 🛠 Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (Fast Python package manager)
  - Install via curl: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - **Note**: After installing via curl, you may need to run `source $HOME/.local/bin/env` to add it to your PATH.
  - Or via pip: `pip install uv`
- Postman (for API testing)

## ⚙️ Installation & Setup

1. **Clone & Navigate**:

   ```bash
   cd django-task-application
   ```

2. **Environment & Dependencies (using `uv`)**:

   The project uses [uv](https://github.com/astral-sh/uv) for lightning-fast environment management.

   ```bash
   # Create virtual environment and install dependencies in one step
   uv sync
   
   # Or manually:
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

3. **Environment Configuration**:
   Create a `.env` file from `.env.example`.
   > [!TIP]
   > Use `POSTGRES_HOST=127.0.0.1` to avoid common connection hangs on some Linux distributions.

4. **Database (PostgreSQL)**:
   
   The project uses Docker to manage the database. Ensure Docker Desktop is running before starting.

   ```bash
   # Start the database container in the background
   docker compose up -d

   # Verify the container is running
   docker ps

   # To stop the database when finished
   docker compose down
   ```

   > [!IMPORTANT]
   > The database is exposed on port **`5433`**. If you are using an external tool like DBeaver or pgAdmin, use `localhost:5433`.

5. **Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Run Server**:

   ```bash
   python manage.py runserver
   ```

## 🔗 Key API Endpoints

- **Landing Page**:
  - `GET /`: API overview and endpoint list (Resolves root 404).
- **Tasks**:
  - `POST /task/add/`: Create a new task.
  - `GET /task/get/`: List tasks (optional `?user_id=X` filter).
  - `GET /task/get/<id>/`: Retrieve a specific task by ID.
- **Users**:
  - `POST /user/add/`: Create a user.
  - `GET /user/get/`: List all users.
- **Jobs** (ViewSets):
  - `GET /jobs/`: List all jobs.
  - `POST /jobs/`: Create a new job. (`id` and `created_at` are auto-generated).
  - `GET /jobs/<id>/`: Retrieve a specific job.
  - `PUT /jobs/<id>/`: Update a specific job (Full).
  - `PATCH /jobs/<id>/`: Update a specific job (Partial).
  - `DELETE /jobs/<id>/`: Delete a specific job.

---
*Created as part of the Task Management Backend Project.*
