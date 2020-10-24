#!/usr/bin/env python3
import os
from flask import Flask, render_template
from utils.img_inference import Inference
from conf import CFG

app = Flask(__name__)

app.config['model'] = Inference(
    labels=CFG['labels'],
    model_path=os.path.join('models', CFG['model_name'])
)

from views import demo_url, demo_upload


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
