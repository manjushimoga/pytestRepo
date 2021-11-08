import pytest

@pytest.mark.sanity
@pytest.mark.run(order=2)
def test_methodA(setUptearDownClass,setUptearDown):
    print('test_jenkins1: test MethodA Execution.....')

@pytest.mark.run(order=1)
def test_methodB(setUptearDownClass,setUptearDown):
    print('test_jenkins1: test MethodB Execution.....')