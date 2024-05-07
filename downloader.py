from telethon import TelegramClient, events, sync
from telethon.tl.types import DocumentAttributeFilename, DocumentAttributeVideo
import os
from datetime import datetime
import sys
from dotenv import dotenv_values

env = dotenv_values(".env")

# Creating App via https://my.telegram.org/apps (on mobile, cause desktop says error)
app_id = env.get('APP_ID')
app_hash = env.get('APP_HASH')

if not app_id or not app_hash:
    print("Error: API_ID or APP_HASH are empty. Please fill in the .env file correctly.")
    sys.exit()

client = TelegramClient('session_name', app_id, app_hash)
client.start()

media_to_download = []

while True:
    group_input = input("Public Telegram Group-Name (required): ")
    if "https://t.me/" not in group_input:
        group_input = "https://t.me/" + group_input
    try:
        group = client.get_entity(group_input)
        break
    except ValueError:
        print("Not found. Please enter a valid group link or username.")
        print(group_input)
        print("Example: 'https://t.me/GROUP_NAME' or just 'GROUP_NAME'")


date_input_since = input("Date from (Format: DD.MM.YYYY): ")
if date_input_since:
    try:
        date_since = datetime.strptime(date_input_since, "%d.%m.%Y").date()
    except ValueError:
        print("Invalid date format. Please enter the date in the format DD.MM.YYYY.")


date_input_to = input("Date to (Format: DD.MM.YYYY): ")
if date_input_to:
    try:
        date_to = datetime.strptime(date_input_to, "%d.%m.%Y").date()
    except ValueError:
        print("Invalid date format. Please enter the date in the format DD.MM.YYYY.")
    

group_folder = group.username or str(group.id) 
if not os.path.exists(group_folder):
    os.makedirs(group_folder)
os.chdir(group_folder)
print("Change folder in " + group_folder)

limitInput = input("Limit of messages: ")
if limitInput == '':
    limitInput = 100
else:
    limitInput = int(limitInput)


for message in client.iter_messages(group, limit=limitInput):
    if date_input_since:
        if message.media and message.date.date() >= date_since:
            media_to_download.append(message)
    elif date_input_since and date_input_to:
        if message.media and message.date.date() >= date_since and message.date.date() <= date_to:
            media_to_download.append(message)
    else:
        if message.media:
            media_to_download.append(message)


def download_media(messageMedia):
    message.download_media()

media_to_download_length = len(media_to_download)
print("Collected " + str(media_to_download_length) + " media to download")
print("Start downloading ...")
i = 1;
for message in media_to_download:
    print(str(i)+"/"+str(media_to_download_length))
    download_media(message.media)
    i += 1


print("DONE")