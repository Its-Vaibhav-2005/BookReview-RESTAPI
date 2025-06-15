from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Book
import json
bookBp = Blueprint('books', __name__)

def isAdmin():
    identity = json.loads(get_jwt_identity())
    print(identity)
    return identity.get('isAdmin', False)

# get all books
@bookBp.route('/api/books', methods=['GET'])
def getBooks():
    books= Book.query.all()
    return jsonify([
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
        } for book in books
    ]), 200

# get book by ID
@bookBp.route('/api/books/<int:Bookid>', methods=['GET'])
@jwt_required()
def getBook(Bookid):
    book = Book.query.filter_by(id=Bookid).first()
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify(
        {
            "id":book.id,
            "title":book.title,
            "author":book.author,
            "genre":book.genre,
        }
    ), 200

# add book
@bookBp.route('/api/books', methods=['POST'])
@jwt_required()
def addBook():
    if not isAdmin():
        return jsonify({'message': 'Admin privileges required'}), 403

    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    genre = data.get('genre')

    if not title or not author:
        return jsonify({'message': 'Title and author are required'}), 400

    newBook = Book(title=title, author=author, genre=genre)
    db.session.add(newBook)
    db.session.commit()

    return jsonify({'message': 'Book added successfully'}), 201

# update the books
@bookBp.route('/api/books/<int:Bookid>', methods=['PUT'])
@jwt_required()
def updateBook(Bookid):
    if not isAdmin():
        return jsonify({'message': 'Admin privileges required'}), 403

    book = Book.query.filter_by(id=Bookid).first()
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.genre = data.get('genre', book.genre)

    db.session.commit()
    return jsonify({'message': 'Book updated successfully'}), 200

# delete book
@bookBp.route('/api/books/<int:Bookid>', methods=['DELETE'])
@jwt_required()
def deleteBook(Bookid):
    if not isAdmin():
        return jsonify({'message': 'Admin privileges required'}), 403

    book = Book.query.get(Bookid)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'}), 200
