import pickle
import random
import time
import traceback
from telethon import TelegramClient, events, sync

from telethon.errors import UserPrivacyRestrictedError, PeerFloodError
from telethon.tl.functions.channels import InviteToChannelRequest

from telethon.tl.functions.messages import AddChatUserRequest

from telethon import TelegramClient, events, sync
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

# Note that ``user_to_add`` is NOT the name of the parameter.
# It's the user you want to add (``user_id=user_to_add``).

api_id = 95576
api_hash = '0bcee09d8c8beb2e7c0d52ce4c1ef594'
bot_token = '1269265114:AAEEtK6S-qaLkAjj2BnO_0d6FPx_1YDvGYk'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

# Other kind of entities.
chats = client.get_entity('https://t.me/joinchat/IqQKlsM8rsNdlntc')

chat_id = chats.id


b = []
with open("1456018596.usrs", "rb") as fp:  # Unpickling
    b = pickle.load(fp)
k = 0

for item in b[390:]:
    randrange = random.randrange(300, 800)
    k = k + 1
    try:
        # Note that ``user_to_add`` is NOT the name of the parameter.
        # It's the user you want to add (``user_id=user_to_add``).

        client(AddChatUserRequest(
            chat_id,
            item.id,
            fwd_limit=100  # Allow the user to see the 10 last messages
        ))
        print(f"{k}th {item.first_name} Waiting for {randrange} Seconds...")
        time.sleep(randrange)
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
