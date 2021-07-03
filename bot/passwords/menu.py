from telebot.types import Message
from bot.bot_init import *
from bot import util
from bot import markup
from database.validators import Validator


@bot.message_handler(func=lambda message: query_hangler(message=message, button_title=BotButtonTitles.MainMenu.PASSWORD_GENERATOR))
def password_menu(message: Message):
    ...
