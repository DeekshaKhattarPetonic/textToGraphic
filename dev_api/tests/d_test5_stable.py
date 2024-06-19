import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()


class ImageGenerateRequest(BaseModel):
    prompt: str
    n: int

@app.post("/generate-images/")
def generate_images(payload: ImageGenerateRequest):
    prompt = payload.prompt
    n = payload.n

    try:
        response = client.images.generate(prompt=prompt,
        n=n,
        size="1024x1024")
        """
        # Check response data type and handle accordingly
        if isinstance(response['data'], list):
            # Extract URLs from list of dictionaries
            image_urls = [image['url'] for image in response['data']]
        else:
            # Handle unexpected response format (raise error or return empty list)
            raise Exception("Unexpected response format from OpenAI API")
        return {"image_urls": image_urls}"""
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating images: {str(e)}")

# Run the FastAPI server if this script is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
