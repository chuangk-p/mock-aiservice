import requests
from mockaiservice.setting.setting import get_api_key, PACKAGE_NAME

def analyze(text:str, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    url = "https://api.aiforthai.in.th/ssense"
    data = {"text":text}
    
    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['sentiment']
    else:
        return res.json()
