from db import db

class DroneModel(db.Model):
    __tablename__ = 'drones'    
    
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    serial_number = db.Column(db.String)
    location = db.Column(db.String)
    status = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=False, nullable=False)
    
    
class ScheduleModel(db.Model):
    __tablename__ = 'schedules'
    id = db.Column(db.Integer, primary_key=True)
    flight_time = db.Column(db.String)
    drone_id = db.Column(db.Integer, db.ForeignKey('drones.id'))
    field_id = db.Column(db.Integer, db.ForeignKey('fields.id'))
   
