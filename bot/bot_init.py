from telebot import TeleBot
from telebot.types import BotCommand, Message, CallbackQuery
from bot.config import Constants, Logs, BotMessageTitles, BotButtonTitles
from typing import Union
from database import util as db_util
from database.config import UserSessionKeys
from logs import logger


bot = TeleBot(token=Constants.TOKEN,
              parse_mode='html')


bot.set_my_commands([BotCommand(command_title, command_description) for command_title, command_description in Constants.COMMANDS.items()])


def get_info_from_message(message: Union[Message, CallbackQuery]) -> tuple[int, str, int]:
    """
        for get little data from message
    :param message: message or callback object
    :return: user chat id, message text, message id
    """
    if isinstance(message, Message):
        if message.content_type != 'text':
            return message.from_user.id, message.caption, message.message_id
        else:
            return message.from_user.id, message.text, message.message_id
    else:
        return message.from_user.id, message.data, message.message.message_id


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
    except Exception as e:      # если бота заблокировали
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


def start_bot():
    logger.success(Logs.Success.BOT_WAS_STARTED)
    bot.polling()
