from tests.common_tests.block_range import (
    push_block_range_single_thread,
    verify_block_range_single_thread,
)


def test_verify_block_range_single_thread(
        parity_session_block_range_56160_56170):
    parity_session_block_range_56160_56170.setup_db_session()
    verify_block_range_single_thread(
        parity_session_block_range_56160_56170)
    pass


def test_parity_push_block_range(parity_settings):
    push_block_range_single_thread(parity_settings)
    pass
