import requests

def tokenize(text:str, normalize:bool, return_json:bool):
    url ='https://api.aiforthai.in.th/lextoplus'
    headers = {'Apikey':"ovBT4rSBVze2Ia7i1GDz9JkEjpyaXU2t"}
    data = {'text':text}
    
    if normalize == False:
        params['norm'] = '0'
    else:
        params['norm'] = '1'
    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['tokens']
    else:
        return res.json()
