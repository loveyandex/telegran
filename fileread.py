import pickle
import random
import time
import traceback
from telethon import TelegramClient, events, sync

from telethon.errors import UserPrivacyRestrictedError, PeerFloodError
from telethon.tl.functions.channels import InviteToChannelRequest

api_id = 95576
api_hash = '0bcee09d8c8beb2e7c0d52ce4c1ef594'
client = TelegramClient('session_name', api_id, api_hash)
client.start()

b = []
with open("1456018596.usrs", "rb") as fp:  # Unpickling
    b = pickle.load(fp)
k = 0
# client.send_message("@Javadyasemi,"hey hey javad bot bot "")
client(InviteToChannelRequest("@quantomfx", [b[22].id]))
print(len(b))