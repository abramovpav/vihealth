from flask import Flask
from flask import render_template
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    print os.path.abspath(os.path.dirname(__file__))
    return render_template('index.html')