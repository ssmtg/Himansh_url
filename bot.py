#!/usr/bin/env python3


"""Importing"""
# Importing External Packages
from pyrogram import Client, idle

# Importing Inbuilt Packages
import logging
from os import path, makedirs, remove

# Importing Credentials & Required Data
try:
    from testexp.config import Config
except ModuleNotFoundError:
    from config import Config


'''For Displaying Errors&Warnings Better'''
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# No task on staring bot
try:
    remove('task.txt')
except FileNotFoundError:
    pass

"""Starting Bot"""
if __name__ == "__main__" :
    # Creating download directories, if they does not exists
    if not path.isdir(Config.DOWNLOAD_LOCATION):
        makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "URL_Uploader",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    print('Bot is Started!')
    app.run()
