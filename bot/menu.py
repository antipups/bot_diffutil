from bot.bot_init import *
from bot import util
from bot import markup


def register_lang_markup(chat_id: int, lang_code: str = '', redirect: bool = False):
    """
        DRY for wait lang markup
    :param lang_code: if first time setup
    :param redirect: if user choise not correct button
    :param chat_id:
    :return:
    """

    schedule_message(chat_id=chat_id,
                     title_message=BotMessageTitles.GET_LANG if not redirect else BotMessageTitles.CHOISE_FROM_KEY,
                     lang=lang_code,
                     method=setup_language,
                     reply_markup=markup.languages())


@bot.message_handler(func=lambda message: message.text == Constants.Commands.START or
                                          query_hangler(message=message,
                                                        button_title=BotButtonTitles.TO_MAIN_MENU))
def start_menu(message: Message = None, chat_id: int = None):
    if message:
        chat_id, text, message_id = get_info_from_message(message=message)

    if Validator.check_user(chat_id=chat_id):

        bot.send_message(chat_id=chat_id,
                         text=db_util.get_text(chat_id=chat_id,
                                               title_message=BotMessageTitles.MAIN_MENU),
                         reply_markup=markup.main_menu(chat_id=chat_id))

    else:
        db_util.add_user(chat_id=chat_id,
                         name=message.from_user.first_name)
        register_lang_markup(chat_id=chat_id,
                             lang_code=message.from_user.language_code)


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

        start_menu(chat_id=chat_id)

    else:
        register_lang_markup(chat_id=chat_id,
                             redirect=True)
