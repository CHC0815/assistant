SET_LIGHT_STATUS_TOOL = {
            "type": "function",
            "function": {
                "name": "set_light_status",
                "description": "Sets the status of a light to on or off",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "light_id": {
                            "type": "string",
                            "description": "The id of the light",
                        },
                        "status": {"type": "string", "enum": ["on", "off"]},
                    },
                    "required": ["light_id", "status"],
                },
            },
    }

def set_light_status(light_id, status):
    print(f"Setting light {light_id} to {status}")
    return f"Setting light {light_id} to {status}"

def get_tool_set_light_status():
    return (SET_LIGHT_STATUS_TOOL, set_light_status)