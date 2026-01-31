# TodoApp

A simple, full-featured Todo application built with Python. This project demonstrates CRUD operations, authentication, and user management using FastAPI, SQLAlchemy, and Jinja2 templates.

## Features
- User registration and authentication
- Add, edit, and delete todos
- Admin and user roles
- RESTful API endpoints
- HTML templates for UI
- Static files for CSS and JS
- Alembic for database migrations
- Unit tests for core functionality

## Project Structure
```
TodoApp/
├── alembic/            # Database migrations
├── routers/            # API route handlers (admin, auth, todos, users)
├── static/             # Static files (CSS, JS)
├── templates/          # Jinja2 HTML templates
├── test/               # Unit tests
├── database.py         # Database connection and models
├── main.py             # FastAPI app entry point
├── models.py           # SQLAlchemy models
├── alembic.ini         # Alembic config
├── .env                # Environment variables (not tracked)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## Setup
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd TodoApp
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   - Copy `.env.example` to `.env` and update values as needed.

5. **Run database migrations:**
   ```bash
   alembic upgrade head
   ```
6. **Start the app:**
   ```bash
   uvicorn main:app --reload
   ```
7. **Run tests:**
   ```bash
   pytest
   ```

## Usage
- Access the app at [http://localhost:8000](http://localhost:8000)
- Register a new user or log in
- Add, edit, and delete your todos
- Admin users can manage all users and todos

## License
This project is licensed under the MIT License.
