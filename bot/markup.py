from telebot.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from database import util as db_util
from bot import util
from bot.config import Keyboards


def _reply_menu(keyboard) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    for row in keyboard:
        button_row = [KeyboardButton(text=button_title) for button_title in row]
        markup.add(*button_row)

    return markup


def main_menu(chat_id: int) -> ReplyKeyboardMarkup:
    return _reply_menu(keyboard=util.keyboard_on_user_language(chat_id=chat_id,
                                                               keyboard=Keyboards.Menu.START))


def languages() -> ReplyKeyboardMarkup:
    return _reply_menu(keyboard=util.languages_for_markup(langs=db_util.get_languages()))


def settings_menu(chat_id: int) -> ReplyKeyboardMarkup:
    return _reply_menu(keyboard=util.keyboard_on_user_language(chat_id=chat_id,
                                                               keyboard=Keyboards.Menu.SETTINGS))


def passwords_menu(chat_id: int) -> ReplyKeyboardMarkup:
    return _reply_menu(keyboard=util.keyboard_on_user_language(chat_id=chat_id,
                                                               keyboard=Keyboards.Menu.PASSWORDS))


def available_pass_lens() -> ReplyKeyboardMarkup:
    return _reply_menu(keyboard=Keyboards.Passwords.LENS)


def cyrillic(chat_id: int) -> ReplyKeyboardMarkup:
    return _reply_menu(keyboard=util.keyboard_on_user_language(chat_id=chat_id,
                                                               keyboard=Keyboards.Passwords.CYR))


def spec_symbols(chat_id: int) -> ReplyKeyboardMarkup:
    return _reply_menu(keyboard=util.keyboard_on_user_language(chat_id=chat_id,
                                                               keyboard=Keyboards.Passwords.SPEC))


def wanna_save(chat_id: int) -> ReplyKeyboardMarkup:
    return _reply_menu(keyboard=util.keyboard_on_user_language(chat_id=chat_id,
                                                               keyboard=Keyboards.Passwords.SAVE))
