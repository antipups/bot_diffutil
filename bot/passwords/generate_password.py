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
        user_data[chat_id].update({UserSessionKeys.PASS_CYR: code})
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
        user_data[chat_id].update({UserSessionKeys.PASS_SPEC: code})
        # logger.debug(f'All data - {user_data}')
        register_save(chat_id=chat_id)

    else:
        register_get_spec_symbols(chat_id=chat_id,
                                  redirect=True)


def generate_pass_and_send_it(chat_id: int, password_title: str = ''):
    """
        Generate pass and sent it at once, after, delete, if password_title - save password with need title
    :param chat_id:
    :param password_title:
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

    send_message(chat_id=chat_id,
                 title_message=BotMessageTitles.MAIN_MENU,
                 reply_markup=markup.main_menu(chat_id=chat_id),
                 delay=Constants.SECONDS_TO_DELETE_MSG - 1)

    if password_title:
        db_util.save_password(chat_id=chat_id,
                              password_title=password_title,
                              password=password)


def create_password_with_params(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)

    if text_title := Validator.check_yes_or_no(chat_id=chat_id,
                                               answer=text):

        if text_title == BotButtonTitles.Passwords.GeneratePassword.SAVE:
            check_key(chat_id=chat_id)

        else:
            generate_pass_and_send_it(chat_id=chat_id)

    else:
        register_save(chat_id=chat_id,
                      redirect=True)


def check_key(chat_id: int):
    key = db_util.get_pub_key(chat_id=chat_id)

    if not key:
        send_message(chat_id=chat_id,
                     title_message=BotMessageTitles.SECURITY_KEY_GEN,
                     reply_markup=markup.clear_markup(),
                     delay=Constants.SECONDS_TO_SEND_MESSAGE_IN_THE_THREAD)

        private_key = db_util.create_keys(chat_id=chat_id)

        msg = send_message(chat_id=chat_id,
                           title_message=BotMessageTitles.GENERATE_KEY,
                           format_args=private_key.decode('utf-8'))

        delay_delete(chat_id=chat_id,
                     message_id=msg.message_id,
                     delay=Constants.SECONDS_TO_DELETE_MSG_WITH_KEY)

    schedule_message(chat_id=chat_id,
                     title_message=BotMessageTitles.PASSWORD_TITLE,
                     method=save_password,
                     reply_markup=markup.back(chat_id=chat_id))


def save_password(message: Message):
    chat_id, text, message_id = get_info_from_message(message=message)

    if BotButtonTitles.BACK == db_util.get_text_code(chat_id=chat_id,
                                                     text=text):
        register_save(chat_id=chat_id)

    else:
        generate_pass_and_send_it(chat_id=chat_id,
                                  password_title=text)
