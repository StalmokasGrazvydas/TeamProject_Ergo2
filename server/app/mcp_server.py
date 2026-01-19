from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Command Server")

@mcp.tool()
def set_color(target: str, color: str) -> dict:
    """
    Set the color of a specified target object in Unity.

    Args:
        target (str):
            The name of the target GameObject in the Unity scene.
            This object must have a Renderer component.

        color (str):
            The color to apply to the object.
            Supported formats:
            - Named colors (e.g. "red", "blue", "green")
            - Hex colors (e.g. "#FF0000")

    Returns:
        dict:
            A command dictionary interpreted by Unity with the following fields:
            - action (str): Always "set_color"
            - target (str): The name of the target GameObject
            - parametersJson (dict):
                - color (str): The color value to apply
    """
    return {
        "action": "set_color",
        "target": target,
        "parametersJson": {"color": color}
    }


@mcp.tool()
def start_effect(effect_name: str) -> dict:
    """
    Start a visual effect in Unity.

    Args:
        effect_name (str):
            The name of the effect to start.
            Example values:
            - "rain"
            - "snow"
            - "fog"

            The effect must exist under the 'Particles' GameObject
            in the Unity scene.

    Returns:
        dict:
            A command dictionary interpreted by Unity with the following fields:
            - action (str): Always "start_effect"
            - target (str): Always "effect_manager"
            - parametersJson (dict):
                - effect_name (str): The effect to start
    """
    return {
        "action": "start_effect",
        "target": "effect_manager",
        "parametersJson": {"effect_name": effect_name}
    }


@mcp.tool()
def stop_effect(effect_name: str) -> dict:
    """
    Stop a visual effect in Unity.

    Args:
        effect_name (str):
            The name of the effect to stop.
            Must match an existing particle effect in Unity.

    Returns:
        dict:
            A command dictionary interpreted by Unity with the following fields:
            - action (str): Always "stop_effect"
            - target (str): Always "effect_manager"
            - parametersJson (dict):
                - effect_name (str): The effect to stop
    """
    return {
        "action": "stop_effect",
        "target": "effect_manager",
        "parametersJson": {"effect_name": effect_name}
    }


@mcp.tool()
def change_scene(scene_name: str) -> dict:
    """
    Change the currently active Unity scene.

    Args:
        scene_name (str):
            The exact name of the Unity scene to load.
            The scene must be included in the Unity Build Settings.

    Returns:
        dict:
            A command dictionary interpreted by Unity with the following fields:
            - action (str): Always "change_scene"
            - target (str): Always "scene_manager"
            - parametersJson (dict):
                - scene_name (str): The scene to load
    """
    return {
        "action": "change_scene",
        "target": "scene_manager",
        "parametersJson": {"scene_name": scene_name}
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")