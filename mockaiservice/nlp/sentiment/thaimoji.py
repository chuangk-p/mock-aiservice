import requests
from mockaiservice.setting.setting import get_api_key

def analyze(text:str, return_json:bool=False):
    api_key = get_api_key()
    headers = {'Apikey':api_key}
    moji_list =[['🙂','😄','😁','😆','😀','😊','😃'],
    ['😢','😥','😰','😓','🙁','😟','😞','😔','😣','😫','😩'],
    ['😡','😠','😤','😖'],
    ['🙄','😒','😑','😕'],
    ['😱'],
    ['😨','😧','😦'],
    ['😮','😲','😯'],
    ['😴','😪'],
    ['😋','😜','😝','😛'],
    ['😍','💕','😘','😚','😙','😗'],
    ['😌'],
    ['😐'],
    ['😷'],
    ['😳'],
    ['😵'],
    ['💔'],
    ['😎','😈'],
    ['🙃','😏','😂','😭'],
    ['😬','😅','😶'],
    ['😉'],
    ['💖','💙','💚','💗','💓','💜','💘','💛'],
    ['😇']]

    url = "https://api.aiforthai.in.th/emoji"
    params = {'text':text}
    res = requests.get(url, params=params, headers=headers)
    if return_json == False:
        keys = res.json().keys()
        emoji = [moji_list[int(k)][0] for k in keys]
        return emoji

    else:
        return res.json()
