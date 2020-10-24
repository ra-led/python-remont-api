from flask import request, render_template
from app import app


@app.route('/demo_url', methods=['POST'])
def demo_url():
    params = request.form.to_dict()
    
    prediction = app.config['model'].predict(url=params['url'])
    
    return render_template(
        'demo_url.html',
        url=params['url'],
        pred=prediction
    )
