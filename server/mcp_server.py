from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Command Server")

@mcp.tool()
def set_color(target: str, color: str) -> dict:
    return {
        "action": "set_color",
        "target": target,
        "parametersJson": {"color": color}
    }

@mcp.tool()
def move_object(target: str, direction: str) -> dict:
    return {
        "action": "move",
        "target": target,
        "parametersJson": {"direction": direction}
    }

@mcp.tool()
def rotate_object(target: str, degrees: int) -> dict:
    return {
        "action": "rotate",
        "target": target,
        "parametersJson": {"degrees": degrees}
    }

if __name__ == "__main__":
    mcp.run(transport="stdio")