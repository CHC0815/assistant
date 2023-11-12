from home import set_state, get_state
import configparser

config = configparser.ConfigParser()

def _set_light_status(light_id, status):
    config.read('config.ini')
    if light_id in config["Mappings"]:
        id = config["Mappings"][light_id]
        return set_state(id, status)
    return f"{light_id} not found"


SET_LIGHT_STATUS = {
    "name": "set_light_status",
    "fun": _set_light_status,
    "params": [
        "light_id",
        "status"
    ],
    "tool_desc": {
            "type": "function",
            "function": {
                "name": "set_light_status",
                "description": "Sets the status of a light to 'on' or 'off'",
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

}