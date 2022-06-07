import pytest
import logging

logger = logging.getLogger()
logger.setLevel('INFO')

from code_for_testing import Human

@pytest.fixture()
def set_human(self):
    yield Human('Stefan', 29, 'male')

@pytest.fixture()
def set_living_friend(self):
    logger.info(msg='\nFixture start')
    yield Human('Francisco', 35, 'male')
    logger.info(msg='\nFixture finished')


@pytest.fixture()
def set_dead_friend(self):
    dead_friend = Human('Dominic', 106, 'male')
    dead_friend.grow()
    yield dead_friend