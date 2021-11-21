import time
from datetime import datetime as dt
from random import randint

import requests
from telethon.sync import TelegramClient

API_ID = 0
API_HASH = ""

phone = "+380"

client = TelegramClient("main", API_ID, API_HASH)
client.start(lambda: phone)  # На вход требует функцию а не строку

name_to = "@vicka2"
links = [

]
# Котики
# links += ["https://fishki.net" + f"/picsw/062011/08/bonus/kotita/0{i}.jpg" for i in range(10, 20)]

photos = []
for content in map(lambda link: requests.get(link).content, links):
    open(f"pictures/{len(photos)}.jpg", 'wb').write(content)
    photos.append(f"pictures/{len(photos)}.jpg")

start_time = (10, 0)
while (now := dt.now()) and now.hour != start_time[0] and now.minute != start_time[1]:
    time.sleep(60)

while True:
    rand_time = randint(0, 60)
    time.sleep((60 - rand_time) * 60)
    photo_id = randint(0, len(photos) - 1)
    if type(photos[photo_id]) == str:
        photos[photo_id] = client.upload_file(f"pictures/{photo_id}.jpg")
    client.send_file(name_to, photos[photo_id])
    time.sleep((60 * 60 * 23) + (rand_time * 60))
