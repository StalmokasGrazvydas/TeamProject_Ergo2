# FastAPI example
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CommandRequest(BaseModel):
    text: str

@app.post("/command")
def handle_command(req: CommandRequest):
    # Map text to structured UnityAction
    if "red" in req.text:
        action = "turn_red"
    elif "blue" in req.text:
        action = "turn_blue"
    else:
        action = "unknown"

    return {
        "action": action,
        "target": "Cube",
        "parametersJson": "{}"
    }