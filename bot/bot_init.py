from threading import Thread
from time import sleep

from telebot import TeleBot
from telebot.types import BotCommand, Message, CallbackQuery
from bot.config import Constants, Logs, BotMessageTitles, BotButtonTitles
from typing import Union
from database import util as db_util
from database.config import UserSessionKeys
from logs import logger
from bot import markup
from database.validators import Validator


bot = TeleBot(token=Constants.TOKEN,
              parse_mode='html',
              skip_pending=True)


bot.set_my_commands([BotCommand(command_title, command_description) for command_title, command_description in Constants.COMMANDS.items()])
user_data = {}


def get_info_from_message(message: Union[Message, CallbackQuery]) -> tuple[int, str, int]:
    """
        for get little data from message
    :param message: message or callback object
    :return: user chat id, message text, message id
    """
    if isinstance(message, CallbackQuery):
        logger.info(Logs.Info.USER_WRITE.format(message.from_user.id,
                                                message.data))
    else:
        if 'END RSA' not in message.text:
            logger.info(Logs.Info.USER_WRITE.format(message.from_user.id,
                    message.caption if message.content_type != 'text' else message.text))

    if isinstance(message, Message):
        if message.content_type != 'text':
            return message.from_user.id, message.caption, message.message_id
        else:
            return message.from_user.id, message.text, message.message_id
    else:
        return message.from_user.id, message.data, message.message.message_id


def send_message(chat_id: int, title_message: str, lang: str = '', reply_markup=None, format_args: Union[str, list, tuple] = [], delay: int = 0):
    """
        For DRY and faster acces to bot.send_message
    :param delay: for send message in new thread and able to delay send
    :param format_args: agrs for format message from db
    :param chat_id:
    :param title_message:
    :param lang:
    :param reply_markup:
    :return:
    """
    if isinstance(format_args, str):
        format_args = [format_args]

    message = {'chat_id': chat_id,
               'text': db_util.get_text(chat_id=chat_id,
                                        title_message=title_message,
                                        lang=lang)
                                        .format(*format_args)
                                        .replace('\\t', '\t')
                                        .replace('\\n', '\n'),
               'reply_markup': reply_markup,
               'parse_mode': 'html'}

    if delay:
        Thread(target=delay_send_message,
               kwargs={'message': message,
                       'delay': delay}).start()
    else:
        return bot.send_message(**message)


def delay_send_message(message: dict, delay: int = Constants.SECONDS_TO_SEND_MESSAGE_IN_THE_THREAD):
    sleep(delay)
    bot.send_message(**message)


def schedule_message(chat_id: int, title_message: str, method, lang:str = '', reply_markup=None):
    """
        for register next step (for low amount code)
    :param lang:
    :param title_message:
    :param chat_id: whom?
    :param text:    what?
    :param method:  method for get new message
    :param reply_markup:  keyboard
    :return:
    """
    try:
        msg = bot.send_message(chat_id=chat_id,
                               text=db_util.get_text(chat_id=chat_id,
                                                     title_message=title_message,
                                                     lang=lang),
                               reply_markup=reply_markup,
                               parse_mode='html')

    except Exception as e:      # if bot was blocked or other causes
        logger.error(Logs.Error.CANT_SAND_WITH_REGISTER.format(e))

    else:
        bot.register_next_step_handler(msg, method)


def delete_message(chat_id: int,
                   message_id: int):
    """
        Delete message with check on block
    :param chat_id:
    :param message_id:
    :return:
    """
    try:
        bot.delete_message(chat_id=chat_id,
                           message_id=message_id)

    except Exception as e:
        logger.error(Logs.Error.CANT_DELETE_MESSAGE.format(e))


def query_hangler(message, button_title: str) -> bool:
    """
        For decorators and decrease amount code
    :param button_title: button code
    :param message: message object
    :return:
    """
    if isinstance(message, Message):
        text = message.text
    else:
        text = message.data

    user_button = db_util.get_text(chat_id=message.from_user.id,
                                   title_message=button_title)
    return True if text == user_button else False


def delay_delete(chat_id: int, message_id: int, delay: int = 10):

    def schedule_delete():
        sleep(delay)
        delete_message(chat_id=chat_id,
                       message_id=message_id)

    Thread(target=schedule_delete).start()


def start_bot():
    logger.success(Logs.Success.BOT_WAS_STARTED)
    bot.polling()
