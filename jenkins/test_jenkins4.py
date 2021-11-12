import pytest

@pytest.mark.sanity
def test_methodA(setUptearDownClass,setUptearDown):
    print('test_jenkins4: test MethodA Execution.....')

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.sanity
def test_methodB(setUptearDownClass,setUptearDown):
    print('test_jenkins4: test MethodB Execution.....')

@pytest.mark.sanity
def test_methodC(setUptearDownClass,setUptearDown):
    print('test_jenkins4: test MethodC Execution.....')

@pytest.mark.regression
def test_methodD(setUptearDownClass,setUptearDown):
    print('test_jenkins4: test MethodD Execution.....')