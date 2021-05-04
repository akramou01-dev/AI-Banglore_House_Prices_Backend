from flask import Flask, request, jsonify
from flask_cors import CORS
import utils
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def test():
    return "<h3>hey from the home page</h3>"


@app.route("/locations", methods=["GET"])
def get_locations():
    response = jsonify({
        "locations": utils.get_locations()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/predict_price", methods=["POST"])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])
    location = request.form["location"]

    response = jsonify({
        "estimated_price": utils.get_estimated_price(location, total_sqft, bath, bhk)
    })
    return response


if __name__ == "__main__":
    print("The server is starting...")
    utils.load_saved_artifacts()
    app.run()
