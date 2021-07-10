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

    @staticmethod
    def pass_len(length: str) -> int:
        """
            Check correct input length, if:
                not number return -1
                not in range return 0

            else: True
        :param length:
        :return:
        """
        if length.replace('-', '').isdigit():
            if Constants.MIN_PASS_LEN <= int(length) <= Constants.MAX_PASS_LEN:
                return 1
            else:
                return 0
        else:
            return -1

    @staticmethod
    def check_yes_or_no(chat_id: int, answer: str) -> str:
        """
            Check valid answer, and return title of answer
        :param chat_id:
        :param answer:
        :return:
        """
        lang = Sessions.get(user=chat_id).session.get(UserSessionKeys.LANG)
        return BotMessages.get_or_none(lang=Languages.get(Languages.code_in_tg == lang),
                                       text=answer).title

