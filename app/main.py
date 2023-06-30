import os

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

from commands.hub import *
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

    # set up item monitoring
    set_up_item_monitoring()

    updater = Updater(TOKEN, use_context=True, workers=6)

    dp = updater.dispatcher

    # Command handler
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("monitor", monitor))
    dp.add_handler(CommandHandler("unmonitor", unmonitor))

    # Message handler

    # Conversation handler

    # Scheduled tasks
    j = updater.job_queue
    j.run_repeating(monitor_item_broadcast, interval=10, first=0)

    # Error handler
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

'''
'''