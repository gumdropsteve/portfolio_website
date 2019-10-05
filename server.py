from flask import Flask, render_template

# app object to route calls
app = Flask(__name__)

# home route
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  


# data science route
@app.route('/ds' , methods=['GET'])
def ds():
    return render_template('ds.html')


# writing route
@app.route('/writing', methods=['GET'])
def media():
    return render_template('writing.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)
