import requests

def tokenize(text:str, return_json:bool):
    url = "https://api.aiforthai.in.th/tpos"
    headers = {'Apikey':"ovBT4rSBVze2Ia7i1GDz9JkEjpyaXU2t"}
    data = {'text':text}

    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['words']
    else:
        return res.json()