import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from config import Config
# the Strings used for this "thing"
from style import Style

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    logger.info(update)
    await update.reply_text(
        text = Style.START_TEXT,
        quote = True
    )

    
