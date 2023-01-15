from db import db

class WeatherModel(db.Model):
    __tablename__ = 'weather'

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer)
    precipitation = db.Column(db.Integer)
    forecast = db.Column(db.String)
