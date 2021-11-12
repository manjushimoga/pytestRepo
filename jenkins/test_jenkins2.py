import pytest

@pytest.mark.regression
def test_methodA(setUptearDownClass,setUptearDown):
    print('test_jenkins2: test MethodA Execution.....')

@pytest.mark.smoke
def test_methodB(setUptearDownClass,setUptearDown,name):
    print('test_jenkins2: test MethodB Execution.....')
    if name is not None:
        assert name.lower() == 'pytest'

@pytest.mark.sanity
def test_methodC(setUptearDownClass,setUptearDown):
    print('test_jenkins2: test MethodC Execution.....')

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.sanity
def test_methodD(setUptearDownClass,setUptearDown,name):
    print('test_jenkins2: test MethodD Execution.....')
    if name is not None:
        assert name.lower() == 'pytest'