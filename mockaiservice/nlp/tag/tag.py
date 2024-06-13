import requests
from mockaiservice.setting.setting import get_api_key

def analyze(text:str, numtag:int, return_json:bool=False):
    api_key = get_api_key()
    headers = {'Apikey':api_key}

    url = "https://api.aiforthai.in.th/tagsuggestion"   
    data = {'text':text,'numtag':str(numtag)}
        
    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['tags']
    else:
        return res.json()
