"""
    this script hosts data-api routes
    that are written using FASTAPI
"""
import os
import logging
from typing import Dict, Any, List
from openai import OpenAI
import pydantic_check


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
file_handler = logging.FileHandler(os.path.join(log_directory, "generate_images.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_images(req_body):
    try:
        response = client.images.generate(prompt=req_body["prompt"],
        n=req_body["n"],
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
        return response, 200

    except Exception as generate_error:  # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%d", exception_type, filename, line_number)
        return {
                "update": False,
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{generate_error}",    # pylint: disable=line-too-long
            }, 500
