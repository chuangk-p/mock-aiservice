import requests
from mockaiservice.setting.setting import get_api_key

def analyze(file:str, return_json:bool):
    api_key = get_api_key()
    url ='https://api.aiforthai.in.th/detectfacemask'

    payload={}
    files=[('file',(file,open(file,'rb'),'image/jpeg'))]

    headers = {'Apikey':api_key}

    res = requests.request("POST", url, headers=headers, data=payload, files=files)

    if return_json == False:
        return res.json()['objects']
    else:
        return res.json()

