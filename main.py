from threading import Thread
from bot.websocket import start_server
# from database import models
from bot import start_bot
from database.util import pool_connection

if __name__ == '__main__':
    # models.create_tables()
    # models.test()
    # start_bot()
    Thread(target=pool_connection).start()
    start_server()
