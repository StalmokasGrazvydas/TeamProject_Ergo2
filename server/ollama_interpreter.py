import json
import ollama

class OllamaInterpreter:
    def __init__(self, model="llama3.2:3b"):
        self.model = model

    async def interpret(self, text: str, tools: list[dict]) -> dict | None:
        tool_list = "\n".join(
            f"- {t['function']['name']}: {t['function']['description']}"
            for t in tools
        )

        prompt = f"""
You are a command interpreter.
Choose the correct command and arguments.

Available commands:
{tool_list}

All commands require all their fields. Required fields must always be present.
If the user does not specify a value, use a sensible default.

Respond ONLY with valid JSON:
{{
  "tool": "<tool_name>",
  "arguments": {{ ... }}
}}

Examples:
"make the cube red" → {{"tool": "set_color", "arguments": {{"target": "Cube", "color": "red"}}}}
"move the cube up" → {{"tool": "move_object", "arguments": {{"target": "Cube", "direction": "up"}}}}

User command:
{text}
"""

        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0}
        )

        content = response["message"]["content"].strip()

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return None