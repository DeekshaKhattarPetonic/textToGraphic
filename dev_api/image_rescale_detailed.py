from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from PIL import Image
import os

app = FastAPI()

class ImageSpecifications(BaseModel):
    image_aspect_ratio: str
    image_dpi: int
    image_color_depth: str
    image_resolution: str
    image_path: str

def modify_image_properties(input_json: ImageSpecifications):
    image_path = input_json.image_path
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
            
            modified_image_path = os.path.join(os.path.dirname(image_path), "modified_" + os.path.basename(image_path))
            modified_img.save(modified_image_path)  # Save the modified image
            
            return modified_image_path
        else:
            return None  # No modifications needed

@app.post("/process_image/")
async def process_image(input_json: ImageSpecifications):
    try:
        if not os.path.isfile(input_json.image_path):
            raise HTTPException(status_code=404, detail="Image file not found")
        
        modified_image_path = modify_image_properties(input_json)

        if modified_image_path:
            return {"message": "Image modified", "modified_image_path": modified_image_path}
        else:
            return {"message": "Image properties match the specifications."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8011)
