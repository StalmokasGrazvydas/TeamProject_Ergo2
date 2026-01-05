from fastapi import FastAPI
from routes import commands, health

app = FastAPI(title="Immersive Room Command Server")

app.include_router(commands.router)
app.include_router(health.router)

@app.get("/")
def root():
    return {"status": "running"}