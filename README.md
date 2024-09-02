# Tasklaunchr 📝

This Django-based web application provides a system for managing todo lists and items. Built using Django and various Python libraries, it offers an interface for users to create, edit, and manage their todo lists and items.

## Features

- User authentication (signup, login, logout)
- Create, edit, and delete todo lists
- Add, edit, and delete todo items within lists
- Mark todo items as completed
- Search functionality for todo items

## Technologies Used

- Python 3.10
- Django 5.0.6
- Docker
- SQLite (for development)

### Key Dependencies

- Django==5.0.6

## Prerequisites

1. Install [Docker](https://docs.docker.com/get-docker/).
2. Ensure you have [Docker Compose](https://docs.docker.com/compose/install/) installed.

## How to Use

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/gvilloslado/tasklaunchr.git
   cd tasklaunchr
   ```

2. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```

3. Access the application at:
   `http://localhost:8000`

4. To create an admin user, run:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. To stop the application, use:
   ```bash
   docker-compose down
   ```

## Project Structure

- `accounts/`: User authentication app
- `todos/`: Main todo list and item management app
- `brain_two/`: Project settings and main URL configuration
