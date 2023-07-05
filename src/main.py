from flask import Flask
from flask import Response
from bimmer_connected.account import MyBMWAccount
from bimmer_connected.api.regions import Regions
import jsonpickle
import os

app = Flask(__name__)

# DEBUG: flask --app main.py --debug run --host=0.0.0.0

@app.route('/')
async def index():
  account = MyBMWAccount(os.getenv('EMAIL'), os.getenv('PASSWORD'), Regions.REST_OF_WORLD)
  await account.get_vehicles()

  car = account.get_vehicle(os.getenv('VIN'))
  json = jsonpickle.encode(car.data, unpicklable=False)
  return Response(json, mimetype='application/json')

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)