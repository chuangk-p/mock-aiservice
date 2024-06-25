import requests
import json
from mockaiservice.setting.setting import get_api_key

def summarize(text:str, comp_rate:float=30, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'Content-Type':'application/json'}
    url = "https://api.aiforthai.in.th/textsummarize"
    data = json.dumps([{"id":100,"comp_rate":comp_rate,"src":text}])

    res = requests.post(url, data=data, headers=headers)
    return res.json()