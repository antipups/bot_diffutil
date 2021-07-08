from time import time
from random import choices
from logs import logger
from passwords.config import Constants


def password_generate(length: int, cyr: bool, spec: bool) -> str:
    need_symbols = Constants.SYMBOLS_TO_GENERATE

    if cyr:
        need_symbols += Constants.RUSSIAN_SYMBOLS

    if spec:
        need_symbols += Constants.SPEC_SYMBOLS

    return ''.join(choices(need_symbols, k=length))


def get_data_for_generate_password(data: dict) -> str:
    password: str = password_generate(length=data['pass_len'],
                                      cyr=True if data['pass_cyr'] == 'use_cyr' else False,
                                      spec=True if data['pass_spec'] == 'use_spec' else False)
    return password
