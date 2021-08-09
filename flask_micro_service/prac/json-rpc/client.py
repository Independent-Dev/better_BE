# 출처: https://www.todaymart.com/m/74
import requests
import json


def main():
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload_list = [{
        "method": "echo",
        "params": ["echome!"],
        "id": 0
    }, {
        "method": "echo",
        "params": ["echome!", "xxx"],
        "id": 0
    }, {
        "method": "add",
        "params": ["1", "1"],
        "id": 0
    }, {
        "method": "add",
        "params": [1, 1],
        "id": 0
    }]
    for payload in payload_list:
        response = requests.post(url, data=json.dumps(payload), headers=headers).json()

        print(response)

if __name__ == "__main__":
    main()