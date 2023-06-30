def start(update, context):
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
    print('user_id: ' + str(user_id))
    # check if the chat is from a group
    if update.message.chat.type == 'group':
        group_id = update.message.chat.id
        print('group_id: ' + str(group_id))
    else:
        print('Not a group chat')

    context.bot.sendMessage(chat_id=chat_id, text='Hey there!', parse_mode='HTML')
