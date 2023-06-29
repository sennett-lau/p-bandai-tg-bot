import os

from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler

from modules.hub import *

load_dotenv()

APP_ENV = os.getenv('APP_ENV') # prd / dev
TOKEN = os.environ.get("TOKEN")
PORT = int(os.environ.get("PORT", "8443"))

def main():
    print('=======================================================')
    if APP_ENV != 'prd':
        print('Testing Environment...')
    else:
        print('Product Environment...')
    print('=======================================================')
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True, workers=6)

    dp = updater.dispatcher

    # Command handler

    # Message handler

    # Conversation handler

    # Error handler
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

'''
'''