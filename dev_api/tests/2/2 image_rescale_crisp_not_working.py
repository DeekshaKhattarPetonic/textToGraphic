from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from PIL import Image, ImageOps
import os

app = FastAPI()

class ImageSpecs(BaseModel):
    image_path: str
    image_aspect_ratio: str
    image_dpi: int
    image_color_depth: str
    image_resolution: str

@app.post("/process-image")
async def process_image(specs: ImageSpecs):
    image_path = specs.image_path

    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise HTTPException(status_code=404, detail="Image file not found")

    # Open the image
    with Image.open(image_path) as img:
        # Get the image properties
        image_properties = {
            "image_aspect_ratio": f"{img.width}:{img.height}",
            "image_dpi": img.info.get("dpi", (0, 0))[0],  # Assuming DPI is stored in the image metadata
            "image_color_depth": img.mode,
            "image_resolution": f"{img.width}x{img.height}"
        }

        # Compare image properties with the specified specifications
        if image_properties != specs.dict(exclude={"image_path"}):  # Exclude image_path from comparison
            # Modify the image (for demonstration, let's just invert it)
            modified_img = ImageOps.invert(img)
            # Save the modified image in the same directory with a modified filename
            modified_image_path = os.path.join(os.path.dirname(image_path), "modified_" + os.path.basename(image_path))
            modified_img.save(modified_image_path)
            return {"message": "Image modified", "modified_image_path": modified_image_path}
        else:
            return {"message": "Image properties match the specifications"}

# Example usage:
# Assume you have an image file at '/path/to/image.jpg' and JSON data as described
# JSON data should be sent as raw JSON in the request body
# {
#     "image_path": "/path/to/image.jpg",
#     "image_aspect_ratio": "16:9",
#     "image_dpi": 300,
#     "image_color_depth": "RGB",
#     "image_resolution": "1920x1080"
# }
