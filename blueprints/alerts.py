from flask import Blueprint, request, jsonify
from db import db
from models.alert import AlertModel
from schemas.schemas import AlertSchema


alert_blueprint = Blueprint('alerts', __name__)

@alert_blueprint.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = AlertModel.query.all()
    return jsonify([alert.serialize() for alert in alerts]), 200

@alert_blueprint.route('/alerts/<int:id>', methods=['GET'])
def get_alert(id):
    alert = AlertModel.query.get(id)
    if alert:
        return jsonify(alert.serialize()), 200
    else:
        return jsonify({"message": "Alert not found"}), 404

@alert_blueprint.route('/alerts', methods=['POST'])
def create_alert():
    data = request.get_json()
    new_alert = AlertModel(
        user_id=data['user_id'],
        message=data['message'],
        timestamp=data['timestamp']
    )
    db.session.add(new_alert)
    db.session.commit()
    return jsonify(new_alert.serialize()), 201

@alert_blueprint.route('/alerts/<int:id>', methods=['DELETE'])
def delete_alert(id):
    alert = AlertModel.query.get(id)
    if alert:
        db.session.delete(alert)
        db.session.commit()
        return jsonify({"message": "Alert deleted"}), 200
    else:
        return jsonify({"message": "Alert not found"}), 404

@alert_blueprint.route('/alerts/<int:id>', methods=['PUT'])
def update_alert(id):
    data = request.get_json()
    alert = AlertModel.query.get(id)
    if alert:
        alert.user_id = data['user_id']
        alert.message = data['message']
        alert.timestamp = data['timestamp']
        db.session.commit()
        return jsonify(alert.serialize()), 200
    else:
        return jsonify({"message": "Alert not found"}), 404