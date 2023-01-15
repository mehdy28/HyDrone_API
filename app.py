from flask import Flask
from db import db
from blueprints.users import user_blueprint
from blueprints.weather import weather_bp
from blueprints.alerts import alert_blueprint
from blueprints.analysis import analysis_blueprint
from blueprints.drones import drones_blueprint , schedules_blueprint
from blueprints.fields import fields_blueprint
from blueprints.irrigation import irrigation_blueprint
from blueprints.login import login_bp
app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(weather_bp)
app.register_blueprint(alert_blueprint)
app.register_blueprint(analysis_blueprint)
app.register_blueprint(drones_blueprint)
app.register_blueprint(schedules_blueprint)
app.register_blueprint(fields_blueprint)
app.register_blueprint(irrigation_blueprint)
app.register_blueprint(login_bp)




# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create the database tables
@app.before_first_request
def create_tables():
    with app.app_context():
        db.create_all()
    

if __name__ == '__main__':
    app.run(debug=True)

