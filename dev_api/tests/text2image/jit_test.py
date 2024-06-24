import os
import requests
from dotenv import load_dotenv



# Your API key
# CAUTION : the python script and .env file need
# to be in the same path for below line.
dotenv_path = os.path.join(os.getcwd(), ".env")
# below dotenv_path for local test in Downloads folder
# dotenv_path = os.path.join(os.path.expanduser("~"), "Downloads", ".env")
load_dotenv(dotenv_path)


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
    'prompt': 'a painting of a futuristic cityscape',
    'n': 1,  # Number of images to generate
    'size': '1024x1024'  # Size of the generated image
}

# Make the API request
response = requests.post(api_endpoint, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    response_data = response.json()
    image_url = response_data['data'][0]['url']
    print(f'Generated Image URL: {image_url}')
else:
    print(f'Error: {response.status_code}, {response.text}')
