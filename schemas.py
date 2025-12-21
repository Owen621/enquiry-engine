from pydantic import BaseModel

class EnquiryIn(BaseModel):
    website_slug: str
    name: str
    email: str
    message: str
