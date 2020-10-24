import io
import torch
import requests

import torchvision.transforms as transforms
from PIL import Image


class Inference():
    def __init__(self, model_path='models/resnet18_baseline_cpu.torch'):
        self.model_path = model_path
        self.model = torch.load(model_path)
        self.labels = ['bez_otdelki', 'luks', 'standart', 'trebuetsya_kosmetika']
        
    def transform_image(self, image_bytes):
        my_transforms = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        image = Image.open(io.BytesIO(image_bytes))
        return my_transforms(image).unsqueeze(0)
    
    
    def predict(self, url=None, file_path=None):
        # если задан url
        if url:
            r = requests.get(url, timeout=4.0)
            if r.status_code != requests.codes.ok:
                assert False, 'Status code error: {}.'.format(r.status_code)
            tensor = self.transform_image(image_bytes=r.content)
        # если задан локальный путь
        elif file_path:
            with open(file_path, 'rb') as f:
                image_bytes = f.read()
                tensor = self.transform_image(image_bytes=image_bytes)
        else:
            assert False, 'Set url or file path'
        
        with torch.no_grad():
            outputs = self.model (tensor)
            _, preds = torch.max(outputs, 1)
            
        return self.labels[preds.item()]
        