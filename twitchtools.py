import requests
import json


# Función para enviar anuncio
def sendCommercial(seconds):
    url = 'https://api.twitch.tv/helix/channels/commercial'

    headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': '9ljs1m0m88zr2w2vgngm5ytpzf5xbx',
            'Authorization': 'Bearer 6n4cq9u9p249baheohfb9sppr233tl',
            'Content-Type': 'application/json'}

    data = '{"broadcaster_id": "68307698","length":' + str(seconds) + '}'
    try:
        r = requests.post(url, headers=headers, timeout=2, data=data)
    except requests.exceptions.Timeout:
        raise Exception('timeout')

    results = r.content

    print(f'Sending commercial result: {results}')


# Funcion para sacar la informacion de un stream
def streamData():
    url = 'https://api.twitch.tv/helix/channels?broadcaster_id=68307698'

    headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': '9ljs1m0m88zr2w2vgngm5ytpzf5xbx',
            'Authorization': 'Bearer x94exnv7s5bp53vssdjm462ruq8lmq'}

    try:
        r = requests.get(url, headers=headers, timeout=2)
    except requests.exceptions.Timeout:
        raise Exception('timeout')

    resultsByte = r.content
    resultsStr = resultsByte.decode('utf8')
    data = json.loads(resultsStr)
    print(f'Sending streamData results: {data}')
    try:
        return data.get('data')[0]
    except IndexError:
        return None


# Función para convertir texto a id de juego
def gameId(game):
    url = 'https://api.twitch.tv/helix/games?name=' + str(game)

    headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': '9ljs1m0m88zr2w2vgngm5ytpzf5xbx',
            'Authorization': 'Bearer 6vluva5hnxag4tkrgw8fb36k23jm6z'}
    print(url)
    try:
        r = requests.get(url, headers=headers, timeout=2)
    except requests.exceptions.Timeout:
        raise Exception('timeout')

    resultsByte = r.content
    print(resultsByte)
    resultsStr = resultsByte.decode('utf8')
    data = json.loads(resultsStr)
    print(f'Sending streamGame results: {data}')
    return data.get('data')[0]


# Función para cambiar el titulo del stream
def setTitle(title):
    url = 'https://api.twitch.tv/helix/channels?broadcaster_id=68307698'

    headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': '9ljs1m0m88zr2w2vgngm5ytpzf5xbx',
            'Authorization': 'Bearer ow5eb0mn24grw8uuhjq86l037prqbw',
            'Content-Type': 'application/json'}
    data = streamData()
    game = data.get('game_id')
    data = '{"game_id":"' + str(game) + '", "title":"' + str(title)
    + '", "broadcaster_language":"es"}'

    try:
        r = requests.patch(url, headers=headers, timeout=2, data=data)
    except requests.exceptions.Timeout:
        raise Exception('timeout')

    results = r.content

    print(f'Sending setTitle results: {results}')


# Función para cambiar la categoria del stream
def setGame(name):
    url = 'https://api.twitch.tv/helix/channels?broadcaster_id=68307698'

    headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': '9ljs1m0m88zr2w2vgngm5ytpzf5xbx',
            'Authorization': 'Bearer ow5eb0mn24grw8uuhjq86l037prqbw',
            'Content-Type': 'application/json'}
    data = streamData()
    title = data.get('title')
    data1 = gameId(name)
    game = data1.get('id')
    data = '{"game_id":"' + str(game) + '", "title":"' + str(title)
    + '", "broadcaster_language":"es"}'

    try:
        r = requests.patch(url, headers=headers, timeout=2, data=data)
    except requests.exceptions.Timeout:
        raise Exception('timeout')

    results = r.content

    print(f'Sending setGame results: {results}')


