import pickle

from telethon import TelegramClient, events, sync
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

api_id = 3120783
api_hash = 'a2b170ac2835659a5e8f78e412fe835e'
client = TelegramClient('session_name', api_id, api_hash)
client.start()

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))

chats.extend(result.chats)

megagroups = []

for chat in chats:
    if hasattr(chat, 'megagroup') and chat.megagroup:
        megagroups.append(chat)


print(megagroups[0])
for megag in megagroups:
    # if megag.title == 'تحلیل بازارهای مالی':
        print('Fetching Members...')
        all_participants = []
        all_participants = client.get_participants(megag, aggressive=True)

        with open(str(megag.id) + "__" + megag.title + ".usrs", "wb") as fp:  # Pickling
            pickle.dump(all_participants, fp)

        print(len(all_participants))
