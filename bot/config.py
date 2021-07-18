from os import environ
from loguru import logger
from time import sleep


class Constants:
    try:
        TOKEN = environ['TG_TOKEN']
    except KeyError:
        logger.error('No token in environment variables')
        sleep(1)
        input('\nPress any key to exit...')
        quit()

    """
        Commands for bot
    """
    class Commands:
        START = '/start'
        PASS = '/pass'
        MKPASS = '/mkpass'
        GETPASS = '/getpass'
        SETTINGS = '/settings'
        LANG = '/lang'

    COMMANDS = {Commands.START: 'Start menu',
                Commands.PASS: 'Passwords menu',
                Commands.MKPASS: 'Generate password',
                Commands.GETPASS: 'Check passwords',
                Commands.SETTINGS: 'Settings',
                Commands.LANG: 'Language',
                }

    AMOUNT_LANGS_IN_ROW = 3

    SECONDS_TO_DELETE_MSG = 10
    SECONDS_TO_DELETE_MSG_WITH_KEY = 30
    SECONDS_TO_SEND_MESSAGE_IN_THE_THREAD = 1


class BotButtonTitles:
    """
        Button codes
    """
    BACK = 'back'
    TO_MAIN_MENU = 'to_main_menu'

    class MainMenu:
        PASSWORD_GENERATOR = 'password_generator'
        MAIN_SETTINGS = 'main_settings'

    class Passwords:
        CREATE = 'create_password'
        CHECK = 'check_passwords'

        class GeneratePassword:
            USE_CYR = 'use_cyr'
            NO_CYR = 'no_cyr'

            USE_SPEC = 'use_spec'
            NO_SPEC = 'no_spec'

            SAVE = 'do_save'
            NOT_SAVE = 'not_save'

    class Settings:
        LANGUAGE = 'language'


class BotMessageTitles:
    """
        Message codes
    """

    MAIN_MENU = 'main_menu'

    CHOISE_FROM_KEY = 'choise_from_key'

    SETTINGS = 'settings'
    GET_LANG = 'get_lang'
    SET_LANG = 'success_set_lang'

    PASSWORDS = 'passwords'

    PASS_LEN = 'get_pass_len'
    LEN_NOT_IN_RANGE = 'len_not_in_range'
    LEN_NOT_A_NUMBER = 'len_not_a_number'
    WITH_CYR_AND_LAT = 'with_cyr_and_lat'
    WITH_SPEC_OR_NOT = 'with_spec'
    WANNA_SAVE = 'wanna_save'
    PASSWORD_WAS_CREATED = 'password_was_created'

    PASSWORD_TITLE = 'password_title'
    GENERATE_KEY = 'generate_key'

    GET_PASS_TITLES = 'get_pass_titles'
    INPUT_PRIV_KEY = 'input_priv_key'
    ERROR_IN_GETTING_PASS = 'error_in_getting_pass'
    PRINT_PASSWORD = 'print_password'
    NOT_VALID_KEY = 'not_valid_key'
    SECURITY_KEY_GEN = 'security_key_gen'


class Keyboards:
    """
        Keyboards, structure list - rows, list in list - buttons in rows
    """
    BACK = [[BotButtonTitles.BACK]]

    class Passwords:
        LENS = [[16, 32, 64],
                [128, 176, 200]]
        CYR = [[BotButtonTitles.Passwords.GeneratePassword.USE_CYR, BotButtonTitles.Passwords.GeneratePassword.NO_CYR ]]
        SPEC = [[BotButtonTitles.Passwords.GeneratePassword.USE_SPEC, BotButtonTitles.Passwords.GeneratePassword.NO_SPEC ]]
        SAVE = [[BotButtonTitles.Passwords.GeneratePassword.SAVE, BotButtonTitles.Passwords.GeneratePassword.NOT_SAVE ]]

    class Menu:
        """
            Bot menus
        """

        START = [[BotButtonTitles.MainMenu.PASSWORD_GENERATOR, ],
                 [BotButtonTitles.MainMenu.MAIN_SETTINGS]]

        SETTINGS = [[BotButtonTitles.Settings.LANGUAGE],
                    [BotButtonTitles.TO_MAIN_MENU]]

        PASSWORDS = [[BotButtonTitles.Passwords.CREATE, BotButtonTitles.Passwords.CHECK],
                     [BotButtonTitles.TO_MAIN_MENU]]


class BotCallbackData:

    CHOSE_PASS = 'chose_pass_{}'


class Logs:
    """
        Logs =)
    """

    class Success:
        BOT_WAS_STARTED = 'Bot was started.'

    class Error:
        CANT_SAND_WITH_REGISTER = 'Can\'t send message with registration step because - *{}*'
        CANT_DELETE_MESSAGE = 'Can\'t delete message because - *{}*'
        GET_PASSWORD = 'Error in getting password. From user - {}'

    class Info:
        USER_WRITE = 'User "{}" write "{}"'

