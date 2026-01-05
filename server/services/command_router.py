from models import UnityAction

def interpret_command(text: str, context: dict | None) -> UnityAction:
    text = text.lower()

    if "open" in text and "door" in text:
        return UnityAction(
            action="open_door",
            target="door_01",
            parameters={}
        )

    if "turn red" in text:
        return UnityAction(
            action="set_color",
            target=context.get("pointed_object") if context else None,
            parameters={"color": "red"}
        )

    return UnityAction(
        action="unknown",
        parameters={"reason": "Command not recognized"}
    )