import sys

sys.path.append('..')

from modules.hub import *


def monitor(update, context):
    if len(context.args) == 0:
        update.message.reply_text('Please enter the product code. e.g. /monitor N2457610001004')
        return
    elif len(context.args) > 1:
        update.message.reply_text('Please enter only one product code. e.g. /monitor N2457610001004')
        return
    else:
        message = context.bot.sendMessage(chat_id=update.message.chat.id, text='Processing...')

        item_id = context.args[0]

        key_id = update.message.chat.id if update.message.chat.type == 'group' else update.message.from_user.id

        item_availability = get_item_availability(item_id)

        if item_availability['name'] == '':
            context.bot.edit_message_text(chat_id=update.message.chat.id, message_id=message.message_id,
                                          text='Product not found.')
            return

        mongo_link = MongoLink()

        mongo_link.add_monitor_item(key_id, item_id)

        context.bot.edit_message_text(chat_id=update.message.chat.id, message_id=message.message_id,
                                      text='Product {} added to monitor list.'.format(item_availability['name']))
        return
    pass


def unmonitor(update, context):
    if len(context.args) == 0:
        update.message.reply_text('Please enter the product code. e.g. /unmonitor N2457610001004')
        return
    elif len(context.args) > 1:
        update.message.reply_text('Please enter only one product code. e.g. /unmonitor N2457610001004')
        return
    else:
        # show processing message
        message = context.bot.sendMessage(chat_id=update.message.chat.id, text='Processing...')

        item_id = context.args[0]

        key_id = update.message.chat.id if update.message.chat.type == 'group' else update.message.from_user.id

        mongo_link = MongoLink()

        data = mongo_link.get_monitor_item(key_id, item_id)

        if data is None:
            # update the processing message to show that the item is not being monitored
            context.bot.edit_message_text(chat_id=update.message.chat.id, message_id=message.message_id,
                                          text='Item is not being monitored.')
            return

        mongo_link.deactivate_monitor_item(key_id, item_id)

        context.bot.edit_message_text(chat_id=update.message.chat.id, message_id=message.message_id,
                                      text='Item is no longer being monitored.')
        return
    pass
