# app.py
from flask import Flask
from hello import hello_world

app = Flask(__name__)

@app.route('/')
def index():
    return hello_world()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
