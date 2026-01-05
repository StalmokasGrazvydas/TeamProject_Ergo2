from pydantic import BaseModel
from typing import Optional, Dict, Any

class CommandRequest(BaseModel):
    text: str
    context: Optional[Dict[str, Any]] = None
    user_id: Optional[str] = None

class UnityAction(BaseModel):
    action: str
    target: Optional[str] = None
    parameters: Dict[str, Any] = {}