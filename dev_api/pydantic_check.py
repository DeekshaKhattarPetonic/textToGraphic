from pydantic import BaseModel


class ImageGenerateRequest(BaseModel):
    prompt: str
    n: int
