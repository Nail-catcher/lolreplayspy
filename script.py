import requests
from sys import argv
script, first = argv

start = int(first)/1000-15
end = int(first)/1000+15

url = 'https://127.0.0.1:2999/replay/recording'
headers = {}
payload = {
    "recording": "true",
    "path": "",
    "codec": "webm",
    "startTime": int(start),
    "endTime": int(end),
    "currentTime": 0,
    "width": 1920,
    "height": 1080,
    "framesPerSecond": 60,
    "enforceFrameRate": "false",
    "replaySpeed": 0
}
response = requests.post(url,verify=False, headers=headers, json=payload)
print (response)