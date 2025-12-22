from pydantic import BaseModel
from typing import Optional

class EnquiryIn(BaseModel):
    website_slug: str
    name: str
    email: str
    message: str
    company: Optional[str] = None  # honeypot
