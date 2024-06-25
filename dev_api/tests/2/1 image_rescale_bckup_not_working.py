from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from PIL import Image
import os

app = FastAPI()

class ImageSpecifications(BaseModel):
    image_aspect_ratio: str
    image_dpi: int
    image_color_depth: str
    image_resolution: str

def modify_image_properties(input_json: ImageSpecifications, image_path: str):
    with Image.open(image_path) as img:
        # Get original image properties
        original_width, original_height = img.size
        original_dpi = img.info.get('dpi', (72, 72))[0]  # Default to 72 if DPI info is not available
        original_color_depth = img.mode

        # Check image properties against input JSON
        if (
            input_json.image_aspect_ratio != f"{original_width}:{original_height}" or
            input_json.image_dpi != original_dpi or
            input_json.image_color_depth != original_color_depth or
            input_json.image_resolution != f"{original_width}x{original_height}"
        ):
            # Create a modified copy of the image with specified properties
            modified_img = img.copy()
            modified_img = modified_img.convert(input_json.image_color_depth)  # Convert color depth
            modified_img = modified_img.resize((int(input_json.image_resolution.split('x')[0]), int(input_json.image_resolution.split('x')[1])))  # Resize to specified resolution
            
            modified_image_path = 'modified_image.jpg'
            modified_img.save(modified_image_path)  # Save the modified image
            
            return modified_image_path
        else:
            return None  # No modifications needed

@app.post("/uploadfile/")
async def upload_file(input_json: ImageSpecifications, file: UploadFile = File(...)):
    try:
        file_location = f"temp_{file.filename}"
        
        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
        
        modified_image_path = modify_image_properties(input_json, file_location)

        os.remove(file_location)  # Clean up the uploaded file
        
        if modified_image_path:
            return FileResponse(modified_image_path, filename="modified_image.jpg")
        else:
            return {"message": "Image properties match the specifications."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
