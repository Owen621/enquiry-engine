from fastapi import FastAPI
from db import SessionLocal, Website, Enquiry
from schemas import EnquiryIn
from email_utils import send_email
import uuid

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/enquiry")
def create_enquiry(data: EnquiryIn):
    db = SessionLocal()

    website = db.query(Website).filter(
        Website.slug == data.website_slug
    ).first()

    if not website:
        return {"error": "Invalid website"}

    enquiry = Enquiry(
        id=str(uuid.uuid4()),
        website_id=website.id,
        name=data.name,
        email=data.email,
        message=data.message
    )

    db.add(enquiry)
    db.commit()
    send_email(
        to_email=website.email_to,
        subject="New enquiry received",
        body=f"""
    New enquiry for {website.slug}

    Name: {data.name}
    Email: {data.email}

    Message:
    {data.message}
    """
    )

    return {"status": "saved"}
