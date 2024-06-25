"""
    This script contains multiple trials of image specs modification
    endpoint (mostly) using OpenCV library (and PIL library sometimes
    perhaps).

    None of the trials could change the color depth and resolution.
    All the trials (older ones to the bottom of script, latest
    on top) could change the aspect ratio and DPI only.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from PIL import Image
import cv2
import numpy as np
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
    
    # Read image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        raise HTTPException(status_code=404, detail="Image file is corrupted or not supported")

    # Get original image properties
    original_height, original_width = img.shape[:2]

    # Check if aspect ratio needs adjustment
    aspect_width, aspect_height = map(int, input_json.image_aspect_ratio.split(':'))
    expected_aspect_ratio = aspect_width / aspect_height
    
    # Check if the resolution needs adjustment
    target_width, target_height = map(int, input_json.image_resolution.split('x'))

    # Adjust resolution and aspect ratio if needed
    if float(original_width) / original_height != expected_aspect_ratio:
        new_width = target_width
        new_height = int(target_width / expected_aspect_ratio)
        if new_height > target_height:
            new_height = target_height
            new_width = int(target_height * expected_aspect_ratio)
        img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
    else:
        img = cv2.resize(img, (target_width, target_height), interpolation=cv2.INTER_LANCZOS4)

    # Adjust color depth if needed
    if input_json.image_color_depth == "RGB":
        if len(img.shape) != 3 or img.shape[2] != 3:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    elif input_json.image_color_depth == "L":
        if len(img.shape) == 3 and img.shape[2] == 3:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    elif input_json.image_color_depth == "P":
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # OpenCV does not support indexed color directly, so a workaround
    else:
        raise HTTPException(status_code=422, detail="Unsupported color depth")

    # Save the modified image with the specified DPI
    modified_image_path = os.path.join(os.path.dirname(image_path), "modified_" + os.path.basename(image_path))
    cv2.imwrite(modified_image_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])  # Compression is just an example
    
    # Set DPI using PIL (as OpenCV does not directly support setting DPI)
    from PIL import Image as PILImage
    
    pil_img = PILImage.open(modified_image_path)
    pil_img.save(modified_image_path, dpi=(input_json.image_dpi, input_json.image_dpi))

    return modified_image_path

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

########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import cv2
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
    
    # Read image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        raise HTTPException(status_code=404, detail="Image file is corrupted or not supported")

    # Get original image properties
    original_height, original_width = img.shape[:2]

    # Check if aspect ratio needs adjustment
    aspect_width, aspect_height = map(int, input_json.image_aspect_ratio.split(':'))
    expected_aspect_ratio = aspect_width / aspect_height
    
    # Check if the resolution needs adjustment
    target_width, target_height = map(int, input_json.image_resolution.split('x'))

    # Adjust resolution and aspect ratio if needed
    if float(original_width) / original_height != expected_aspect_ratio:
        new_width = target_width
        new_height = int(target_width / expected_aspect_ratio)
        if new_height > target_height:
            new_height = target_height
            new_width = int(target_height * expected_aspect_ratio)
        img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
    else:
        img = cv2.resize(img, (target_width, target_height), interpolation=cv2.INTER_LANCZOS4)

    # Adjust color depth if needed
    if input_json.image_color_depth == "RGB":
        if len(img.shape) != 3 or img.shape[2] != 3:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    elif input_json.image_color_depth == "L":
        if len(img.shape) == 3 and img.shape[2] == 3:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        raise HTTPException(status_code=422, detail="Unsupported color depth")

    # Save the modified image with the specified DPI
    modified_image_path = os.path.join(os.path.dirname(image_path), "modified_" + os.path.basename(image_path))
    cv2.imwrite(modified_image_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])  # Compression is just an example
    
    # Set DPI using PIL (as OpenCV does not directly support setting DPI)
    from PIL import Image as PILImage
    
    pil_img = PILImage.open(modified_image_path)
    pil_img.save(modified_image_path, dpi=(input_json.image_dpi, input_json.image_dpi))

    return modified_image_path

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
"""