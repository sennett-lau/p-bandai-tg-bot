import logging
import sys

from telegram.ext import ConversationHandler

from .module_mongo import MongoLink
from .module_cache import set_cache

sys.path.append('..')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def end(update):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
    return ConversationHandler.END

def set_up_item_monitoring():
    m = MongoLink()

    items = m.get_monitor_items()

    for item in items:
        set_cache(item['combined_id'], item['monitor'])
    pass

def combined_id_decode(combined_id):
    return {
        'key_id': combined_id.split('::')[0],
        'item_id': combined_id.split('::')[1],
    }
