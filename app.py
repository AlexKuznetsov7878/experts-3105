from flask import  Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World!'
@app.route('/hello')
def hello():
    return 'Hello Alex!'
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
