import requests
from mockaiservice.setting.setting import get_api_key

def convert(text:str, path:str, speaker:int=0, phrase_break:int=0, audiovisual:int=0):
    api_key = get_api_key()
    headers = {'Apikey':api_key}

    url = 'https://api.aiforthai.in.th/vaja9/synth_audiovisual'
    data = {'input_text':text,'speaker': speaker, 
            'phrase_break':phrase_break, 'audiovisual':audiovisual}
    
    response = requests.post(url, json=data, headers=headers)     
    resp = requests.get(response.json()['wav_url'],headers=headers)
    if resp.status_code == 200:
        with open(path, 'wb') as f:
            f.write(resp.content)

        return f'{path}'
    else:
        return resp.reason