from flask import  request, jsonify
from db import db
from models.irrigation import IrrigationModel,IrrigationScheduleModel,IrrigationSystemModel
from schemas.schemas import IrrigationScheduleSchema,IrrigationSchema,IrrigationSystemSchema
import datetime
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("irrigation", __name__, description="Opertations on irrigation")


@blp.route('/irrigation', methods=['GET'])
def get_irrigation():
    irrigation = IrrigationModel.query.all()
    return jsonify([irrigation.to_json() for irrigation in irrigation])

@blp.route('/irrigation', methods=['POST'])
def create_irrigation():
    data = request.get_json()
    new_irrigation = IrrigationModel(
        water_level=data['water_level'],
        irrigation_pattern=data['irrigation_pattern'],
        field_id=data['field_id']
    )
    db.session.add(new_irrigation)
    db.session.commit()
    return jsonify(new_irrigation.to_json())

@blp.route('/irrigation/<int:id>', methods=['GET'])
def get_irrigation_by_id(id):
    irrigation = IrrigationModel.query.get(id)
    return jsonify(irrigation.to_json())

@blp.route('/irrigation/<int:id>', methods=['PUT'])
def update_irrigation_by_id(id):
    data = request.get_json()
    irrigation = IrrigationModel.query.get(id)
    irrigation.water_level = data['water_level']
    irrigation.irrigation_pattern = data['irrigation_pattern']
    irrigation.field_id = data['field_id']
    db.session.commit()
    return jsonify(irrigation.to_json())

@blp.route('/irrigation/<int:id>', methods=['DELETE'])
def delete_irrigation_by_id(id):
    irrigation = IrrigationModel.query.get(id)
    db.session.delete(irrigation)
    db.session.commit()
    return jsonify({'message': 'Irrigation has been deleted'})


@blp.route('/irrigation_systems', methods=['GET'])
def get_irrigation_systems():
    irrigation_systems = IrrigationSystemModel.query.all()
    return jsonify([irrigation_system.to_json() for irrigation_system in irrigation_systems])

@blp.route('/irrigation_systems', methods=['POST'])
def create_irrigation_system():
    data = request.get_json()
    new_irrigation_system = IrrigationSystemModel(
        name=data['name'],
        location=data['location'],
        status=data['status'],
        status_updated_at=datetime.datetime.now()
    )
    db.session.add(new_irrigation_system)
    db.session.commit()
    return jsonify(new_irrigation_system.to_json())

@blp.route('/irrigation_systems/<int:id>', methods=['GET'])
def get_irrigation_system_by_id(id):
    irrigation_system = IrrigationSystemModel.query.get(id)
    return jsonify(irrigation_system.to_json())

@blp.route('/irrigation_systems/<int:id>', methods=['PUT'])
def update_irrigation_system_by_id(id):
    data = request.get_json()
    irrigation_system = IrrigationSystemModel.query.get(id)
    irrigation_system.name = data['name']
    irrigation_system.location = data['location']
    irrigation_system.status = data['status']
    irrigation_system.status_updated_at = datetime.datetime.now()
    db.session.commit()
    return jsonify(irrigation_system.to_json())

@blp.route('/irrigation_systems/<int:id>', methods=['DELETE'])
def delete_irrigation_system_by_id(id):
    irrigation_system = IrrigationSystemModel.query.get(id)
    db.session.delete(irrigation_system)
    db.session.commit()
    return jsonify({'message': 'Irrigation system has been deleted'})

@blp.route('/irrigation_schedules', methods=['GET'])
def get_irrigation_schedules():
    irrigation_schedules = IrrigationScheduleModel.query.all()
    return jsonify([irrigation_schedule.to_json() for irrigation_schedule in irrigation_schedules])


    
@blp.route('/irrigation_schedules', methods=['POST'])
def create_irrigation_schedule():
    data = request.get_json()
    new_irrigation_schedule = IrrigationScheduleModel(
        irrigation_system_id=data['irrigation_system_id'],
        start_time=data['start_time'],
        end_time=data['end_time'],
        repeat=data['repeat'],
        interval=data['interval'],
        field_id=data['field_id']
    )
    db.session.add(new_irrigation_schedule)
    db.session.commit()
    return jsonify(new_irrigation_schedule.to_json())

@blp.route('/irrigation_schedules/<int:id>', methods=['GET'])
def get_irrigation_schedule_by_id(id):
    irrigation_schedule = IrrigationScheduleModel.query.get(id)
    return jsonify(irrigation_schedule.to_json())

@blp.route('/irrigation_schedules/<int:id>', methods=['PUT'])
def update_irrigation_schedule_by_id(id):
    data = request.get_json()
    irrigation_schedule = IrrigationScheduleModel.query.get(id)
    irrigation_schedule.irrigation_system_id = data['irrigation_system_id']
    irrigation_schedule.start_time = data['start_time']
    irrigation_schedule.end_time = data['end_time']
    irrigation_schedule.repeat = data['repeat']
    irrigation_schedule.interval = data['interval']
    irrigation_schedule.field_id = data['field_id']
    db.session.commit()
    return jsonify(irrigation_schedule.to_json())



@blp.route('/irrigation_schedules/<int:id>', methods=['DELETE'])
def delete_irrigation_schedule_by_id(id):
    irrigation_schedule = IrrigationScheduleModel.query.get(id)
    db.session.delete(irrigation_schedule)
    db.session.commit()
    return jsonify({'message': 'Irrigation schedule has been deleted'})

