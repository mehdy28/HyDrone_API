from db import db 


class AnalysisModel(db.Model):
    __tablename__ = 'analysis'

    id = db.Column(db.Integer, primary_key=True)
    crop_stress = db.Column(db.Integer)
    disease = db.Column(db.String)
    pests = db.Column(db.String)

