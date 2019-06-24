import pandas as pd
from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)
