from flask import  request, jsonify
from db import db
from models.field import FieldModel
from schemas.schemas import FieldSchema
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("fields", __name__, description="Opertations on fields")


@blp.route('/fields', methods=['GET'])
def get_fields():
    fields = FieldModel.query.all()
    return jsonify([field.to_json() for field in fields])

@blp.route('/fields', methods=['POST'])
def create_field():
    data = request.get_json()
    new_field = FieldModel(
        size=data['size'],
        type=data['type'],
        location=data['location'],
        name=data['name'],
        user_id=data['user_id']
    )
    db.session.add(new_field)
    db.session.commit()
    return jsonify(new_field.to_json())

@blp.route('/fields/<int:id>', methods=['GET'])
def get_field_by_id(id):
    field = FieldModel.query.get(id)
    return jsonify(field.to_json())

@blp.route('/fields/<int:id>', methods=['PUT'])
def update_field_by_id(id):
    data = request.get_json()
    field = FieldModel.query.get(id)
    field.size = data['size']
    field.type = data['type']
    field.location = data['location']
    field.name = data['name']
    field.user_id = data['user_id']
    db.session.commit()
    return jsonify(field.to_json())

@blp.route('/fields/<int:id>', methods=['DELETE'])
def delete_field_by_id(id):
    field = FieldModel.query.get(id)
    db.session.delete(field)
    db.session.commit()
    return jsonify({'message': 'Field has been deleted'})
