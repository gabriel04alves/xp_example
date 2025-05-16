import os
from datetime import datetime, timedelta, timezone
from jose import jwt 
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM") 

def create_token():
    expire = datetime.now(timezone.utc) + timedelta(hours=24)
    payload = {"exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)