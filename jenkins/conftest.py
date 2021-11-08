import pytest

@pytest.fixture(scope='module')
def setUptearDownClass():
    print('setUp Class Method(Activity)....')
    yield
    print('tearDown Class Method(Activity)....')

@pytest.fixture()
def setUptearDown():
    print('setUp method activity....')
    yield
    print('tearDown Method Activity....')
