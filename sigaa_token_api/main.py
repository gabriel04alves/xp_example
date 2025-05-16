from fastapi import FastAPI
app = FastAPI()

@app.post("/token")
def login():
    print('Passou por aqui...')
    return {"Endpoint funcionando!"}