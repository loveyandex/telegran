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
client = TelegramClient('session_name', api_id, api_hash)
client.start()

from telethon.tl.types import InputPeerChat


# Other kind of entities.
chats = client.get_entity("https://t.me/joinchat/sP7qisaaa4k5NDFk")
chat_id = chats.id

print("chat_id",chats)



b = []
with open("1456018596.usrs", "rb") as fp:  # Unpickling
    b = pickle.load(fp)
k = 0

for item in b[555:]:
    print(item)
    randrange = random.randrange(1, 2)
    k = k + 1
    try:
        # Note that ``user_to_add`` is NOT the name of the parameter.
        # It's the user you want to add (``user_id=user_to_add``).

        print(f"{k}th {item.first_name} Waiting for {randrange} Seconds...")
        client(AddChatUserRequest(
            chat_id,
            int(item.id),
            fwd_limit=100  # Allow the user to see the 10 last messages
        ))
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
