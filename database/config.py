class Constants:
    DATABASE_INPUT_DATA = {'user': 'root',
                           'password': 'root',
                           'database': 'bot_different_utilities',
                           'charset': 'utf8mb4'}

    MAX_PASS_LEN = 501
    MIN_PASS_LEN = 8


class Logs:
    class Info:
        NEW_USER = 'New user - {}'


class UserSessionKeys:
    LANG = 'lang'
    PASS_LEN = 'pass_len'
    PASS_CYR = 'pass_cyr'
    PASS_SPEC = 'pass_spec'
