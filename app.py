# Python application code ::
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a Python Flask application running on EC2."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
