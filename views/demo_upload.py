from flask import request, render_template
from app import app
from base64 import b64encode


@app.route('/demo_upload', methods=['POST'])
def demo_upload():
    file = request.files["file"]
    file_bytes = file.read()
    
    prediction = app.config['model'].predict(file_bytes=file_bytes)
    
    image = b64encode(file_bytes).decode("utf-8")
    
    return render_template(
        'demo_upload.html',
        image=image,
        pred=prediction
    )
