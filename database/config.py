class Constants:
    DATABASE_INPUT_DATA = {'user': 'root',
                           'password': 'root',
                           'database': 'bot_different_utilities',
                           'charset': 'utf8mb4',
                           'host': 'db',
                           # 'host': 'localhost',
                           # 'max_connections': None,
                           'stale_timeout': 300
                           }

    MAX_PASS_LEN = 200
    MIN_PASS_LEN = 8

    POOLING_TIMEOUT = 30 * 60


class Logs:

    class Info:
        NEW_USER = 'New user - {}'

    class Error:
        POOLING = 'Pooling error - {}'

    class Success:
        POOLING = 'Pooling success'


class UserSessionKeys:
    LANG = 'lang'
    PASS_LEN = 'pass_len'
    PASS_CYR = 'pass_cyr'
    PASS_SPEC = 'pass_spec'
    PASSWORD_TITLE = 'password_title'
