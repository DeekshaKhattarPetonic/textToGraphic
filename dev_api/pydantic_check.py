from pydantic import BaseModel


class ImageGenerateRequest(BaseModel):
    prompt: str
    n: int

class PromptGenerateRequest(BaseModel):
    industry: str
    image_category: str
    targeted_customer_segment: str
    usage_purpose: str
    image_description: str
    image_aspect_ratio: str
    image_dpi: int
    image_color_depth: str
    image_resolution: str

class ImageSpecsRequest(BaseModel):
    image_aspect_ratio: str
    image_dpi: str
    image_color_depth: str
    image_resolution: str
