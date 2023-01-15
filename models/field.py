from db import db 

class FieldModel(db.Model):
    __tablename__ = 'fields'

    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer)
    type = db.Column(db.String)
    location = db.Column(db.String)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    irrigation_system_id = db.Column(db.Integer, db.ForeignKey('irrigation_systems.id'))
    analysis_id = db.Column(db.Integer, db.ForeignKey('analysis.id'))
    drone_id = db.Column(db.Integer, db.ForeignKey('drones.id'))

    