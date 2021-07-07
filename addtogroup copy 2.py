from telethon.tl.types import InputPeerChat, MessageActionChatAddUser, MessageActionChatDeleteUser
import pickle
import random
import time
import traceback
from telethon import TelegramClient, events, sync
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser

from telethon.errors import UserPrivacyRestrictedError, PeerFloodError
from telethon.tl.functions.channels import InviteToChannelRequest,DeleteMessagesRequest

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


# Other kind of entities.
chats = client.get_entity("https://t.me/joinchat/sP7qisaaa4k5NDFk")

chat_id = chats.id
target_group_entity = InputPeerChannel(chats.id, chats.access_hash)
# print("chat_id",chats)

@client.on(events.NewMessage(chats=target_group_entity))
def my_event_handler(event):
    message=(event.message)
    if isinstance(message.action, MessageActionChatDeleteUser) or isinstance(message.action, MessageActionChatAddUser):
            result = client(DeleteMessagesRequest(target_group_entity, [message.id]))
            print(result)



b = []
with open("1236110738__تریدرهای ارز دیجیتال.usrs", "rb") as fp:  # Unpickling
    b = pickle.load(fp)
k = 0

for user in b[250:]:
    print(user)
    user_to_add = InputPeerUser(user.id, user.access_hash)
    randrange = random.randrange(2, 5)
    k = k + 1
    try:
        # Note that ``user_to_add`` is NOT the name of the parameter.
        # It's the user you want to add (``user_id=user_to_add``).

        print(f"{k}th {user.first_name} Waiting for {randrange} Seconds...")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))

        time.sleep(randrange)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        time.sleep(5*180)
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except Exception as e:
        # traceback.print_exc()
        print(f"Unexpected Error wai{e.__str__}")
        sleep = time.sleep(randrange)
        continue
print(len(b))


def deleteaddusermsg(chat ,channel):
    i=0
    for message in client.iter_messages(chat):
        # do something with the message from recent to older
        print((message))
        if isinstance(message.action, MessageActionChatDeleteUser) or isinstance(message.action, MessageActionChatAddUser):
            result = client(DeleteMessagesRequest(channel, [message.id]))
