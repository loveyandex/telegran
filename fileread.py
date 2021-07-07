import pickle
import random
import time
import traceback
from telethon import TelegramClient, events, sync
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputUser

from telethon.errors import UserPrivacyRestrictedError, PeerFloodError
from telethon.tl.functions.channels import InviteToChannelRequest

api_id = 95576
api_hash = '0bcee09d8c8beb2e7c0d52ce4c1ef594'
client = TelegramClient('session_name', api_id, api_hash)
client.start()

b = []
with open("1236110738__تریدرهای ارز دیجیتال.usrs", "rb") as fp:  # Unpickling
    b = pickle.load(fp)
k = 0

chann=client.get_entity("@RADIKALTOKEN") 
channel_id = chann.id
channel_access_hash = chann.access_hash

chanal=InputPeerChannel(channel_id, channel_access_hash)

for item in b[0:]:
    
    user_to_add = InputUser(item.id, item.access_hash)
    randrange = 0
    k = k + 1
    try:
        client(InviteToChannelRequest(chanal, [user_to_add]))
        print(f"{k}th {item.first_name} Waiting for {randrange} Seconds...")
        time.sleep(10)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        time.sleep(5*180)
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except:
        traceback.print_exc()
        print("Unexpected Error wait")
        sleep = time.sleep(randrange)
        continue
print(len(b))

