import jwt
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models import UserModel
from schemas.schemas import UserSchema
from db import db


# Create a blueprint for the login route
login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    # Retrieve the user's information from the request
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')

    # Check if the user provided an email or a name
    if email:
        user = UserModel.query.filter_by(email=email).first()
    elif name:
        user = UserModel.query.filter_by(name=name).first()
    else:
        return {'message': 'Please provide an email or a name.'}, 401

    # Check if the user exists and the password is correct
    if not user or not check_password_hash(user.password, password):
        return {'message': 'Could not verify'}, 401

    # Generate an access token and a refresh token for the user
    expiry = datetime.utcnow() + timedelta(minutes=30)
    access_token = jwt.encode({'user_id': user.id, 'exp': expiry}, "SECRET_KEY", algorithm='HS256')
    expiry = datetime.utcnow() + timedelta(hours=2)
    refresh_token = jwt.encode({'user_id': user.id, 'exp': expiry}, "SECRET_KEY", algorithm='HS256')

    # Return the user's information and the tokens
    return {'user': {'id': user.id, 'name': user.name, 'email': user.email}, 'access_token': access_token.decode('utf-8'), 'refresh_token': refresh_token.decode('utf-8')}, 200



