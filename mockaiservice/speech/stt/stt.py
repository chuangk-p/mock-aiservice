import requests
from mockaiservice.setting.setting import get_api_key

def convert(path:str, outputlevel:str='--uttlevel', outputformat:str='--txt', return_json:bool=False):
    api_key = get_api_key()
    url = "https://api.aiforthai.in.th/partii-webapi"
    
    files = {'wavfile': (path, open(path, 'rb'), 'audio/wav')}
    headers = {
        'Apikey': api_key,
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        }
    
    params = {"outputlevel":"--uttlevel","outputformat":outputformat}
    res = requests.request("POST", url, headers=headers, files=files, data=params)
    if return_json == False:
        return res.json()['message']
    else:
        return res.json()
