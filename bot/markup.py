from telebot.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from database import util as db_util
from bot import util
from bot.config import Keyboards


def main_menu(chat_id: int) -> ReplyKeyboardMarkup:

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    for row in util.keyboard_on_user_language(chat_id=chat_id,
                                              keyboard=Keyboards.Menu.START):
        button_row = [KeyboardButton(text=button_title) for button_title in row]
        markup.add(*button_row)

    return markup


def languages() -> ReplyKeyboardMarkup:

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    for row in util.languages_for_markup(langs=db_util.get_languages()):
        button_row = [KeyboardButton(text=button_title) for button_title in row]
        markup.add(*button_row)

    return markup
