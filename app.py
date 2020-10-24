#!/usr/bin/env python3
from flask import Flask, render_template
import numpy as np
import torch
from utils.img_inference import Inference


app = Flask(__name__)
app.config['inference'] = Inference = 

from views import demo

@app.route('/')
def index():
    return render_template('index.html')
