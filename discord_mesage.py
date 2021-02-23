import requests


payload = {
    'content': "yoyo"
}

header ={
    'authorization': 'MzIzNDk2NDkzMTQ1MTI4OTYw.YCp79g.5Ot6UYGLUSHbmXebiMONI6aiDlA'
}

r = requests.post("https://discord.com/api/v8/channels/807274192503570432/messages", data=payload, headers=header)
