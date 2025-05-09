from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import InferenceClient
import os
import subprocess

def ask_tenancy_faq(question, location=None, model="llama3:latest"):
    prompt = (
        f"You are a legal assistant specializing in tenancy laws in {location}.\n"
        f"Question: {question}\n"
        f"Give a clear, legally accurate, tenant-friendly answer."
    )
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        capture_output=True
    )
    return result.stdout.decode("utf-8")

