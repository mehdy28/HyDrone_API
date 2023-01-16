from flask import Flask
from flask_smorest import Api
from db import db
from blueprints.users import blp as UsersBlueprint
from blueprints.weather import blp as WeatherBleuprint
from blueprints.alerts import blp as AlertBleuprint
from blueprints.analysis import blp as AnalysisBlueprint
from blueprints.drones import blp as DronesBlueprint 
from blueprints.fields import blp as FieldsBlueprint
from blueprints.irrigation import blp as  IrrigationBlueprint
from blueprints.login import blp as LoginBlueprint
from blueprints.register import blp as RegisterBlueprint

app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


app.config["API_TITLE"] = "HyDrone REST API"
app.config["API_VERSION"] = "v1.0.0"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Create the database tables
@app.before_first_request
def create_tables():
    with app.app_context():
        db.create_all()
  
api = Api(app)
api.register_blueprint(RegisterBlueprint)
api.register_blueprint(LoginBlueprint)
api.register_blueprint(UsersBlueprint)
api.register_blueprint(WeatherBleuprint)
api.register_blueprint(AlertBleuprint)
api.register_blueprint(AnalysisBlueprint)
api.register_blueprint(DronesBlueprint)
api.register_blueprint(FieldsBlueprint)
api.register_blueprint(IrrigationBlueprint)


if __name__ == '__main__':
    app.run(debug=True)

