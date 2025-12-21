from db import SessionLocal, Website
import uuid

db = SessionLocal()

website = Website(
    id=str(uuid.uuid4()),
    slug="test-site",
    email_to="conberntall@gmail.com"
)

db.add(website)
db.commit()

print("Test website created")
