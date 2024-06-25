import os
import json
from typing import Optional
from fastapi import FastAPI, HTTPException, Query
import requests
from dotenv import load_dotenv
from pydantic import BaseModel  # Import BaseModel for defining Pydantic models

app = FastAPI()

# Load environment variables
dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path)

# Get the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise EnvironmentError("API key not found in environment variables.")

# Define the API endpoint
api_endpoint = 'https://api.openai.com/v1/images/generations'

# Headers for the API request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Define request body data model
class ImageGenerationRequest:
    prompt: str
    n: int
    size: str

# Define response model
class ImageGenerationResponse(BaseModel):
    image_url: str
    response_data: dict

# FastAPI endpoint to generate images
@app.post("/generate-images/", response_model=ImageGenerationResponse)
async def generate_images(request_body: ImageGenerationRequest):
    data = {
        'prompt': request_body.prompt,
        'n': request_body.n,
        'size': request_body.size
    }

    try:
        # Make the API request
        response = requests.post(api_endpoint, headers=headers, json=data)
        response.raise_for_status()
        response_data = response.json()
        image_url = response_data['data'][0]['url']
        return {"image_url": image_url, "response_data": response_data}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error calling OpenAI API: {str(e)}")

    except (KeyError, IndexError) as e:
        raise HTTPException(status_code=500, detail=f"Error parsing OpenAI response: {str(e)}")

# Optional: Run the FastAPI application with Uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
