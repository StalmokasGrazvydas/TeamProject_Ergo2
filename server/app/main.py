from fastapi import FastAPI
from pydantic import BaseModel
from mcp_client import MCPClient
from ollama_interpreter import OllamaInterpreter
from contextlib import asynccontextmanager

mcp_client = MCPClient()
interpreter = OllamaInterpreter()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[FastAPI] Starting MCP client...")
    await mcp_client.connect()
    print("[FastAPI] MCP client connected")
    try:
        yield
    finally:
        print("[FastAPI] Closing MCP client...")
        await mcp_client.close()
        print("[FastAPI] MCP client closed")

app = FastAPI(lifespan=lifespan)

class CommandRequest(BaseModel):
    text: str

@app.post("/command")
async def handle_command(req: CommandRequest):
    return await mcp_client.interpret_with_llm(req.text, interpreter)