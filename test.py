
from telethon import TelegramClient, events, sync
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser

api_id = 95576
api_hash = '0bcee09d8c8beb2e7c0d52ce4c1ef594'
client = TelegramClient('session_name', api_id, api_hash)
client.start()
# client.send_file('@Javadyasemi', "F:\\Pictures\\patterns\\2020\\Oct\\Screenshot 2020-11-24 121604.jpg",caption="ha ha ha ha i am sender fuck u javad")
# client.send_message(, "پس چگونه به او کافر میشووی حتی بات ها نیز در برابر او سر تسلیم فرود اورده اند")

client(InviteToChannelRequest("@quantomfx",[InputPeerUser("114637215")]))

# for  dialog in client.iter_dialogs():
#     print(dialog.name, 'has ID', dialog.id)
#     # You can, of course, use markdown in your messages:
#     message = client.send_message(
#         'me',
#         'This message has **bold**, `code`, __italics__ and '
#         'a [nice website](https://example.com)!',
#         link_preview=False
#     )
#
#     # Sending a message returns the sent message object, which you can use
#     print(message.raw_text)
#
#     # You can reply to messages directly if you have a message object
#     message.reply('Cool!')
#     break