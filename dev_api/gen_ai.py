"""
    this script hosts data-api routes
    that are written using FASTAPI
"""
import os
import sys
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
        prompt_modified = req_body["prompt"] + " The generated image should be realistic and detail oriented."
        response = client.images.generate(prompt=prompt_modified,
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


example_json = {
"industry": "Finance",
"image_category": "Process Category",
"targeted_customer_segment": "Accountants",
"usage_purpose": "Educational material for training accountants on new financial software processes",
"image_description": "An illustration showing a step-by-step guide on how to use the new financial software. The image includes a modern office setting with an accountant using a computer, financial charts on the screen, and icons representing different software features.",
"image_aspect_ratio": "16:9",
"image_dpi": "300",
"image_color_depth": "24-bit",
"image_resolution": "1920x1080"
}

prompt_generated = "Create an illustration for the finance industry targeting accountants. The image should serve as educational material for training accountants on new financial software processes. It should depict a step-by-step guide on using the software, set in a modern office with an accountant using a computer. Include financial charts on the screen and icons representing different software features. The image should have a 16:9 aspect ratio, 300 DPI, 24-bit color depth, and 1920x1080 resolution."


def optimize_prompt(req_body):
    try:
        prompt = """Help me convert this json {req_body} to a one line prompt for dall-e 2.
                    Make sure you do not delete any information, or add any.
                    To ensure that DALL-E 2 understands all the requirements, it's helpful to format the prompt in a clear and concise way.
                    This prompt retains all the information while ensuring clarity and conciseness for DALL-E 2.
                    Below are examples of a json, and the prompt generated from it:
                    example json: {example_json}
                    prompt generated: {prompt_generated}
                    Do not get biased by the example. Generate prompt logically."""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt.format(req_body=req_body,example_json=example_json,prompt_generated=prompt_generated)}
            ],
            max_tokens=4000,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip(), 200

    except Exception as generate_error:  # pylint: disable=broad-exception-caught
        exception_type, _, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        logger.error("%s||||%s||||%d", exception_type, filename, line_number)
        return {
                "helpText": f"Exception: {exception_type}||||{filename}||||{line_number}||||{generate_error}",    # pylint: disable=line-too-long
            }, 500
