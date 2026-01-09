import os
import json
import ollama

# Make Ollama accessible to the container
os.environ["OLLAMA_HOST"] = "http://host.docker.internal:11434"

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
"make the cube red" → {{"tool": "set_color", "arguments": {{"target": "cube", "color": "red"}}}}

For changing scenes, use the exact scene names provided: "MainMenu", "World_1", "World_2", "World_3", "World_4", "World_5"

User command:
{text}
"""

        try:
            # ✅ Remove the invalid 'host' argument
            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": 0}
            )

            content = response["message"]["content"].strip()
            return json.loads(content)
        except json.JSONDecodeError:
            print(f"[OllamaInterpreter] Failed to parse JSON from response:\n{content}")
            return None
        except Exception as e:
            print(f"[OllamaInterpreter] Ollama error: {e}")
            return None