from db import db


# irrigation.py
class IrrigationModel(db.Model):
    __tablename__ = 'irrigation'

    id = db.Column(db.Integer, primary_key=True)
    water_level = db.Column(db.Integer)
    irrigation_pattern = db.Column(db.String)

class IrrigationSystemModel(db.Model):
    __tablename__ = 'irrigation_systems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    status = db.Column(db.String)
    status_updated_at = db.Column(db.DateTime)
    irrigation_id = db.Column(db.Integer, db.ForeignKey('irrigation.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class IrrigationScheduleModel(db.Model):
    __tablename__ = 'irrigation_schedules'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    water_amount = db.Column(db.String)
    irrigation_system_id = db.Column(db.Integer, db.ForeignKey('irrigation_systems.id'))
