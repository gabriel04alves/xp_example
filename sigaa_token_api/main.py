from fastapi import FastAPI
from auth import create_token

app = FastAPI()

@app.post("/token")
def login():
    token = create_token()
    return {"access_token": token, "token_type": "bearer"}