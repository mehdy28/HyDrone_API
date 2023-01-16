from flask import  request, jsonify
from db import db
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.weather import WeatherModel
from schemas.schemas import WeatherSchema

blp = Blueprint("weather", __name__, description="Operations on weather")

@blp.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'GET':
        weathers = WeatherModel.query.all()
        return jsonify([weather.to_dict() for weather in weathers])
    if request.method == 'POST':
        data = request.get_json()
        weather = WeatherModel(temperature=data['temperature'], precipitation=data['precipitation'], forecast=data['forecast'])
        db.session.add(weather)
        db.session.commit()
        return jsonify(weather.to_dict()), 201

@blp.route('/weather/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def weather_by_id(id):
    weather = WeatherModel.query.get(id)
    if request.method == 'GET':
        return jsonify(weather.to_dict())
    if request.method == 'PUT':
        data = request.get_json()
        weather.temperature = data['temperature']
        weather.precipitation = data['precipitation']
        weather.forecast = data['forecast']
        db.session.commit()
        return jsonify(weather.to_dict())
    if request.method == 'DELETE':
        db.session.delete(weather)
        db.session.commit()
        return '', 204
