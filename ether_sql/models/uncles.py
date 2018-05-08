from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
from sqlalchemy import LargeBinary


from ether_sql.models import base


class Uncles(base):

    """
    Class defining an uncle in the ethereum blockchain, its properties are more
    accurately defined in the ethereum yellow paper https://github.com/ethereum/yellowpaper.

    :param str uncle_hash: The Keccak 256-bit hash of this uncle
    :param int uncle_blocknumber: Number of blocks behind this uncle
    :param str parent_hash: The Keccak 256-bit hash of the parent of this uncle
    :param int difficulty: Difficulty level of this block
    :param int current_blocknumber: Block number where this uncle was included
    :param int gas_used: Total gas used by the transactions in this uncle
    :param str miner: Address of account where all corresponding uncle rewards are transferred
    :param int timestamp: Unix time at the at this uncles inception
    :param str sha3uncles: Keccak 256-bit hash of the uncles portion of this uncle
    :param bytes extra_data: Byte array of 32 bytes or less containing extra data of this block
    :param int gas_limit: Current maximum gas expenditure per block

    """
    __tablename__ = 'uncles'

    uncle_hash = Column(String(66), primary_key=True, unique=True, index=True)
    uncle_blocknumber = Column(Integer, nullable=False)
    parent_hash = Column(String(66), nullable=False)
    difficulty = Column(String(66), unique=True, nullable=False)
    current_blocknumber = Column(Integer,  ForeignKey('blocks.block_number'),
                                 unique=True)
    gas_used = Column(Integer, nullable=False)
    miner = Column(String(42), nullable=False)
    timestamp = Column(TIMESTAMP)
    sha3uncles = Column(String(66), nullable=False)
    extra_data = Column(LargeBinary)
    gas_limit = Column(Integer, nullable=False)

    def to_dict(self):
        return {
                'uncle_hash': self.uncle_hash,
                'uncle_blocknumber': self.uncle_blocknumber,
                'parent_hash': self.parent_hash,
                'difficulty': self.difficulty,
                'current_blocknumber': self.current_blocknumber,
                'gas_used': self.gas_used,
                'miner': self.miner,
                'timestamp': self.timestamp,
                'sha3uncles': self.sha3uncles,
                'extra_data': self.extra_data,
                'gas_limit': self.gas_limit
                }

    def __repr__(self):
        return "<Uncle {}>".format(self.uncle_hash)
