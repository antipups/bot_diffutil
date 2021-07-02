from database.models import *


class Validator:
    """
        Class for validate something (check row in db and other)
    """

    @staticmethod
    def check_user(chat_id: int):
        return Users.get_or_none(Users.id == chat_id)

    @staticmethod
    def check_language(lang_title: str):
        return Languages.get_or_none(Languages.title == lang_title)

