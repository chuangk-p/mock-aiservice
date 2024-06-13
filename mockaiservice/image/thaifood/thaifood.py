import base64
import requests, json
from mockaiservice.setting.setting import get_api_key

def analyze(file:str, return_json:bool=False):
    with open(file, 'rb') as image_file:
        base64_bytess = base64.b64encode(image_file.read())

    api_key = get_api_key()
    headers = {'Apikey':api_key, 'Content-Type':'application/json'}
    url = "https://api.aiforthai.in.th/thaifood"

    base64_bytes = base64_bytess.decode("utf-8")
    data = {"file":base64_bytes}
    params = json.dumps(data)
    
    res = requests.post(url, data=params, headers=headers)
    
    if return_json == False:
        return res.json()['objects']
    else:
        return res.json()

