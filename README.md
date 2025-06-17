# Task Manager with Django and MongoDB

A task management application built with Django and MongoDB using MongoEngine ODM.

## Features

- Create, read, update, and delete tasks
- Task attributes: title, description, status, priority, due date, tags, etc.
- User management for task assignment
- Clean, responsive UI built with Bootstrap

## Prerequisites

- Python 3.6+
- MongoDB 4.0+

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd task_manager
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure MongoDB is running on your system:
   - On Windows, start the MongoDB service
   - On macOS/Linux: `sudo systemctl start mongod` (or equivalent)

4. Run the Django development server:
   ```
   python manage.py runserver
   ```

5. Access the application at http://127.0.0.1:8000/

## Usage

- Create new tasks with the "Create Task" button
- View all tasks on the main page
- Click on a task to view its details
- Edit or delete tasks from the detail view
- Mark tasks as complete
- Manage users in the Users section

## Project Structure

- `tasks/models.py` - MongoDB document models (Task, User)
- `tasks/views.py` - CRUD views for tasks and users
- `tasks/forms.py` - Forms for task and user management
- `tasks/templates/` - HTML templates for the UI

## License

MIT