from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method =='POST':
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        predicted_price = util.get_estimated_price(location,total_sqft,bhk,bath)
        
    return render_template('index.html', predicted_price = predicted_price)
    # response = jsonify({  
    #     'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    # })
    # response.headers.add('Access-Control-Allow-Origin', '*')

    # return response




if __name__ == '__main__':
	print("Server starting ..")
	util.load_saved_artifacts()
	app.run()