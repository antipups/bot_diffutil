from telebot.types import Message
from bot.bot_init import *
from bot import util
from bot import markup
from bot.menu import start_menu, register_lang_markup


def register_settings_markup(chat_id: int, redirect: bool = False):
    """
        DRY for wait settings markup
    :param redirect: if user choise not correct button
    :param chat_id:
    :return:
    """

    schedule_message(chat_id=chat_id,
                     title_message=BotMessageTitles.SETTINGS if not redirect else BotMessageTitles.CHOISE_FROM_KEY,
                     method=settings_choise,
                     reply_markup=markup.settings_menu(chat_id=chat_id))


@bot.message_handler(func=lambda message: query_hangler(message=message, button_title=BotButtonTitles.MainMenu.MAIN_SETTINGS))
def settings_menu(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)
    register_settings_markup(chat_id=chat_id)


def settings_choise(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)

    if text := db_util.get_text_code(chat_id=chat_id,
                                     text=text):
        if text == BotButtonTitles.BACK:
            start_menu(chat_id=chat_id)

        elif text == BotButtonTitles.Settings.LANGUAGE:
            register_lang_markup(chat_id=chat_id)

    else:
        register_settings_markup(chat_id=chat_id,
                                 redirect=True)
