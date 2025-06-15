from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Review, Book, User

reviewBp = Blueprint('reviews', __name__)


# Submit review for a book
@reviewBp.route('/api/books/<int:bookId>/reviews', methods=['POST'])
@jwt_required()
def submitReview(bookId):
    data = request.get_json()
    content = data.get('content')
    rating = data.get('rating')

    if not content or rating is None:
        return jsonify({'message': 'Content and rating are required'}), 400

    book = Book.query.get(bookId)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    identity = get_jwt_identity()
    print(identity)
    userId = identity.get('id')

    review = Review(content=content, rating=rating, userId=userId, bookId=bookId)

    db.session.add(review)
    db.session.commit()

    return jsonify({'message': 'Review submitted successfully'}), 201


# List all reviews for a book
@reviewBp.route('/api/books/<int:bookId>/reviews', methods=['GET'])
def listReviews(bookId):
    book = Book.query.get(bookId)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    reviews = Review.query.filter_by(bookId=bookId).all()
    result = []
    for review in reviews:
        user = User.query.get(review.userId)
        result.append({
            'reviewId': review.id,
            'content': review.content,
            'rating': review.rating,
            'user': user.username
        })

    return jsonify(result), 200


# Get all reviews submitted by the current user
@reviewBp.route('/api/usr/reviews', methods=['GET'])
@jwt_required()
def myReview():
    identity = get_jwt_identity()
    userId = identity.get('id')

    reviews = Review.query.filter_by(userId=userId).all()
    result = []

    for review in reviews:
        book = Book.query.get(review.bookId)
        result.append({
            'reviewId': review.id,
            'content': review.content,
            'rating': review.rating,
            'book': book.title
        })

    return jsonify(result), 200
