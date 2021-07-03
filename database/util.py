from database.models import *
from database.config import Logs, UserSessionKeys
from logs import logger


def get_languages() -> tuple:
    """
        Get all langs from base
    :return:
    """
    langs = Languages.select(Languages.title).tuples()
    return tuple(langs)


def add_user(chat_id: int, name: str):
    """
        Create/register new user in db
    :param chat_id:
    :param name:
    :return:
    """

    user = Users(id=chat_id,
                 name=name)
    user.save(force_insert=True)
    Sessions(user=user,
             session={}).save(force_insert=True)


def set_language(chat_id: int, title_language: str):
    """
        Setup language to user
    :param chat_id:
    :param title_language:
    :return:
    """
    set_user_data(chat_id=chat_id,
                  key=UserSessionKeys.LANG,
                  value=Languages.get(title=title_language).code_in_tg)


def set_user_data(chat_id: int, key: str, value: str) -> dict:
    """
        Get or Create session for new user
    :param chat_id:
    :param key:
    :param value:
    :return:
    """
    if session := Sessions.get_or_none(user=Users.get(id=chat_id)):
        session.session.update({key: value})
        session.save()
    else:
        session = Sessions(user=Users.get(tg_id=chat_id),
                           session={key: value})
        session.save(force_insert=True)

    return session.session


def get_text(chat_id: int, title_message: str, lang: str = '') -> str:
    """
        Get message for user
    :param title_message: title need message
    :param chat_id: user id, which we get language
    :param lang: lang if not set lang in session
    :return:
    """

    if not lang:
        lang = Sessions.get(user=Users.get(id=chat_id)).session.get(UserSessionKeys.LANG)

    return BotMessages.get(lang=Languages.get(code_in_tg=lang),
                           title=title_message).text


def get_text_code(chat_id: int, text: str) -> str:
    """
        Get code of text
    :param chat_id:
    :param text: text in botmessages
    :return: text title
    """

    lang = Sessions.get(user=Users.get(id=chat_id)).session.get(UserSessionKeys.LANG)
    if code := BotMessages.get_or_none(BotMessages.lang == Languages.get(code_in_tg=lang),
                                       BotMessages.text == text):
        return code.title

    else:
        return ''


def get_user_data(chat_id: int, code: str) -> str:
    """
        Get user data from db
    :param code:
    :param chat_id:
    :return: value of session code
    """
    if session := Sessions.get_or_none(user=chat_id).session:
        return session.session.get(code)


