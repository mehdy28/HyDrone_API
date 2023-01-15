from flask import Blueprint, request, jsonify
from db import db
from models.drone import DroneModel, ScheduleModel
from schemas.schemas import DroneSchema


drones_blueprint = Blueprint('drones', __name__)
schedules_blueprint = Blueprint('schedules', __name__)

@drones_blueprint.route('/drones', methods=['GET'])
def get_drones():
    drones = DroneModel.query.all()
    return jsonify([drone.to_json() for drone in drones])

@drones_blueprint.route('/drones', methods=['POST'])
def create_drone():
    data = request.get_json()
    new_drone = DroneModel(
        type=data['type'],
        serial_number=data['serial_number'],
        location=data['location'],
        status=data['status']
    )
    db.session.add(new_drone)
    db.session.commit()
    return jsonify(new_drone.to_json())

@drones_blueprint.route('/drones/<int:id>', methods=['GET'])
def get_drone_by_id(id):
    drone = DroneModel.query.get(id)
    return jsonify(drone.to_json())

@drones_blueprint.route('/drones/<int:id>', methods=['PUT'])
def update_drone_by_id(id):
    data = request.get_json()
    drone = DroneModel.query.get(id)
    drone.type = data['type']
    drone.serial_number = data['serial_number']
    drone.location = data['location']
    drone.status = data['status']
    db.session.commit()
    return jsonify(drone.to_json())

@drones_blueprint.route('/drones/<int:id>', methods=['DELETE'])
def delete_drone_by_id(id):
    drone = DroneModel.query.get(id)
    db.session.delete(drone)
    db.session.commit()
    return jsonify({'message': 'Drone has been deleted'})
#################
#################
#################

@schedules_blueprint.route('/schedules', methods=['GET'])
def get_schedules():
    schedules = ScheduleModel.query.all()
    return jsonify([schedule.to_json() for schedule in schedules])

@schedules_blueprint.route('/schedules', methods=['POST'])
def create_schedule():
    data = request.get_json()
    new_schedule = ScheduleModel(
        drone_id=data['drone_id'],
        flight_time=data['flight_time'],
        field_id=data['field_id']
    )
    db.session.add(new_schedule)
    db.session.commit()
    return jsonify(new_schedule.to_json())

@schedules_blueprint.route('/schedules/<int:id>', methods=['GET'])
def get_schedule_by_id(id):
    schedule = ScheduleModel.query.get(id)
    return jsonify(schedule.to_json())


@schedules_blueprint.route('/schedules/<int:id>', methods=['PUT'])
def update_schedule_by_id(id):
    data = request.get_json()
    schedule = ScheduleModel.query.get(id)
    schedule.drone_id = data['drone_id']
    schedule.flight_time = data['flight_time']
    schedule.field_id = data['field_id']
    db.session.commit()
    return jsonify(schedule.to_json())

@schedules_blueprint.route('/schedules/<int:id>', methods=['DELETE'])
def delete_schedule_by_id(id):
    schedule = ScheduleModel.query.get(id)
    db.session.delete(schedule)
    db.session.commit()
    return jsonify({'message': 'Schedule has been deleted'})