import requests

def emonews(text:str, return_json:bool=False):
    url ="https://api.aiforthai.in.th/emonews/prediction"
    headers = {"apikey":"ovBT4rSBVze2Ia7i1GDz9JkEjpyaXU2t"}
    params = {"text":text}
    
    res = requests.get(url, params=params, headers=headers)
    if return_json == False:
        return res.json()['result']
    else:
        return res.json()
