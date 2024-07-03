from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI"

@app.get("/nombre")
async def nombre():
    return {'nombre': 'Samuel'}