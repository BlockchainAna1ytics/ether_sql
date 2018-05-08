import logging
import settings
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import sys
from ethjsonrpc import EthJsonRpc, ParityEthJsonRpc, InfuraEthJsonRpc
from ether_sql.models import base

logger = logging.getLogger(__name__)


def setup_logging():
    """
    Add logging format to logger used for debugging and info
    """

    handler = logging.StreamHandler(sys.stdout if settings.LOG_STDOUT else sys.stderr)
    formatter = logging.Formatter(settings.LOG_FORMAT)
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(settings.LOG_LEVEL)


def setup_db_session(user, password, db, host='localhost', port=5432):
    """
    Connects to the psql database given its parameters and returns the
    connection session

    We connect with the help of the PostgreSQL URL
    example url--> postgresql://federer:grandestslam@localhost:5432/tennis
    inspired from: https://suhas.org/sqlalchemy-tutorial/

    :param user: user who owns the database
    :param password: password if needed to unlock this database
    :param host: host port to connect to this database
    :param db: name of the database

    :return: The connection to the database
    """

    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # Create an engine that stores data in the PostgreSQL
    engine = sqlalchemy.create_engine(url, client_encoding='utf8')
    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    base.metadata.bind = engine

    # A DBSession() instance establishes all conversations with the database
    # and represents a "staging zone" for all the objects loaded into the
    # database session object. Any change made against the objects in the
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    logging.info('Connected to the db {}'.format(db))

    return session, engine


def setup_node_session(node_type, host='localhost', port=8545, api_token=''):
    """
    Connects to appropriate node using values specified in settings.py

    :param str node_type: Type of node, available options 'Parity', 'Geth' and 'Infura'
    :param str host: Name of host
    :param int port: Port number of the connection
    :param str api_token: Api token if needed
    """

    if node_type == 'Parity':
        node = ParityEthJsonRpc(host=host, port=port)
    elif node_type == 'Geth':
        node = EthJsonRpc(host=host, port=port)
    elif node_type == 'Infura':
        network = host.split('.')[0]  # getting the network name
        node = InfuraEthJsonRpc(network=network, infura_token=api_token)
    else:
        raise ValueError('Node {} not supported'.format(node_type))

    logging.info('Connected to {} node'.format(node_type))

    return node


setup_logging()

db_session, db_engine = setup_db_session(user=settings.SQLALCHEMY_USER,
                                         password=settings.SQLALCHEMY_PASSWORD,
                                         db=settings.SQLALCHEMY_DB)

node_session = setup_node_session(node_type=settings.NODE_TYPE,
                                  host=settings.NODE_HOST,
                                  port=settings.NODE_PORT,
                                  api_token=settings.NODE_API_TOKEN)
