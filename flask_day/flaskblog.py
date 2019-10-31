import pickle
import pandas as pd
# import the nessecary pieces from Flask
from flask import Flask, render_template, request, jsonify, Response, url_for

# create the app object that will route our calls
app = Flask(__name__)

# BLOG PART
@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# LINEAR REGRESSION PART
@app.route('/mpg', methods = ['GET'])
def mpg():
    '''http://0.0.0.0:3333/mpg'''
    return render_template('mpg.html')

model = pickle.load(open('linreg.p','rb'))

@app.route('/inference',  methods = ['POST'])
def inference():
    req = request.get_json()
    print(req)
    c,h,w = req['cylinders'],req['horsepower'],req['weight']
    prediction = list(model.predict([[c,h,w]]))
    return jsonify({'c':c,'h': h,'w':w,'prediction':prediction[0] })

@app.route('/plot',  methods = ['GET'])
def plot():
    df = pd.read_csv('cars.csv')
    data = list(zip(df.mpg,df.weight))
    return jsonify(data)

# when run from command line, start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)
