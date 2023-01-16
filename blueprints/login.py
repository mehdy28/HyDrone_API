from models import UserModel
from flask import Flask, request, jsonify, make_response
from schemas.schemas import UserSchema
from db import db
import jwt
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from functools import wraps
import datetime



# Create a blueprint for the login route
blp = Blueprint("login", __name__, description="Login")


from flask import  request, jsonify
from werkzeug.security import check_password_hash , generate_password_hash



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, 'SECRET_KEY')
            current_user = UserModel.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@blp.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = UserModel.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message' : 'The user has been deleted!'})

@blp.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = UserModel.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'SECRET_KEY')

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

@blp.route('/register', methods=['POST'])
def register():
    # Retrieve the user's information from the request
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = UserModel(username=data['username'], email=data['email'], password=hashed_password)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return {'message': 'New user created.'}, 201
