import requests


def sendCommercial(seconds=30):
    url = 'https://api.twitch.tv/kraken/channels/68307698/commercial'

    headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': '9ljs1m0m88zr2w2vgngm5ytpzf5xbx',
            'Authorization': 'OAuth plzzydjz89p7xgjgosrq29vp2nbqg8',
            'Content-Type': 'application/json'}
        
    data = '{"length":' + str(seconds) + '}'
    try:
        r = requests.post(url, headers=headers, timeout=2, data=data)
    except requests.exceptions.Timeout:
        raise Exception('timeout')

    results = r.content


    print(f'Sending commercial result: {results}')

'''
https://dev.twitch.tv/docs/authentication#getting-tokens

https://id.twitch.tv/oauth2/authorize?client_id=fsdki8jqahtbpbbpzryor6p29gn2ji&redirect_uri=http%3A%2F%2Flocalhost&response_type=token+id_token&scope=channel_commercial+openid
#http://localhost/#access_token=plzzydjz89p7xgjgosrq29vp2nbqg8&id_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjEifQ.eyJhdWQiOiI5bGpzMW0wbTg4enIydzJ2Z25nbTV5dHB6ZjV4YngiLCJleHAiOjE2MTQ2MzkyMjIsImlhdCI6MTYxNDYzODMyMiwiaXNzIjoiaHR0cHM6Ly9pZC50d2l0Y2gudHYvb2F1dGgyIiwic3ViIjoiNjgzMDc2OTgiLCJhdF9oYXNoIjoiWXI5akxhVFlTWEFVOGQ4WmMwbmJqUSIsImF6cCI6IjlsanMxbTBtODh6cjJ3MnZnbmdtNXl0cHpmNXhieCIsInByZWZlcnJlZF91c2VybmFtZSI6IlJlcG9ydEZvckZsYW1lIn0.VZ-uFD-D2nFXg4topEar9kmVwJeXbf5-5sbkNB6mEJ0SQV-UtoOqmR4vCiSTIfgpqtZRUZtq7yqxaXY-VCzsTkaMEeUqI1DUZsu0JJI4xuuf0kb2unedI3xMzhV80-ZUq-3jYPsd_zMSvHDKD1sP-U9GMYb81bNpdVXJWrE-bRUQfNMN8uBj_Y-hnJUonnz1KESxSYKkLDlM8AJPujHpcL2gJn6gyaePkprtEN2aXFGdXP3-pTDdQIwmWSwOQm6CySu3gH2mW-O_YYCJcQzyntNSbgovW_PVIfKTeI8WWyB3Qrg-Z7LcJ7UpevQCoPqa4PwHG67hrzH6GfFAvKLopg&scope=channel_commercial+openid&token_type=bearer'
'''
