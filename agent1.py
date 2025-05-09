from transformers import pipeline, BlipProcessor, BlipForConditionalGeneration
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import InferenceClient
from PIL import Image
import torch
import os
import requests
import subprocess

# Load BLIP for image captioning
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Generate image caption using BLIP
def get_image_description(image_path):
    image = Image.open(image_path).convert('RGB')
    inputs = blip_processor(image, return_tensors="pt")
    with torch.no_grad():
        output = blip_model.generate(**inputs)
    caption = blip_processor.decode(output[0], skip_special_tokens=True)
    return caption

# Step 2: Ask Ollama for property advice
def ask_ollama(prompt, model="llama3:latest"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        capture_output=True
    )
    return result.stdout.decode("utf-8")

# Step 3: Full pipeline
def get_troubleshooting_suggestion(image_path):
    caption = get_image_description(image_path)
    prompt = (
        f"You are a helpful assistant diagnosing home maintenance issues.\n"
        f"Image Description: \"{caption}\"\n"
        f"Give practical, clear advice to a tenant about what they should do."
    )
    response = ask_ollama(prompt)
    return caption, response

# Combined agent function
def agent1_flow(image_path):
    caption = get_image_description(image_path)
    suggestion = get_troubleshooting_suggestion(image_path)
    return caption, suggestion

