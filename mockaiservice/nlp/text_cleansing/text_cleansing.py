import requests
from mockaiservice.setting.setting import get_api_key

def clean(text:str, return_json:bool=False):
    api_key = get_api_key()
    headers = {'Apikey':api_key}

    url = "https://api.aiforthai.in.th/textcleansing"
    data = {'text':text}

    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['cleansing_text']
    else:
        return res.json()
