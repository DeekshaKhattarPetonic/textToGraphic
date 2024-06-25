"""
    this script hosts data-api routes
    that are written using FASTAPI
"""
import os
import logging
from fastapi import FastAPI, File, UploadFile, Response, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any, List
import shutil
import pydantic_check
from gen_ai import generate_images, optimize_prompt
# from modify_image_properties import modify_image_properties

# Determine the directory for logs
log_directory = os.path.join(os.getcwd(), 'logs')

# Create the logs directory if it doesn't exist
if not os.path.exists(log_directory):
    os.mkdir(log_directory)

# Configure logging
# logging.basicConfig(
#     filename="logs.log"
#     level=logging.DEBUG,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     handlers=[logging.StreamHandler()],
# )

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler for this script's log file
file_handler = logging.FileHandler(os.path.join(log_directory, "data_api.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)



# Create a FastAPI instance
app = FastAPI()

# Allowing all origins for now
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/gen-api/health")
async def health():
    """Route funtion to return health status of gen-api"""

    return JSONResponse(content={"API_status": "healthy"}, status_code=200)


@app.post("/gen-api/generate-images")
async def generate_images_api(payload: pydantic_check.ImageGenerateRequest):
    """Route function for generating images from Dall-e 2"""

    response, status_code = generate_images(vars(payload))
    if status_code==200:
        return response
    else:
        return JSONResponse(content=response, status_code=status_code)


@app.post("/gen-api/prompt-generation")
async def generate_images_api(payload: pydantic_check.PromptGenerateRequest):
    """Route function for prompt formation for Dall-e 2"""

    resend_response, status_code = optimize_prompt(vars(payload))
    return JSONResponse(content=resend_response, status_code=status_code)


# @app.post("/non-gen-api/modify_image")
# async def modify_image(image_specs: str = Form(...), image_file: UploadFile = File(...)):
#     # Parse image_specs JSON string to dictionary
#     specs_dict = json.loads(image_specs)

#     # Save the uploaded image
#     with open("temp_image.jpg", "wb") as temp_image:
#         shutil.copyfileobj(image_file.file, temp_image)

#     # Modify image properties
#     modified_image = modify_image_properties(specs_dict, "temp_image.jpg")

#     # Delete temporary image file
#     os.remove("temp_image.jpg")

#     # Return modified image as downloadable response
#     if modified_image:
#         return Response(content=modified_image.getvalue(), media_type="image/jpeg", headers={
#             "Content-Disposition": f"attachment; filename=modified_image.jpg"
#         })
#     else:
#         return {"message": "Image properties match the specifications."}


# Run the FastAPI server if this script is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
