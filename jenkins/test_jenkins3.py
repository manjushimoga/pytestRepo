import pytest

@pytest.mark.regression
@pytest.mark.smoke
def test_methodA(setUptearDownClass,setUptearDown,name):
    print('test_jenkins3: test MethodA Execution.....')
    assert name.lower() == 'pytest'

@pytest.mark.smoke
def test_methodB(setUptearDownClass,setUptearDown):
    print('test_jenkins3: test MethodB Execution.....')

@pytest.mark.sanity
def test_methodC(setUptearDownClass,setUptearDown):
    print('test_jenkins3: test MethodC Execution.....')

@pytest.mark.regression
def test_methodD(setUptearDownClass,setUptearDown,name):
    print('test_jenkins3: test MethodD Execution.....')
    print("Pytest command argument", name)
    assert name.lower()=='pytest'