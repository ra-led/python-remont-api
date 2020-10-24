import json
from flask import request, render_template
from app import app
from base64 import b64encode


@app.route('/predict_class', methods=['POST'])
def predict_class():
    file = request.files["file"]
    file_bytes = file.read()
    
    prediction = app.config['model'].predict(file_bytes=file_bytes)
    
    return json.dumps({'predicted': prediction})
