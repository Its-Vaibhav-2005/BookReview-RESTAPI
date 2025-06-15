from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import db, User
import json
authBp = Blueprint('auth', __name__)

@authBp.route('/api/register', methods=['POST'])
def registerUser():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    isAdmin = data.get('isAdmin', False)

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    newUser = User(username=username, isAdmin=isAdmin)
    newUser.setPasswd(password)
    db.session.add(newUser)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@authBp.route('/api/login', methods=['POST'])
def loginUser():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.checkPasswd(password):
        accessToken = create_access_token(identity=json.dumps({'id': user.id, 'isAdmin': user.isAdmin}))
        return jsonify({'access_token': accessToken}), 200
    return jsonify({'message': 'Invalid credentials'}), 401