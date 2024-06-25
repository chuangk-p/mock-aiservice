import requests
import json
from mockaiservice.setting.setting import get_api_key

def translate(text:str, src:str, to:str, return_json:bool=True):
    api_key = get_api_key()
    url = "https://api.aiforthai.in.th/xiaofan-zh-th"
    headers = {'Apikey':api_key, 'Content-Type':'application/json'}
    data = json.dumps({"input": text, "src": src, "trg": to})
    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['output']
    else:
        return res.json()
