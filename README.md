# Book Management API

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)

A RESTful API for managing books, user authentication, and book reviews. This API allows users to register, login, manage books (for admin users), and submit reviews for books.

## Repository Information

- **Repository**: [BookReview-RESTAPI](https://github.com/Its-Vaibhav-2005/BookReview-RESTAPI)
- **Author**: Vaibhav

## Features

- User Authentication (Register/Login)
- JWT-based Authorization
- Book Management (CRUD operations)
- Book Reviews System
- Role-based Access Control (Admin/Regular Users)

## Tech Stack

- Python 3.x
- Flask (Web Framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- Flask-JWT-Extended (Authentication)
- Flask-SQLAlchemy (Database ORM)

## Project Structure

```
book-management/
├── app/
│   └── models.py         # Database models
├── routes/
│   ├── auth.py          # Authentication routes
│   ├── books.py         # Book management routes
│   └── reviews.py       # Review management routes
├── instance/
│   └── bookReview.db    # SQLite database
├── main.py              # Application entry point
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Code Architecture

The application follows a modular architecture with the following components:

1. **Models** (`app/models.py`):
   - User: Handles user authentication and authorization
   - Book: Manages book information
   - Review: Handles book reviews and ratings

2. **Routes** (`routes/`):
   - Authentication routes for user registration and login
   - Book management routes for CRUD operations
   - Review routes for submitting and retrieving reviews

3. **Main Application** (`main.py`):
   - Flask application configuration
   - Database initialization
   - JWT setup
   - Blueprint registration

## API Routes

| Method | Endpoint | Description | Auth Required | Admin Required |
|--------|----------|-------------|---------------|----------------|
| POST | `/api/register` | Register a new user | No | No |
| POST | `/api/login` | Login user | No | No |
| GET | `/api/books` | Get all books | No | No |
| GET | `/api/books/<id>` | Get book by ID | Yes | No |
| POST | `/api/books` | Add a new book | Yes | Yes |
| PUT | `/api/books/<id>` | Update a book | Yes | Yes |
| DELETE | `/api/books/<id>` | Delete a book | Yes | Yes |
| POST | `/api/books/<id>/reviews` | Submit a review | Yes | No |
| GET | `/api/books/<id>/reviews` | Get book reviews | No | No |
| GET | `/api/usr/reviews` | Get user's reviews | Yes | No |

## Code Examples

### User Registration
```python
# POST /api/register
{
    "username": "john_doe",
    "password": "secure_password",
    "isAdmin": false
}
```

### Book Creation (Admin Only)
```python
# POST /api/books
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Fiction"
}
```

### Submitting a Review
```python
# POST /api/books/1/reviews
{
    "content": "A masterpiece of American literature",
    "rating": 5
}
```

## Setup and Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with the following variables:
   ```
   JWT_SECRET_KEY=your_jwt_secret_key
   SECRET_KEY=your_flask_secret_key
   ```
5. Run the application:
   ```bash
   python main.py
   ```

The server will start on `http://localhost:3100`

## Security Features

- Password hashing using Werkzeug's security functions
- JWT-based authentication
- Role-based access control
- Protected routes using JWT tokens
- Admin-only routes for book management

## Database Schema

### User Table
- id (Primary Key)
- username (Unique)
- password (Hashed)
- isAdmin (Boolean)

### Book Table
- id (Primary Key)
- title
- author
- genre

### Review Table
- id (Primary Key)
- content
- rating
- userId (Foreign Key)
- bookId (Foreign Key)

## Error Handling

The API returns appropriate HTTP status codes and error messages:
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Contact

For any questions or suggestions, please open an issue in the [GitHub repository](https://github.com/Its-Vaibhav-2005/BookReview-RESTAPI/issues). 