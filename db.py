from sqlalchemy import create_engine, Column, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=True
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Website(Base):
    __tablename__ = "websites"
    id = Column(String, primary_key=True)
    slug = Column(String, unique=True)
    email_to = Column(String)

class Enquiry(Base):
    __tablename__ = "enquiries"
    id = Column(String, primary_key=True)
    website_id = Column(String, ForeignKey("websites.id"))
    name = Column(String)
    email = Column(String)
    message = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)
