from telebot.types import Message
from bot.bot_init import *
from bot import util
from bot import markup
from database.validators import Validator


@bot.message_handler(commands=Constants.Commands.START)
def start_menu(message: Message = None, chat_id: int = None):
    chat_id, text, message_id = get_info_from_message(message=message)
    if Validator.check_user(chat_id=chat_id):

        bot.send_message(chat_id=chat_id,
                         text=db_util.get_text(chat_id=chat_id,
                                               title_message=BotMessageTitles.MAIN_MENU),
                         reply_markup=markup.main_menu(chat_id=chat_id))

    else:
        db_util.add_user(chat_id=chat_id,
                         name=message.from_user.first_name)
        schedule_message(chat_id=chat_id,
                         title_message=BotMessageTitles.GET_LANG,
                         lang=message.from_user.language_code,
                         method=setup_language,
                         reply_markup=markup.languages())


def setup_language(message: Message):
    """
        Setup language
    :param message: language title
    :return:
    """
    chat_id, text, message_id = get_info_from_message(message=message)

    if Validator.check_language(lang_title=text):
        db_util.set_language(chat_id=chat_id,
                             title_language=text)

        bot.send_message(chat_id=chat_id,
                         text=db_util.get_text(chat_id=chat_id,
                                               title_message=BotMessageTitles.SET_LANG))

        bot.send_message(chat_id=chat_id,
                         text=db_util.get_text(chat_id=chat_id,
                                               title_message=BotMessageTitles.MAIN_MENU),
                         reply_markup=markup.main_menu(chat_id=chat_id))

    else:
        schedule_message(chat_id=chat_id,
                         title_message=BotMessageTitles.CHOISE_FROM_KEY,
                         lang=message.from_user.language_code,
                         method=setup_language,
                         reply_markup=markup.languages())
