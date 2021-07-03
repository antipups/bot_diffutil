from os import environ
from loguru import logger
from time import sleep


class Constants:
    try:
        TOKEN = environ['tg_token']
    except KeyError:
        logger.error('No token in environment variables')
        sleep(1)
        input('\nPress any key to exit...')
        quit()

    class Commands:
        """
            Commands for bot
        """
        START = ['start', 'старт']

    COMMANDS = {Commands.START[0]: 'Start menu',}
    AMOUNT_LANGS_IN_ROW = 3


class BotButtonTitles:
    """
        Button codes
    """
    BACK = 'back'

    class MainMenu:
        PASSWORD_GENERATOR = 'password_generator'
        MAIN_SETTINGS = 'main_settings'

    class Passwords:
        CREATE_PASSWORD = 'create_password'

    class Settings:
        LANGUAGE = 'language'


class BotMessageTitles:
    """
        Message codes
    """

    GET_LANG = 'get_lang'
    CHOISE_FROM_KEY = 'choise_from_key'
    SET_LANG = 'success_set_lang'
    MAIN_MENU = 'main_menu'
    SETTINGS = 'settings'


class Keyboards:
    """
        Keyboards, structure list - rows, list in list - buttons in rows
    """

    class Menu:
        """
            Bot menus
        """

        START = [[BotButtonTitles.MainMenu.PASSWORD_GENERATOR, BotButtonTitles.MainMenu.MAIN_SETTINGS]]
        SETTINGS = [[BotButtonTitles.Settings.LANGUAGE],
                    [BotButtonTitles.BACK]]


class Logs:
    """
        Logs =)
    """

    class Success:
        BOT_WAS_STARTED = 'Bot was started.'

    class Error:
        CANT_SAND_WITH_REGISTER = 'Can\'t send message with registration step because - *{}*'
        CANT_DELETE_MESSAGE = 'Can\'t delete message because - *{}*'

