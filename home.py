import requests
import configparser

config = configparser.ConfigParser()

def get_state(id) -> (int, str):
    config.read('config.ini')
    url = config["HomeAssistant"]["url"] + ":" + config["HomeAssistant"]["port"] + "/api/states/" + id
    headers = {
        "Authorization": "Bearer " + config["HomeAssistant"]["token"],
        "content-type": "application/json"
    }

    response = requests.request("GET", url, headers=headers)
    return (response.status_code, response.text)

def set_state(id, state) -> (int, str):
    config.read('config.ini')

    url = config["HomeAssistant"]["url"] + ":" + config["HomeAssistant"]["port"] + "/api/services/switch/turn_"
    if state == "on":
        url += "on"
    elif state == "off":
        url += "off"

    headers = {
        "Authorization": "Bearer " + config["HomeAssistant"]["token"],
        "content-type": "application/json"
    }

    data = {
        "entity_id": id
    }

    response = requests.request("POST", url, headers=headers, json=data)
    return (response.status_code, response.text)

def main():
    config.read('config.ini')

    print(set_state("test123", "off"))


if __name__ == "__main__":
    main()