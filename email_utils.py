import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

FROM_EMAIL = "Enquiries <enquiries@chapterweb.co.uk>"

def send_email(to_email: str, subject: str, body: str):
    if not resend.api_key:
        print("Resend API key missing")
        return

    try:
        resend.Emails.send({
            "from": FROM_EMAIL,
            "to": [to_email],
            "subject": subject,
            "text": body,
        })
    except Exception as e:
        print("Email failed:", e)