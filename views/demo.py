from flask import request, render_template
from app import app
import json


@app.route('/demo', methods=['POST'])
def predict_image():
    params = request.form.to_dict()
    
    return render_template(
        'demo.html',
        url=params['url'],
        pred='Class'
        )
