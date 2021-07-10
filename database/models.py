import json
from peewee import *
from database.config import *


db = MySQLDatabase(**Constants.DATABASE_INPUT_DATA)


class BaseModel(Model):
    """
        Инициализация базовой модели с прикрепленнём конекшином
    """
    class Meta:
        database = db


class Users(BaseModel):
    """
        Users which use bot
    """
    class Meta:
        primary_key = False

    id = IntegerField(primary_key=True,
                      help_text='ID in telegram')
    name = CharField(max_length=64)


class Keys(BaseModel):
    """
        Keys which belong to users
    """
    class Meta:
        primary_key = False

    user = ForeignKeyField(Users,
                           on_delete='CASCADE',
                           on_update='CASCADE',
                           primary_key=True)
    key = BlobField(help_text='Public key for user')


class JSONField(BlobField):
    """
        Custom field for JSON serialize + additional protect in bytes (blob field)
    """

    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)


class Sessions(BaseModel):
    """
        Sessions every user, for don't forget user history after reload bot
    """

    class Meta:
        primary_key = False

    user = ForeignKeyField(Users,
                           on_delete='CASCADE',
                           on_update='CASCADE',
                           primary_key=True)

    session = JSONField(help_text='Session user data')


class Passwords(BaseModel):
    """
        User Passwords in Encrypted Format
    """

    user = ForeignKeyField(Users,
                           on_delete='CASCADE',
                           on_update='CASCADE')

    title = CharField(help_text='password title')
    encrypted_password = BlobField(help_text='encrypted user password')


class Languages(BaseModel):
    """
        Languages in project
    """
    code_in_tg = CharField(max_length=2,
                           unique=True,
                           help_text='language code in tg')
    title = CharField(max_length=16,
                      unique=True,
                      help_text='language title')


class BotMessages(BaseModel):
    """
        Model for other text messages for bot on other languages
    """

    title = CharField(max_length=128,
                      help_text='message title for get message from bot')
    lang = ForeignKeyField(Languages,
                           on_delete='CASCADE',
                           on_update='CASCADE',)
    text = CharField(max_length=1024,)


def create_tables():
    Users.create_table()
    Keys.create_table()
    Sessions.create_table()
    Passwords.create_table()
    Languages.create_table()
    BotMessages.create_table()


def test():
    ...
