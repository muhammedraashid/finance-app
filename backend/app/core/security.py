from datetime import datetime, timedelta, timezone
from jose import jwt
from dotenv import load_dotenv
import os


load_dotenv()

SECRET = os.getenv("SECRET_KEY")
ALGORITHM =  os.getenv("ALGORITHM")

def create_access_token(data: dict, expires:int = None):
    expire_minutes = expires or int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",60))
    payload = data.copy()
    payload["exp"] = timezone.now() + timedelta(minutes=expire_minutes)
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)