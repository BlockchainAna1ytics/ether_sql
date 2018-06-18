import os

# Task queue settings
REDIS_URL = "redis://localhost:6379/0"
CELERY_BROKER = REDIS_URL
CELERY_BACKEND = CELERY_BROKER
CELERYD_TASK_SOFT_TIME_LIMIT = 60
CELERYD_TASK_TIME_LIMIT = 120
CELERYD_LOG_FORMAT = '[%(asctime)s][PID:%(process)d][%(levelname)s][%(processName)s] %(message)s'
CELERYD_TASK_LOG_FORMAT = '[%(asctime)s][PID:%(process)d][%(levelname)s][%(processName)s] task_name=%(task_name)s taks_id=%(task_id)s %(message)s'


class DefaultSettings():
    # SQLALCHEMY settings
    SQLALCHEMY_USER = os.environ.get("USER")
    # password that is set when creating psql user
    SQLALCHEMY_PASSWORD = 'develop'
    SQLALCHEMY_DB = 'ether_sql'
    SQLALCHEMY_HOST = 'localhost'
    SQLALCHEMY_PORT = 5432

    # Logging settings
    LOG_STDOUT = "TRUE"
    LOG_FORMAT = "[%(asctime)s][%(levelname)s][%(name)s] %(message)s"
    LOG_LEVEL = "INFO"

    # Node settings
    # Available options 'Geth', 'Parity', 'Infura'
    NODE_TYPE = "Infura"
    NODE_URL = 'https://mainnet.infura.io/'
    # Tables to parse
    # Use this option to parse traces, needs parity with cli --tracing=on
    PARSE_TRACE = False
    PARSE_STATE_DIFF = False


class PersonalInfuraSettings(DefaultSettings):
    NODE_TYPE = "Infura"
    NODE_API_TOKEN = ""  # your infura api_token
    NODE_URL = 'https://mainnet.infura.io/{}'.format(NODE_API_TOKEN)


class PersonalParitySettings(DefaultSettings):
    NODE_TYPE = "Parity"
    PARSE_TRACE = True
    PARSE_STATE_DIFF = True


class PersonalGethSettings(DefaultSettings):
    NODE_TYPE = "Geth"


class TestSettings(DefaultSettings):
    # SQLALCHEMY settings
    SQLALCHEMY_DB = 'ether_sql_tests'

    # Logging settings
    LOG_LEVEL = "DEBUG"


class ParityTestSettings(TestSettings):

    # Node settings
    # Available options 'Geth', 'Parity', 'Infura'
    NODE_TYPE = "Parity"

    # Tables to parse
    # Use this option to parse traces, needs parity with cli --tracing=on
    PARSE_TRACE = True


SETTINGS_MAP = {'DefaultSettings': DefaultSettings,
                'TestSettings': TestSettings,
                'ParityTestSettings': ParityTestSettings,
                'PersonalInfuraSettings': PersonalInfuraSettings,
                'PersonalParitySettings': PersonalParitySettings,
                'PersonalGethSettings': PersonalGethSettings}
