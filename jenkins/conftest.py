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



def pytest_addoption(parser):
    parser.addoption("--name", action="store")

@pytest.fixture(scope='session')
def name(request):
    name_value = request.config.getoption("--name")

    if name_value is None:
        return 'No value'
    return name_value

# @pytest.fixture()
# def bwsr(request): #This will return the Browser value to setup method
#     return request.config.getoption("--browser")
