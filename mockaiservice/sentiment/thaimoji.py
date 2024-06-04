import requests

def thaimoji(text:str, return_json:bool=False):
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
    headers = {
        'Apikey': "ovBT4rSBVze2Ia7i1GDz9JkEjpyaXU2t"
        }
    res = requests.get(url, params=params, headers=headers)
    if return_json == False:
        keys = res.json().keys()
        emoji = [moji_list[int(k)][0] for k in keys]
        return emoji

    else:
        return res.json()
