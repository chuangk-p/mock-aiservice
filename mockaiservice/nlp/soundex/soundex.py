import requests
from mockaiservice.setting.setting import get_api_key

def analyze(text:str, model:str='personname', return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key}

    url = "https://api.aiforthai.in.th/soundex"
    data = {'word':text, 'model':model}

    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['words']
    else:
        return res.json()
