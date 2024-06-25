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

# Your API key
# CAUTION : the python script and .env file need
# to be in the same path for below line.
dotenv_path = os.path.join(os.getcwd(), ".env")
# below dotenv_path for local test in Downloads folder
# dotenv_path = os.path.join(os.path.expanduser("~"), "Downloads", ".env")
load_dotenv(dotenv_path)

@app.post("/generate-images/")
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

    # prompt = (
    #     'A luxurious contemporary living room with large windows overlooking a garden. '
    #     'Do not give random or giberrish objects '
    #     'A sleek glass coffee table, a marble fireplace with an abstract painting, and a black entertainment system with a flat-screen TV. '
    #     'A bar area with a black countertop and white stools, and soft ambient lighting with recessed lights and floor lamps.'
    # )

    # Data for the API request
    data = {
        'prompt': prompt,
        'n': n,  # Number of images to generate
        'size': '1024x1024'
    }

    # Make the API request
    response = requests.post(api_endpoint, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        response_data = response.json()
        for i, image_data in enumerate(response_data['data']):
            image_url = image_data['url']
            # print(f'Generated Image URL {i+1}: {image_url}')
            # print("\n\n\n")
        return response_data
    else:
        return f'Error: {response.status_code}, {response.text}'

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

    # prompt = (
    #     'A luxurious contemporary living room with large windows overlooking a garden. '
    #     'Do not give random or giberrish objects '
    #     'A sleek glass coffee table, a marble fireplace with an abstract painting, and a black entertainment system with a flat-screen TV. '
    #     'A bar area with a black countertop and white stools, and soft ambient lighting with recessed lights and floor lamps.'
    # )

    # Data for the API request
    data = {
        'prompt': prompt,
        'n': n,  # Number of images to generate
        'size': '1024x1024'
    }

    # Make the API request
    # response = requests.post(api_endpoint, headers=headers, json=data)
    response = client.images.generate(**data)

    # Check the response
    # if response.status_code == 200:
    #     response_data = response.json()
    #     for i, image_data in enumerate(response_data['data']):
    #         image_url = image_data['url']
            # print(f'Generated Image URL {i+1}: {image_url}')
            # print("\n\n\n")
    return response
    # else:
    #     return f'Error: {response.status_code}, {response.text}'

if __name__ == "__main__": # type: ignore
    prompt = (
        'A luxurious contemporary living room with large windows overlooking a garden. '
        'Do not give random or giberrish objects '
        'A sleek glass coffee table, a marble fireplace with an abstract painting, and a black entertainment system with a flat-screen TV. '
        'A bar area with a black countertop and white stools, and soft ambient lighting with recessed lights and floor lamps.'
    )
    test_openai_api(prompt)