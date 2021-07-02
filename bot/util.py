from bot.bot_init import *
from bot.config import Keyboards


def languages_for_markup(langs: tuple) -> list:
    """
        Prepare to output keyboard with need amount button on row
    :param langs:
    :return:
    """
    langs = [lang[0] for lang in langs]
    return [tuple(langs[iterator: iterator + Constants.AMOUNT_LANGS_IN_ROW])
            for iterator in range(0,
                                  len(langs),
                                  Constants.AMOUNT_LANGS_IN_ROW)]


def keyboard_on_user_language(chat_id: int, keyboard: list) -> list:
    """
        Get keyboard in need language
    :param chat_id:
    :param keyboard:
    :return:
    """
    return [tuple(db_util.get_text(chat_id=chat_id,
                                   title_message=button) for button in row) for row in keyboard]
