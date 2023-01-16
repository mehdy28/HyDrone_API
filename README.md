# HyDrone_API
HyDrone_API is a RESTful API that allows you to control and monitor a drone using a simple HTTP interface.

# Installation
To install HyDrone_API, you will need to have Python 3.6 or later and pip installed on your system. Then, you can simply run the following command to install the required dependencies:
pip install -r requirements.txt

## Usage
To start the API, simply run the following command:
python app.py

This will start the API on port 8000 by default. You can change the port by passing a --port argument.

## The API has the following endpoints:

GET /status: Retrieves the current status of the drone, including battery level and GPS coordinates.
POST /takeoff: Makes the drone take off.
POST /land: Makes the drone land.
POST /move: Makes the drone move to a specific GPS coordinate.
# Examples
# Retrieve the current status of the drone
curl http://localhost:8000/status

# Make the drone take off
curl -X POST http://localhost:8000/takeoff

# Make the drone move to a specific GPS coordinate
curl -X POST http://localhost:8000/move -d '{"latitude": 37.788022, "longitude": -122.399797}'

# Make the drone land
curl -X POST http://localhost:8000/land
# Contribution
Feel free to contribute to this project by submitting pull requests or by reporting issues.

# License
HyDrone_API is released under the MIT license.

# Author
HyDrone_API is developed by Mehdy28.