# Función para comprobar que un canal está en directo
def streamLive():
    url = 'https://api.twitch.tv/helix/streams?user_id=68307698'

    headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': '9ljs1m0m88zr2w2vgngm5ytpzf5xbx',
            'Authorization': 'Bearer ow5eb0mn24grw8uuhjq86l037prqbw'}

    try:
        r = requests.get(url, headers=headers, timeout=2)
    except requests.exceptions.Timeout:
        raise Exception('timeout')

    resultsByte = r.content
    resultsStr = resultsByte.decode('utf8')
    data = json.loads(resultsStr)
    print(f'Sending streamGame results: {data}')
    try:
        result = data.get('data')[0]
    except TypeError:
        result = None
    return result


# Función para convertir texto a id de user
def UserToId(user):
    url = 'https://api.twitch.tv/helix/games?name='

    headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': '9ljs1m0m88zr2w2vgngm5ytpzf5xbx',
            'Authorization': 'Bearer 6vluva5hnxag4tkrgw8fb36k23jm6z'}
    print(url)
    try:
        r = requests.get(url, headers=headers, timeout=2)
    except requests.exceptions.Timeout:
        raise Exception('timeout')

    resultsByte = r.content
    print(resultsByte)
    resultsStr = resultsByte.decode('utf8')
    data = json.loads(resultsStr)
    print(f'Sending streamGame results: {data}')
    return data.get('data')[0]


# Función para ver desde hace cuanto tiempo sigues al canal
def followSince(user):
    url = 'https://api.twitch.tv/helix/users/follows?'
    'first=1&to_id=68307698&from_id=' + str(user)

    headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': '9ljs1m0m88zr2w2vgngm5ytpzf5xbx',
            'Authorization': 'Bearer ow5eb0mn24grw8uuhjq86l037prqbw'}

    try:
        r = requests.get(url, headers=headers, timeout=2)
    except requests.exceptions.Timeout:
        raise Exception('timeout')

    resultsByte = r.content
    resultsStr = resultsByte.decode('utf8')
    data = json.loads(resultsStr)
    print(f'Sending streamGame results: {data}')
    data = data.get('data')[0]
    fecha = data.get('followed_at')
    print(fecha)
    return fecha


'''
https://dev.twitch.tv/docs/authentication#getting-tokens
channel:edit:commercial
https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=9ljs1m0m88zr2w2vgngm5ytpzf5xbx&redirect_uri=http://localhost&scope=channel:manage:broadcast
#http://localhost/#access_token=plzzydjz89p7xgjgosrq29vp2nbqg8&id_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjEifQ.eyJhdWQiOiI5bGpzMW0wbTg4enIydzJ2Z25nbTV5dHB6ZjV4YngiLCJleHAiOjE2MTQ2MzkyMjIsImlhdCI6MTYxNDYzODMyMiwiaXNzIjoiaHR0cHM6Ly9pZC50d2l0Y2gudHYvb2F1dGgyIiwic3ViIjoiNjgzMDc2OTgiLCJhdF9oYXNoIjoiWXI5akxhVFlTWEFVOGQ4WmMwbmJqUSIsImF6cCI6IjlsanMxbTBtODh6cjJ3MnZnbmdtNXl0cHpmNXhieCIsInByZWZlcnJlZF91c2VybmFtZSI6IlJlcG9ydEZvckZsYW1lIn0.VZ-uFD-D2nFXg4topEar9kmVwJeXbf5-5sbkNB6mEJ0SQV-UtoOqmR4vCiSTIfgpqtZRUZtq7yqxaXY-VCzsTkaMEeUqI1DUZsu0JJI4xuuf0kb2unedI3xMzhV80-ZUq-3jYPsd_zMSvHDKD1sP-U9GMYb81bNpdVXJWrE-bRUQfNMN8uBj_Y-hnJUonnz1KESxSYKkLDlM8AJPujHpcL2gJn6gyaePkprtEN2aXFGdXP3-pTDdQIwmWSwOQm6CySu3gH2mW-O_YYCJcQzyntNSbgovW_PVIfKTeI8WWyB3Qrg-Z7LcJ7UpevQCoPqa4PwHG67hrzH6GfFAvKLopg&scope=channel_commercial+openid&token_type=bearer'
'''
