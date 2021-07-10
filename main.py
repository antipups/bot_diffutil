from database import models
from bot import start_bot


if __name__ == '__main__':
    models.create_tables()
    # models.test()
    start_bot()
