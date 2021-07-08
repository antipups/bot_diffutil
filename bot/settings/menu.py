from bot.bot_init import *
from bot import util
from bot.menu import start_menu, register_lang_markup


@bot.message_handler(func=lambda message: message.text == Constants.Commands.SETTINGS or
                                          query_hangler(message=message, button_title=BotButtonTitles.MainMenu.MAIN_SETTINGS))
def settings_menu(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)
    send_message(chat_id=chat_id,
                 title_message=BotMessageTitles.SETTINGS,
                 reply_markup=markup.settings_menu(chat_id=chat_id))


@bot.message_handler(func=lambda message: message.text == Constants.Commands.LANG or
                                          query_hangler(message=message, button_title=BotButtonTitles.Settings.LANGUAGE))
def settings_choise(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)
    register_lang_markup(chat_id=chat_id)

