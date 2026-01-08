from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Command Server")

@mcp.tool()
def set_color(target: str, color: str) -> dict:
    """Set the color of a specified target object.
    Args:
        target (str): The name of the target object.
        color (str): The color to set the target object to.
    Returns:
        dict: A dictionary containing the action, target, and parametersJson."""
    return {"action": "set_color", "target": target, "parametersJson": {"color": color}}

@mcp.tool()
def change_scene(scene_name: str) -> dict:
    """Change the current scene to the specified scene name.
    Args:
        scene_name (str): The name of the scene to switch to.
    Returns:
            dict: A dictionary containing the action, target, and parametersJson."""
    return {"action": "change_scene", "target": "scene_manager", "parametersJson": {"scene_name": scene_name}}

if __name__ == "__main__":
    mcp.run(transport="stdio")