from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'location': util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods = ['POST'])
def predict_home_price():
    location = request.form['location']
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    bhk = int(request.form['bhk'])
    

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, balcony, bhk)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting python flask server for home price prediction:")
    app.run()
