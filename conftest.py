import time

import pytest
from loguru import logger

@pytest.fixture()
def set_up():
    logger.warning('Start test')
    yield
    time.sleep(5)
    logger.warning('Finish test')

