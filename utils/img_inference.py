import io
import torch
import requests

import torchvision.transforms as transforms
from PIL import Image


class Inference():
    def transform_image(self, image_bytes):
        my_transforms = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        image = Image.open(io.BytesIO(image_bytes))
        return my_transforms(image).unsqueeze(0)
    
    
    def predict(url):
        # url = 'https://cdn-p.cian.site/images/8/513/557/kvartira-moskva-ulica-trehgornyy-val-755315843-4.jpg'
    #    with open(url, 'rb') as f:
    #        image_bytes = f.read()
    #        tensor = transform_image(image_bytes=image_bytes)
    #        print('SHAPE', tensor.shape)
            
        r = requests.get(url, timeout=4.0)
        if r.status_code != requests.codes.ok:
            assert False, 'Status code error: {}.'.format(r.status_code)
    
        with Image.open(r.content) as im:
            
            tensor = transform_image(self, image_bytes=im)
        
        with torch.no_grad():
            outputs = app.config['model'](tensor)
            _, preds = torch.max(outputs, 1)
            
        class_name = app.config['labels'][preds.item()]
        