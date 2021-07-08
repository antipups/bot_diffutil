from bot.bot_init import *
from bot import util
from bot.passwords.generate_password import register_password_length


@bot.message_handler(func=lambda message: message.text == Constants.Commands.PASS or
                                          query_hangler(message=message,
                                                        button_title=BotButtonTitles.MainMenu.PASSWORD_GENERATOR))
def password_menu(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)
    send_message(chat_id=chat_id,
                 title_message=BotMessageTitles.PASSWORDS,
                 reply_markup=markup.passwords_menu(chat_id=chat_id))


@bot.message_handler(func=lambda message: message.text == Constants.Commands.MKPASS or
                                          query_hangler(message=message,
                                                        button_title=BotButtonTitles.Passwords.CREATE))
def create_password(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)
    register_password_length(chat_id=chat_id)


@bot.message_handler(func=lambda message: message.text == Constants.Commands.GETPASS or
                                          query_hangler(message=message,
                                                        button_title=BotButtonTitles.Passwords.CHECK))
def passwords_choise(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)
    print('check')
