from flask import Blueprint, request, jsonify
from db import db

from models import UserModel
from schemas.schemas import UserSchema



user_blueprint = Blueprint('user', __name__)



@user_blueprint.route('/users', methods=['GET'])
def get_users():
    # Get all users from the database
    users = UserModel.query.all()

    # Serialize the users using the user schema
    user_schema = UserSchema(many=True)
    users_data = user_schema.dump(users)

    return jsonify(users_data)

@user_blueprint.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    # Get the user by id
    user = UserModel.query.get(id)

    # Return a 404 error if the user does not exist
    if not user:
        return '', 404

    # Serialize the user using the user schema
    user_schema = UserSchema()
    user_data = user_schema.dump(user)

    return jsonify(user_data)

@user_blueprint.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    # Get the user by id
    user = UserModel.query.get(id)

    # Return a 404 error if the user does not exist
    if not user:
        return '', 404

    # Deserialize the request data using the user schema
    user_schema = UserSchema()
    update_data = user_schema.load(request.get_json())

    # Update the user object with the new data
    for key, value in update_data.items():
        setattr(user, key, value)

    # Commit the changes to the session
    db.session.commit()

    # Serialize the updated user object and return it as the response
    user_data = user_schema.dump(user)
    return jsonify(user_data)

# user_blueprint.py
# ...

@user_blueprint.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Get the user by id
    user = UserModel.query.get(id)

    # Return a 404 error if the user does not exist
    if not user:
        return '', 404

    # Delete the user from the session
    db.session.delete(user)
    db.session.commit()

    # Return a 204 status code indicating that the deletion was successful
    return '', 204





