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
    tg_id = IntegerField(unique=True,
                         help_text='ID in telegram')


class Keys(BaseModel):
    """
        Keys which belong to users
    """
    class Meta:
        primary_key = False

    user = ForeignKeyField(Users,
                           on_delete=Constants.ForeignTypeOfChange.CASCADE,
                           on_update=Constants.ForeignTypeOfChange.CASCADE,
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
                           on_delete=Constants.ForeignTypeOfChange.CASCADE,
                           on_update=Constants.ForeignTypeOfChange.CASCADE,
                           primary_key=True)

    session = JSONField(help_text='Session user data')


class Passwords(BaseModel):
    """
        User Passwords in Encrypted Format
    """

    user = ForeignKeyField(Users,
                           on_delete=Constants.ForeignTypeOfChange.CASCADE,
                           on_update=Constants.ForeignTypeOfChange.CASCADE,
                           primary_key=True)

    title = BlobField(help_text='encrypted password title')
    encrypted_password = BlobField(help_text='encrypted user password')


def create_tables():
    Users.create_table()
    Keys.create_table()
    Sessions.create_table()
    Passwords.create_table()
