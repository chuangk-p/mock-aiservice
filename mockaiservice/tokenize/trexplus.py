import requests

def tokenize(text:str, return_json:bool):
    url = "https://api.aiforthai.in.th/tlexplus"
    headers = {'Apikey':"ovBT4rSBVze2Ia7i1GDz9JkEjpyaXU2t"}
    data = {'text':text}

    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['tokens']
    else:
        return res.json()