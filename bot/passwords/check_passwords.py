from bot.bot_init import *
from bot import util
from bot.config import BotCallbackData
from passwords import generate_password


@bot.callback_query_handler(func=lambda message: message.data.startswith(BotCallbackData.CHOSE_PASS[:-2]))
def get_priv_key(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)
    db_util.set_user_data(chat_id=chat_id,
                          key=UserSessionKeys.PASSWORD_TITLE,
                          value=text[11:])
    schedule_message(chat_id=chat_id,
                     title_message=BotMessageTitles.INPUT_PRIV_KEY,
                     method=print_password,
                     reply_markup=markup.clear_markup())


def print_password(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)
    delete_message(chat_id=chat_id,
                   message_id=message_id)
    try:
        status, password = db_util.get_password(chat_id=chat_id,
                                                private_key=text)
    except Exception as e:
        logger.error(Logs.Error.GET_PASSWORD.format(chat_id))
        send_message(chat_id=chat_id,
                     title_message=BotMessageTitles.ERROR_IN_GETTING_PASS,
                     reply_markup=markup.main_menu(chat_id=chat_id))

    else:
        if status:
            msg = send_message(chat_id=chat_id,
                               title_message=BotMessageTitles.PRINT_PASSWORD,
                               format_args=password,
                               reply_markup=markup.main_menu(chat_id=chat_id))
            delay_delete(chat_id=chat_id,
                         message_id=msg.message_id,
                         delay=Constants.SECONDS_TO_DELETE_MSG)
        else:
            send_message(chat_id=chat_id,
                         title_message=password,
                         reply_markup=markup.main_menu(chat_id=chat_id))


