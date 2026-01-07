import os
import shutil
import json
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class MCPClient:
    def __init__(self):
        self.session = None
        self.exit_stack = None

    async def connect(self):
        python_cmd = shutil.which("python") or "python"
        server_path = os.path.join(os.path.dirname(__file__), "mcp_server.py")

        server_params = StdioServerParameters(
            command=python_cmd,
            args=[server_path],
            env=None
        )

        self.exit_stack = AsyncExitStack()

        read, write = await self.exit_stack.enter_async_context(
            stdio_client(server_params)
        )

        self.session = await self.exit_stack.enter_async_context(
            ClientSession(read, write)
        )

        await self.session.initialize()

    async def close(self):
        if self.exit_stack:
            await self.exit_stack.aclose()
        self.session = None
        self.exit_stack = None

    async def list_llm_tools(self):
        tools = await self.session.list_tools()

        return [
            {
                "type": "function",
                "function": {
                    "name": t.name,
                    "description": t.description or "",
                    "parameters": t.inputSchema
                }
            }
            for t in tools.tools
        ]

    async def call_tool(self, name: str, args: dict):
        result = await self.session.call_tool(name, args)
        block = result.content[0]

        # Convert any Pydantic model to JSON string first
        if hasattr(block, "model_dump_json"):
            raw = block.model_dump_json()
        elif hasattr(block, "text"):
            raw = block.text
        else:
            raw = "{}"

        # ✅ Parse the JSON string into a Python dict
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            # Fallback if LLM returned invalid JSON
            return {
                "action": "unknown",
                "target": "",
                "parametersJson": {"raw": raw}
            }

    async def interpret_with_llm(self, text: str, interpreter):
        tools = await self.list_llm_tools()
        decision = await interpreter.interpret(text, tools)
        if not decision:
            return {"action": "unknown", "target": "", "parametersJson": {"text": text}}

        # Fill missing required fields with defaults
        args = decision.get("arguments", {})
        tool_name = decision.get("tool")

        if not tool_name:
            return {"action": "unknown", "target": "", "parametersJson": {"text": text}}

        if "target" not in args:
            args["target"] = "Cube"

        # Call tool and return parsed JSON
        return await self.call_tool(tool_name, args)