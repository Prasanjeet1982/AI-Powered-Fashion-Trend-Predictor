import torch
from transformers import CLIPProcessor, CLIPLMHeadModel
import numpy as np
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16", device=device)
model = CLIPLMHeadModel.from_pretrained("openai/clip-vit-base-patch16", device=device)

def predict_trend(image, caption):
    image_array = np.array(image.resize((224, 224))) / 255.0
    caption = [caption] if caption else [""]
    
    inputs = processor(text=caption, images=[image_array], return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    image_features = outputs.logits_per_image
    text_features = outputs.logits_per_text
    
    combined_features = np.concatenate([image_features.cpu().detach().numpy(), text_features.cpu().detach().numpy()], axis=1)
    predictions = model.predict([combined_features])
    
    predicted_trend = np.argmax(predictions)
    return predicted_trend
