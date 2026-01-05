from fastapi import APIRouter
from models import CommandRequest, UnityAction
from services.command_router import interpret_command

router = APIRouter(prefix="/command", tags=["commands"])

@router.post("/", response_model=UnityAction)
def handle_command(cmd: CommandRequest):
    return interpret_command(cmd.text, cmd.context)