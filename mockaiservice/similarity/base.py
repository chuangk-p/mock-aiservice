import requests

def similarity(text:str, model:str, numword:int, return_json:bool):
    url = "https://api.aiforthai.in.th/thaiwordsim"
    headers = {'Apikey':"ovBT4rSBVze2Ia7i1GDz9JkEjpyaXU2t"}

    if model != 'thwiki' and model != 'twitter':
        raise ValueError(
            f"""Model \"{model}\" not found."""
        )
    data = {'word':text,'model':model,'numword':str(numword)}
    
    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['words']
    else:
        return res.json()
