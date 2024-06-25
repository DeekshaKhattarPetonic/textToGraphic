"""
    This script contains multiple trials of image specs
    modification endpoint (mostly) using PIL library.

    None of the trials could change the color depth and resolution.
    The latest trials (older ones to the bottom of script, latest
    on top) could change the aspect ratio and DPI only.
"""

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

        # Check if aspect ratio needs adjustment
        aspect_width, aspect_height = map(int, input_json.image_aspect_ratio.split(':'))
        expected_aspect_ratio = aspect_width / aspect_height
        
        # Check if the resolution needs adjustment
        target_width, target_height = map(int, input_json.image_resolution.split('x'))

        # Create a modified copy of the image with specified properties
        modified_img = img.copy()

        # Change color depth if needed - convert to the desired mode
        if input_json.image_color_depth != original_color_depth:
            modified_img = modified_img.convert(input_json.image_color_depth)

        # Adjust resolution and aspect ratio if needed
        if original_width / original_height != expected_aspect_ratio:
            new_width = target_width
            new_height = int(target_width / expected_aspect_ratio)
            
            if new_height > target_height:
                new_height = target_height
                new_width = int(target_height * expected_aspect_ratio)
            
            modified_img = modified_img.resize((new_width, new_height), Image.LANCZOS)
        else:
            modified_img = modified_img.resize((target_width, target_height), Image.LANCZOS)

        # Save the image with the specified DPI
        modified_image_path = os.path.join(os.path.dirname(image_path), "modified_" + os.path.basename(image_path))
        modified_img.save(modified_image_path, dpi=(input_json.image_dpi, input_json.image_dpi))

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

        # Check if aspect ratio needs adjustment
        aspect_width, aspect_height = map(int, input_json.image_aspect_ratio.split(':'))
        expected_aspect_ratio = aspect_width / aspect_height
        
        # Check if the resolution needs adjustment
        target_width, target_height = map(int, input_json.image_resolution.split('x'))

        # Create a modified copy of the image with specified properties
        modified_img = img.copy()

        # Change color depth if needed - convert to the desired mode
        if input_json.image_color_depth != original_color_depth:
            modified_img = modified_img.convert(input_json.image_color_depth)

        # Adjust resolution and aspect ratio if needed
        if not (original_width == target_width and original_height == target_height):
            # Calculate the target height while preserving the aspect ratio
            if original_width / original_height != expected_aspect_ratio:
                target_height = int(target_width / expected_aspect_ratio)
            modified_img = modified_img.resize((target_width, target_height), Image.LANCZOS)

        # Save the image with the specified DPI
        modified_image_path = os.path.join(os.path.dirname(image_path), "modified_" + os.path.basename(image_path))
        modified_img.save(modified_image_path, dpi=(input_json.image_dpi, input_json.image_dpi))

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
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
"""
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

        # Check if aspect ratio needs adjustment
        aspect_width, aspect_height = map(int, input_json.image_aspect_ratio.split(':'))
        expected_aspect_ratio = aspect_width / aspect_height
        
        # Check if the resolution needs adjustment
        target_width, target_height = map(int, input_json.image_resolution.split('x'))

        # Create a modified copy of the image with specified properties
        modified_img = img.copy()

        # Change color depth if needed - convert to the desired mode
        if input_json.image_color_depth != original_color_depth:
            modified_img = modified_img.convert(input_json.image_color_depth)

        # Adjust resolution and aspect ratio if needed
        if not (original_width == target_width and original_height == target_height):
            if original_width / original_height != expected_aspect_ratio:
                modified_img = modified_img.resize((target_width, target_height), Image.LANCZOS)
            else:
                modified_img = modified_img.resize((target_width, target_height), Image.LANCZOS)

        # Save the image with specified DPI
        modified_image_path = os.path.join(os.path.dirname(image_path), "modified_" + os.path.basename(image_path))
        modified_img.save(modified_image_path, dpi=(input_json.image_dpi, input_json.image_dpi))

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
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
"""
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

        # Check if aspect ratio needs adjustment
        aspect_width, aspect_height = map(int, input_json.image_aspect_ratio.split(':'))
        aspect_ratio_correct = (original_width / original_height) == (aspect_width / aspect_height)

        # Check if the resolution needs adjustment
        target_width, target_height = map(int, input_json.image_resolution.split('x'))
        resolution_correct = (original_width == target_width) and (original_height == target_height)

        # Check if color depth needs adjustment
        color_depth_correct = input_json.image_color_depth == original_color_depth

        # Check if DPI needs adjustment
        dpi_correct = input_json.image_dpi == original_dpi

        # Determine if any modifications are needed
        if not (aspect_ratio_correct and resolution_correct and color_depth_correct and dpi_correct):
            # Create a modified copy of the image with specified properties
            modified_img = img.copy()

            # Change color depth if needed
            if input_json.image_color_depth != original_color_depth:
                modified_img = modified_img.convert(input_json.image_color_depth)

            # Resize to specified resolution and adjust aspect ratio if needed
            if not (resolution_correct and aspect_ratio_correct):
                modified_img = modified_img.resize((target_width, target_height), Image.LANCZOS)

            # Save the image with specified DPI
            modified_image_path = os.path.join(os.path.dirname(image_path), "modified_" + os.path.basename(image_path))
            modified_img.save(modified_image_path, dpi=(input_json.image_dpi, input_json.image_dpi))
            
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
"""
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
"""
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
        new_width, new_height = map(int, input_json.image_resolution.split('x'))
        aspect_ratio_correct = (original_width / original_height) == (new_width / new_height)
        dpi_correct = input_json.image_dpi == original_dpi
        color_depth_correct = input_json.image_color_depth == original_color_depth

        if not (aspect_ratio_correct and dpi_correct and color_depth_correct):
            # Create a modified copy of the image with specified properties
            modified_img = img.copy()

            # Change color depth if needed
            if input_json.image_color_depth != original_color_depth:
                modified_img = modified_img.convert(input_json.image_color_depth)

            # Resize to specified resolution
            if new_width != original_width or new_height != original_height:
                modified_img = modified_img.resize((new_width, new_height))

            # Save the image with specified DPI
            modified_image_path = os.path.join(os.path.dirname(image_path), "modified_" + os.path.basename(image_path))
            modified_img.save(modified_image_path, dpi=(input_json.image_dpi, input_json.image_dpi))
            
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
"""
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
"""
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

        # Calculate new width and height to match the aspect ratio
        aspect_ratio = tuple(map(int, input_json.image_aspect_ratio.split(':')))
        new_width, new_height = aspect_ratio
        if new_width * original_height != new_height * original_width:
            new_height = int(original_height * (new_width / original_width))
            new_width = int(original_width * (new_height / original_height))
        
        # Check image properties against input JSON
        if (
            input_json.image_aspect_ratio != f"{new_width}:{new_height}" or
            input_json.image_dpi != original_dpi or
            input_json.image_color_depth != original_color_depth or
            input_json.image_resolution != f"{original_width}x{original_height}"
        ):
            # Create a modified copy of the image with specified properties
            modified_img = img.copy()

            # Change color depth
            if input_json.image_color_depth != original_color_depth:
                modified_img = modified_img.convert(input_json.image_color_depth)

            # Resize to specified resolution
            target_width, target_height = map(int, input_json.image_resolution.split('x'))
            if target_width != original_width or target_height != original_height:
                modified_img = modified_img.resize((target_width, target_height))

            # Save the image with specified DPI
            modified_image_path = os.path.join(os.path.dirname(image_path), "modified_" + os.path.basename(image_path))
            modified_img.save(modified_image_path, dpi=(input_json.image_dpi, input_json.image_dpi))
            
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
"""
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################
"""
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
"""
