import pickle
import pandas as pd
from flask import Flask, render_template, request, jsonify, Response

# app object to route calls
app = Flask( __name__ )
# home route
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')  # '<p> Hello. </p>'

# real_estate route
@app.route('/real_estate', methods=['GET'])
def real_estate():
    return render_template('real_estate.html')

# data science route
@app.route('/ds' , methods=['GET'])
def ds():
    return render_template('ds.html')

# media & production route
@app.route('/media', methods=['GET'])
def media():
    return render_template('media.html')

'''unsure below'''
# mpg route
@app.route('/mpg', methods = ['GET'])
def mpg():
    return render_template('mpg.html')
# load model
model = pickle.load(open('linreg.p', 'rb'))
# inference route
@app.route('/inference',methods= ['POST'])
def inference():
    req = request.get_json()
    print(req)
    c,h,w = req['cylinders'], req['horsepower'], req['weight']
    prediction = list(model.predict([[c,h,w]]))
    return jsonify({'c':c, 'h':h, 'w':w, 'prediction':prediction[0]})
# scatter plot
@app.route('/plot', methods=['GET'])
def plot():
    df = pd.read_csv('cars.csv')
    data = list(zip(df.mpg , df.weight))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)
