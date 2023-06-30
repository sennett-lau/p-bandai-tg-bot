from .hub import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Filters, CallbackQueryHandler, ConversationHandler

def monitor_item_broadcast(context):
    cache = all_cache()
    unmonitor_keys = []

    for key in cache:
        if cache[key]:
            key_id, item_id = key.split('::')
            item = get_item_availability(item_id)

            if item['is_available']:
                item_url = get_item_url(item_id)

                keyboard = [
                    [InlineKeyboardButton("Buy", url=item_url)],
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                text = 'Product {} is available!'.format(item['name'])

                try:
                    context.bot.send_message(chat_id=key_id, text=text, reply_markup=reply_markup)
                except Exception as e:
                    print(e)

                set_cache(key, False)
                unmonitor_keys.append(key)
            else:
                print('Product {} is not available.'.format(item['name']))
                pass

    m = MongoLink()
    m.mass_deactivate_monitor_items(unmonitor_keys)

    pass



