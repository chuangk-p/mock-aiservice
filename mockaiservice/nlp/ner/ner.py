import requests
from mockaiservice.setting.setting import get_api_key

def analyze(text:str, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key}
    url = "https://api.aiforthai.in.th/tner"
    data = {'text':text}

    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return {'POS':res.json()['POS'] , 'tags':res.json()['tags']}
    else:
        return res.json()
