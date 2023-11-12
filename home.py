import requests
import configparser

config = configparser.ConfigParser()

def get_state(id) -> (int, str):
    config.read('config.ini')
    base_url = config["HomeAssistant"]["url"]
    port = config["HomeAssistant"]["port"]
    url = base_url + ":" + port + "/api/states/" + id
    headers = {
        "Authorization": "Bearer " + config["HomeAssistant"]["token"],
        "content-type": "application/json"
    }

    response = requests.request("GET", url, headers=headers)
    return (response.status_code, response.text)

def set_state(id, state) -> (int, str):
    config.read('config.ini')

    base_url = config["HomeAssistant"]["url"]
    port = config["HomeAssistant"]["port"]

    type = id.split(".")[0]

    url = base_url + ":" + port + f"/api/services/{type}/turn_"
    if state == "on":
        url += "on"
    elif state == "off":
        url += "off"

    token = config["HomeAssistant"]["token"]
    headers = {
        "Authorization": "Bearer " + token,
        "content-type": "application/json"
    }

    data = {
        "entity_id": id
    }

    response = requests.request("POST", url, headers=headers, json=data)
    return (response.status_code, response.text)

def main():
    print(set_state("test123", "off"))


if __name__ == "__main__":
    main()