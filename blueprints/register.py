from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import UserModel
from schemas.schemas import UserSchema
from db import db

# Create a blueprint for the signup route
signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['POST'])
def signup():
    # Retrieve the user's information from the request
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = UserModel(name=data['name'], email=data['email'], password=hashed_password, admin=False)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return {'message': 'New user created.'}, 201