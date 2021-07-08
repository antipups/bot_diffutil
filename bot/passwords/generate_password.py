from bot.bot_init import *
from bot import util
from passwords import generate_password


def register_password_length(chat_id: int, title_message: str = BotMessageTitles.PASS_LEN):
    """
        DRY for wait password len
    :param title_message: title of need message (example: for validation)
    """

    schedule_message(chat_id=chat_id,
                     title_message=title_message,
                     method=get_pass_len,
                     reply_markup=markup.available_pass_lens())


def register_get_symbols_type(chat_id: int, redirect: bool = False):
    """
        DRY for wait get type of symbols
    :param redirect: if user choise not correct button
    """

    schedule_message(chat_id=chat_id,
                     title_message=BotMessageTitles.WITH_CYR_AND_LAT if not redirect else BotMessageTitles.CHOISE_FROM_KEY,
                     method=get_symbols_type,
                     reply_markup=markup.cyrillic(chat_id=chat_id))


def register_get_spec_symbols(chat_id: int, redirect: bool = False):
    """
        DRY for wait get spec symbols
    :param redirect: if user choise not correct button
    """

    schedule_message(chat_id=chat_id,
                     title_message=BotMessageTitles.WITH_SPEC_OR_NOT if not redirect else BotMessageTitles.CHOISE_FROM_KEY,
                     method=get_spec_symbols,
                     reply_markup=markup.spec_symbols(chat_id=chat_id))


def register_save(chat_id: int, redirect: bool = False):
    """
        DRY for wait get spec symbols
    :param redirect: if user choise not correct button
    """

    schedule_message(chat_id=chat_id,
                     title_message=BotMessageTitles.WANNA_SAVE if not redirect else BotMessageTitles.CHOISE_FROM_KEY,
                     method=create_password_with_params,
                     reply_markup=markup.wanna_save(chat_id=chat_id))


def get_pass_len(message: Message):
    """
        Get length of generate password
    :param message:
    :return:
    """
    chat_id, text, message_id = get_info_from_message(message=message)

    result_validate = Validator.pass_len(length=text)

    if result_validate == 1:
        user_data[chat_id] = {UserSessionKeys.PASS_LEN: int(text)}
        register_get_symbols_type(chat_id=chat_id)
        return

    elif result_validate == 0:
        title_message = BotMessageTitles.LEN_NOT_IN_RANGE

    else:
        title_message = BotMessageTitles.LEN_NOT_A_NUMBER

    register_password_length(chat_id=chat_id,
                             title_message=title_message)


def get_symbols_type(message: Message):
    """
        Cyrylic or latin or both
    """
    chat_id, text, message_id = get_info_from_message(message=message)

    code = Validator.check_yes_or_no(chat_id=chat_id, answer=text)

    if code:
        user_data[chat_id].update({UserSessionKeys.PASS_CYR: code.title})
        register_get_spec_symbols(chat_id=chat_id)
    else:
        register_get_symbols_type(chat_id=chat_id,
                                  redirect=True)


def get_spec_symbols(message: Message):
    """
        Special symbol use or not
    """
    chat_id, text, message_id = get_info_from_message(message=message)

    code = Validator.check_yes_or_no(chat_id=chat_id, answer=text)

    if code:
        user_data[chat_id].update({UserSessionKeys.PASS_SPEC: code.title})
        # logger.debug(f'All data - {user_data}')
        register_save(chat_id=chat_id)

    else:
        register_get_spec_symbols(chat_id=chat_id,
                                  redirect=True)


def generate_pass_and_send_it(chat_id: int):
    """
        Generate pass and sent it at once, after, delete
    :param chat_id:
    :return:
    """

    password = generate_password.get_data_for_generate_password(user_data[chat_id])

    msg = send_message(chat_id=chat_id,
                       title_message=BotMessageTitles.PASSWORD_WAS_CREATED,
                       format_args=password,
                       reply_markup=markup.main_menu(chat_id=chat_id))

    delay_delete(chat_id=chat_id,
                 message_id=msg.message_id,
                 delay=Constants.SECONDS_TO_DELETE_MSG)


def create_password_with_params(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)

    if Validator.check_yes_or_no(chat_id=chat_id,
                                 answer=text):

        if text == BotButtonTitles.Passwords.GeneratePassword.SAVE:
            ...

        else:
            generate_pass_and_send_it(chat_id=chat_id)

    else:
        register_save(chat_id=chat_id,
                      redirect=True)
