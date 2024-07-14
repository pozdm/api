import os
import configparser

_config = configparser.ConfigParser()
_config.read("config.ini", encoding="utf-8")


def _get_from_config_or_env(section: str, key: str) -> str:
    result = _config[section][key]
    if not result:
        return os.environ[f"{section}:{key}"]
    return result


DEVELOPERS = list(map(int, _get_from_config_or_env("table", "developers").split(", ")))
# TELEGRAM_TOKEN = _get_from_config_or_env("bot", "telegram_token")
# ADMIN_TELEGRAM_ID = int(_get_from_config_or_env("bot", "admin_telegram_id"))
# ADMIN_TELEGRAM_ID_2 = int(_get_from_config_or_env("app", "admin_telegram_id_2"))
# ADMIN_TELEGRAM_ID_3 = int(_get_from_config_or_env("app", "admin_telegram_id_3"))
# ADMIN_TELEGRAM_ID_4 = int(_get_from_config_or_env("app", "admin_telegram_id_4"))
# EGS = _get_from_config_or_env("egs", "token")
SA_URL = _get_from_config_or_env("db", "sa_url")
# PG_URL = _get_from_config_or_env("db", "test_url")
# YAZZH_URL = _get_from_config_or_env("db", "yazzh_url")
# CLICKHOUSE_URL = _get_from_config_or_env("db", "clickhouse_url")
# CLICKHOUSE_USER = _get_from_config_or_env("db", "clickhouse_user")
# CLICKHOUSE_PASSWORD = _get_from_config_or_env("db", "clickhouse_password")
# CLICKHOUSE_DATABASE = _get_from_config_or_env("db", "clickhouse_database")
# CHECK = _get_from_config_or_env("table", "check")
# UPDATE_DB = _get_from_config_or_env("table", "update_db")
MYPETSOWNERS = _get_from_config_or_env("table", "mypets_owners")
DOU = _get_from_config_or_env("table", "dou")
API = _get_from_config_or_env("table", "api")
VK = _get_from_config_or_env("table", "vk")
CHATS_COUNT = _get_from_config_or_env("table", "chats_count")
CHATS_USERS_COUNT = _get_from_config_or_env("table", "chats_users_count")
# TESTRESULT = _get_from_config_or_env("table", "testresult")
# TESTSTATUS = _get_from_config_or_env("table", "teststatus")
# TESTLAUNCH = _get_from_config_or_env("table", "testlaunch")
# TESTLAUNCHSTAT = _get_from_config_or_env("table", "testlaunchstat")
# TESTSESSION = _get_from_config_or_env("table", "testsession")
# TESTSESSIONENV = _get_from_config_or_env("table", "testsessionenv")
# ENVVARVAL = _get_from_config_or_env("table", "envvarval")
# ENVVAR = _get_from_config_or_env("table", "envvar")
# PG_URL_USERS = _get_from_config_or_env("db", "pg_url_users")

# LIST_API = _get_from_config_or_env("api", "list_api")