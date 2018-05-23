import pytest
from decimal import Decimal
import datetime

from ether_sql.setup import Session
from ether_sql.models import base


@pytest.fixture(scope='module')
def empty_db_infura_session():
    """
    Infura Fixture containing exmpty database
    """
    config = 'TestSettings'
    empty_db_infura_session = Session(override_settings=config)
    return empty_db_infura_session


@pytest.fixture(scope='module')
def empty_db_parity_session():
    """
    Parity Fixture containing exmpty database
    """
    config = 'ParityTestSettings'
    empty_db_parity_session = Session(override_settings=config)
    return empty_db_parity_session


@pytest.fixture(scope='module')
def empty_table_infura_session(empty_db_infura_session):
    """
    Infura Fixture with created but empty tables
    """
    empty_table_infura_session = empty_db_infura_session
    base.metadata.create_all(empty_table_infura_session.db_engine)
    return empty_table_infura_session


@pytest.fixture(scope='module')
def empty_table_parity_session(empty_db_parity_session):
    """
    Parity Fixture with created but empty tables
    """
    empty_table_parity_session = empty_db_parity_session
    base.metadata.create_all(empty_table_parity_session.db_engine)
    return empty_table_parity_session


@pytest.fixture()
def expected_block_properties():
    expected_block_properties = {'block_number': Decimal('56160'),
                                 'timestamp': datetime.datetime(2015, 8, 9, 1, 14, 50),
                                 'transaction_count': Decimal('1'),
                                 'block_hash': u'0x685b2226cbf6e1f890211010aa192bf16f0a0cba9534264a033b023d7367b845',
                                 'difficulty': Decimal('1640036045719'),
                                 'uncle_count': Decimal('1'),
                                 'sha3uncles': u'0x8a67da3121c69b45a19f4674a7272ebad677f9775ca6b35d79067974ca687a64',
                                 'miner': u'0x3F98e477a361F777DA14611a7e419A75Fd238b6b',
                                 'gas_used': Decimal('50290'),
                                 'parent_hash': u'0x071218ca3c6549337289e5e0e78227f59a82d62a972d6d73e6b8e55dcbaa65eb',
                                 'extra_data': u'0x476574682f76312e302e312f6c696e75782f676f312e342e32',
                                 'gas_limit': Decimal('3141592')}
    return expected_block_properties


@pytest.fixture()
def expected_uncle_properties():
    expected_uncle_properties = {'timestamp': datetime.datetime(2015, 8, 9, 1, 14, 50),
                                 'current_blocknumber': Decimal('56160'),
                                 'difficulty': u'1640036436734',
                                 'sha3uncles': u'0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
                                 'uncle_blocknumber': Decimal('56158'),
                                 'miner': u'0xbe4532e1b1db5c913cf553be76180c1777055403',
                                 'gas_used': Decimal('0'),
                                 'uncle_hash': u'0xc78c35720d930f9ef34b4e6fb9d02ffec936f9b02a8f0fa858456e4afd4d5614',
                                 'parent_hash': u'0xcc30e8a9b15c548d5bf113c834143a8f0e1909fbfea96b2a208dc154293a78cf',
                                 'extra_data': u'0x476574682f686261722f76312e302e312f6c696e75782f676f312e342e32',
                                 'gas_limit': Decimal('3141592')}
    return expected_uncle_properties


@pytest.fixture()
def expected_transaction_properties():
    expected_transaction_properties = {'nonce': Decimal('6'),
                                       'block_number': Decimal('56160'),
                                       'timestamp': datetime.datetime(2015, 8, 9, 1, 14, 50),
                                       'transaction_hash': u'0x8696c8669e07ae7e4ceef43945fe9c78252ab76f1a3c16658a04a644b8329736',
                                       'transaction_index': Decimal('0'),
                                       'data': u'0x90b98a110000000000000000000000006463f715d594a1a4ace4bb9c3b288a74decf294d00000000000000000000000000000000000000000000000000000000000003e8',
                                       'gas_price': Decimal('57105088684'),
                                       'sender': u'0x9B2c46642CAF6B936dc0633da521f1E946B7e18F',
                                       'value': Decimal('0'),
                                       'receiver': u'0xDBB576b5B0e7BF0570A981AAb3AD39A0c5F19EB1',
                                       'start_gas': Decimal('90000')}
    return expected_transaction_properties


@pytest.fixture()
def expected_receipt_properties():
    expected_receipt_properties = {'status': None,
                                   'block_number': Decimal('56160'),
                                   'contract_address': None,
                                   'transaction_index': Decimal('0'),
                                   'timestamp': datetime.datetime(2015, 8, 9, 1, 14, 50),
                                   'cumulative_gas_used': Decimal('50290'),
                                   'transaction_hash': u'0x8696c8669e07ae7e4ceef43945fe9c78252ab76f1a3c16658a04a644b8329736',
                                   'gas_used': Decimal('50290')}
    return expected_receipt_properties


@pytest.fixture()
def expected_log_values():
    expected_log_values = {'block_number': Decimal('56160'),
                           'topics_count': Decimal('1'),
                           'log_index': Decimal('0'),
                           'timestamp': datetime.datetime(2015, 8, 9, 1, 14, 50),
                           'transaction_hash': u'0x8696c8669e07ae7e4ceef43945fe9c78252ab76f1a3c16658a04a644b8329736',
                           'topic_4': u'',
                           'topic_3': u'',
                           'topic_2': u'',
                           'topic_1': u'0x16cdf1707799c6655baac6e210f52b94b7cec08adcaf9ede7dfe8649da926146',
                           'address': u'0xDBB576b5B0e7BF0570A981AAb3AD39A0c5F19EB1',
                           'transaction_index': Decimal('0'),
                           'data': u'0x0000000000000000000000009b2c46642caf6b936dc0633da521f1e946b7e18f0000000000000000000000006463f715d594a1a4ace4bb9c3b288a74decf294d00000000000000000000000000000000000000000000000000000000000003e8'}
    return expected_log_values
