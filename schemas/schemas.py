from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    public_id = fields.String()
    name = fields.String()
    email = fields.String()
    password = fields.String()
    admin = fields.Boolean()

class WeatherSchema(Schema):
    id = fields.Integer()
    temperature = fields.Integer()
    precipitation = fields.Integer()
    forecast = fields.String()

class IrrigationSchema(Schema):
    id = fields.Integer()
    water_level = fields.Integer()
    irrigation_pattern = fields.String()

class IrrigationSystemSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    location = fields.String()
    status = fields.String()
    status_updated_at = fields.DateTime()
    irrigation_id = fields.Integer()
    user_id = fields.Integer()

class IrrigationScheduleSchema(Schema):
    id = fields.Integer()
    start_time = fields.DateTime()
    end_time = fields.DateTime()
    water_amount = fields.String()
    irrigation_system_id = fields.Integer()

class AnalysisSchema(Schema):
    id = fields.Integer()
    crop_stress = fields.Integer()
    disease = fields.String()
    pests = fields.String()

class AlertSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    message = fields.String()
    timestamp = fields.String()

class FieldSchema(Schema):
    id = fields.Integer()
    size = fields.Integer()
    type = fields.String()
    location = fields.String()
    name = fields.String()
    user_id = fields.Integer()
    irrigation_system_id = fields.Integer()
    analysis_id = fields.Integer()
    drone_id = fields.Integer()

class DroneSchema(Schema):
    id = fields.Integer()
    type = fields.String()
    serial_number = fields.String()
    location = fields.String()
    status = fields.String()
    user_id = fields.Integer()

class ScheduleSchema(Schema):
    id = fields.Integer()
    flight_time = fields.String()
    drone_id = fields.Integer()
    field_id = fields.Integer()

