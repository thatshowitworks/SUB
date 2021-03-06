"""
A script to automatically spam files based on certain triggers by anyone in that chat.
 
This script assumes that you have certain files on the working directory,
such as "xfiles.m4a" or "anytime.png" for some of the automated replies.
"""
 
import os
import sys
import time
import logging
from config import Config
 
from telethon import TelegramClient, events
from telethon.sessions import StringSession
 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
 
 
 
triggerer = '.destroy'
stop = '.stop'
 
# Gif/Images
files = ['gif.gif', 'jj.mp4']
id = Config.api_id
hash = Config.api_hash
string = Config.string_session
 
@events.register(events.NewMessage)
async def handler(event):
    if event.raw_text.lower().startswith(triggerer):
        # for i in range(3): # use for loop for test
        while True:
            for file in files:
                await client.send_file(event.chat_id, file)
                if event.raw_text.lower().startswith(stop):
                            break
 
 
# Change StringSession as per your need
client = TelegramClient(StringSession(string), id, hash, proxy=None)
 
with client:
   # This remembers the events.NewMessage we registered before
   client.add_event_handler(handler)
 
   print('(Press Ctrl+C to stop this or do .stop in a chat)')
   client.run_until_disconnected()
