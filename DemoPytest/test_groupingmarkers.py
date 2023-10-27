import pytest

#test_groupingmarkers.py file has 5 test cases.
@pytest.mark.regression
def testmarkeraddoftwonum():
    """testcase: function for adding two hardcoded values and sum it.  \
    assert the sum value is equal to hardcoded sum value or not """
    a=5
    b=10
    sum=a+b
    assert sum == 15

@pytest.mark.sanity
def testmarkeraddofthreenum():
    """testcase: function for adding three hardcoded values and sum it.  \
    assert the sum value is equal to hardcoded sum value or not """
    a=5
    b=10
    c=20
    sum=a+b+c
    assert sum == 35

@pytest.mark.skip
def testmarkerwindowsplatform():
    """testcase: function for windowsplatform operation"""
    pass


def testmarkerlinuxplatform():
    """testcase: function for linuxplatform operation"""
    pass

@pytest.mark.xfail
def testmultiply():
    """testcase: function for multiplicaton operation, \
    need to add logic properly, currently kept it as xfail custom marker category"""
    pass
