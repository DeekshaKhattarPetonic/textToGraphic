import os
import requests
from dotenv import load_dotenv
import json
from fastapi import FastAPI, HTTPException, Query
import requests
from openai import OpenAI

client = OpenAI()                  
from dotenv import load_dotenv
from pydantic import BaseModel  # Import BaseModel for defining Pydantic models

app = FastAPI()

class ImageGenerateRequest(BaseModel):
    prompt: str
    n: int

dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path)


import os

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")


@app.post("/generate-images-2/")
def test_openai_api(payload: ImageGenerateRequest):
    req_body = vars(payload)
    prompt = req_body['prompt']
    n = req_body['n']
    api_key = os.getenv("OPENAI_API_KEY")
    print (api_key)

    # Define the API endpoint
    api_endpoint = 'https://api.openai.com/v1/images/generations'

    # Headers for the API request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }


    # Data for the API request
    data = {
        'prompt': prompt,
        'n': n,  # Number of images to generate
        'size': '1024x1024'
    }

    response = client.images.generate(**data)

    return response

if __name__ == "__main__":
    prompt = (
        'A luxurious contemporary living room with large windows overlooking a garden. '
        'Do not give random or giberrish objects '
        'A sleek glass coffee table, a marble fireplace with an abstract painting, and a black entertainment system with a flat-screen TV. '
        'A bar area with a black countertop and white stools, and soft ambient lighting with recessed lights and floor lamps.'
    )
    test_openai_api(prompt)