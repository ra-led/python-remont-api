#!/usr/bin/env python3
from flask import Flask, render_template
from utils.img_inference import Inference


app = Flask(__name__)

app.config['model'] = Inference()

from views import demo_url, demo_upload

@app.route('/')
def index():
    return render_template('index.html')
