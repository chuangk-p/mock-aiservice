import requests,json,base64 
from mockaiservice.setting.setting import get_api_key

def analyze(file:str, return_json:bool=False):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'Content-Type':'application/json'}
    fileByte = open(file, 'rb').read()
    b64 = base64.b64encode(fileByte)
    params = json.dumps({"file":b64.decode('ascii') })

    url ='https://api.aiforthai.in.th/nsfw'

    
    res = requests.post(url, data=params, headers=headers)
    
    if return_json == False:
        return res.json()['objects']
    else:
        return res.json()

