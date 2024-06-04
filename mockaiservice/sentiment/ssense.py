import requests

def ssense(text:str, return_json:bool=False):
    url = "https://api.aiforthai.in.th/ssense"
    headers = {"apikey":"ovBT4rSBVze2Ia7i1GDz9JkEjpyaXU2t"}
    data = {"text":text}
    
    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['sentiment']
    else:
        return res.json()
