from telethon.tl.types import InputPeerChat, MessageActionChatAddUser
import pickle
import random
import time
import json
import traceback
from telethon import TelegramClient, events, sync
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, MessageActionChatDeleteUser

from telethon.errors import UserPrivacyRestrictedError, PeerFloodError
from telethon.tl.functions.channels import DeleteMessagesRequest, InviteToChannelRequest

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
chat = client.get_entity("https://t.me/joinchat/sP7qisaaa4k5NDFk")

chat_id = chat.id
channel = InputPeerChannel(chat.id, chat.access_hash)

for message in client.iter_messages(chat):
    ...  # do something with the message from recent to older
    print((message))
    if isinstance(message.action, MessageActionChatDeleteUser) or isinstance(message.action, MessageActionChatAddUser):
        result = client(DeleteMessagesRequest(channel, [message.id]))
    

