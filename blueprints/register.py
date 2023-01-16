from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import  request, jsonify
from werkzeug.security import generate_password_hash
from models import UserModel
from schemas.schemas import UserSchema
from db import db

# Create a blueprint for the signup route

blp = Blueprint("register", __name__, description="Register")


@blp.route('/signup', methods=['POST'])
def signup():
    # Retrieve the user's information from the request
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = UserModel(username=data['username'], email=data['email'], password=hashed_password, admin=False)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return {'message': 'New user created.'}, 201