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
    "username": "Vaibhav Pandey",
    "password": "my-password",
    "isAdmin": true
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

### User Table Schema
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Unique identifier for user |
| username | VARCHAR(100) | UNIQUE, NOT NULL | User's login name |
| password | VARCHAR(128) | NOT NULL | Hashed password |
| isAdmin | BOOLEAN | DEFAULT FALSE | Admin privileges flag |

### Book Table Schema
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Unique identifier for book |
| title | VARCHAR(150) | NOT NULL | Book title |
| author | VARCHAR(100) | NOT NULL | Book author |
| genre | VARCHAR(100) | NULL | Book genre |

### Review Table Schema
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Unique identifier for review |
| content | TEXT | NOT NULL | Review text content |
| rating | INTEGER | NOT NULL | Rating (1-5) |
| userId | INTEGER | FOREIGN KEY | Reference to User table |
| bookId | INTEGER | FOREIGN KEY | Reference to Book table |

### Sample Data

#### Books Table Sample Entry
```json
{
    "id": 1,
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "genre": "Fantasy"
}
```

#### Reviews Table Sample Entry
```json
{
    "id": 1,
    "content": "A magical journey that introduces us to the wizarding world. Perfect for readers of all ages!",
    "rating": 5,
    "userId": 1,
    "bookId": 1
}
```

#### Users Table Sample Entry
```json
{
    "id": 1,
    "username": "Vaibhav Pandey",
    "password": "hashed_password_here",
    "isAdmin": true
}
```

### Relationships
- One User can have many Reviews (One-to-Many)
- One Book can have many Reviews (One-to-Many)
- Each Review belongs to one User and one Book (Many-to-One)

## Error Handling

| HTTP Status Code | Error Code | Description | Example Response |
|-----------------|------------|-------------|------------------|
| 200 | OK | Request successful | `{"message": "Operation successful"}` |
| 201 | Created | Resource created successfully | `{"message": "Book added successfully"}` |
| 400 | Bad Request | Invalid request parameters | `{"message": "Title and author are required"}` |
| 401 | Unauthorized | Authentication required | `{"message": "Invalid credentials"}` |
| 403 | Forbidden | Insufficient permissions | `{"message": "Admin privileges required"}` |
| 404 | Not Found | Resource not found | `{"message": "Book not found"}` |
| 409 | Conflict | Resource already exists | `{"message": "Username already exists"}` |
| 422 | Unprocessable Entity | Invalid data format | `{"message": "Invalid rating value"}` |
| 500 | Internal Server Error | Server-side error | `{"message": "Internal server error"}` |

### Common Error Scenarios

1. **Authentication Errors**
   - Invalid credentials
   - Missing JWT token
   - Expired JWT token

2. **Validation Errors**
   - Missing required fields
   - Invalid data types
   - Out of range values (e.g., rating > 5)

3. **Authorization Errors**
   - Non-admin user trying to modify books
   - User trying to modify another user's review

4. **Resource Errors**
   - Book not found
   - User not found
   - Review not found

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Contact

For any questions or suggestions, please open an issue in the [GitHub repository](https://github.com/Its-Vaibhav-2005/BookReview-RESTAPI/issues). 