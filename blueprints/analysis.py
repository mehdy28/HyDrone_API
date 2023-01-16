from flask import  request, jsonify
from db import db
from models.analysis import AnalysisModel
from schemas.schemas import AnalysisSchema
from flask_smorest import Blueprint, abort

blp = Blueprint("analysis", __name__, description="Opertations on analysis")


@blp.route('/analysis', methods=['GET'])
def get_analysis():
    analysis = AnalysisModel.query.all()
    return jsonify([analysis.to_json() for analysis in analysis])

@blp.route('/analysis', methods=['POST'])
def create_analysis():
    data = request.get_json()
    new_analysis = AnalysisModel(
        crop_stress=data['crop_stress'],
        disease=data['disease'],
        pests=data['pests'],
        field_id=data['field_id']
    )
    db.session.add(new_analysis)
    db.session.commit()
    return jsonify(new_analysis.to_json())

@blp.route('/analysis/<int:id>', methods=['GET'])
def get_analysis_by_id(id):
    analysis = AnalysisModel.query.get(id)
    return jsonify(analysis.to_json())

@blp.route('/analysis/<int:id>', methods=['PUT'])
def update_analysis_by_id(id):
    data = request.get_json()
    analysis = AnalysisModel.query.get(id)
    analysis.crop_stress = data['crop_stress']
    analysis.disease = data['disease']
    analysis.pests = data['pests']
    analysis.field_id = data['field_id']
    db.session.commit()
    return jsonify(analysis.to_json())

@blp.route('/analysis/<int:id>', methods=['DELETE'])
def delete_analysis_by_id(id):
    analysis = AnalysisModel.query.get(id)
    db.session.delete(analysis)
    db.session.commit()
    return jsonify({'message': 'Analysis has been deleted'})
