import pytest

# keep the common pytest fixture function into conftest.py.
# so that we can use across the files available inside the package.

@pytest.fixture(autouse=True,scope="session")
def general_setup():
    print("\n general_setup fixture function will be applicable across all the file, since the scope is defined for session and autouse as True...")
    yield
    print("\n clean up progress")

@pytest.fixture()
def addition_setup(calculationtype):
    print("\n going to perform addition operation for int data type variables")
    if calculationtype == "addition":
        print("\n it will perform addition operation")
    else:
        print("\n not a valid calculationtype. it support only addition")


@pytest.fixture()
def welcome_setup():
    print("\n saying welcome to user for pytest based codebase understanding")

#fixtureparametrizing example
@pytest.fixture(params=["a","b"])
def test_alphabet(request):
    print("\n fixture function call counting using alphabet variable:",request.param,"\n")

def pytest_addoption(parser):
    parser.addoption("--calculationtype")

@pytest.fixture()
def calculationtype(request):
    return request.config.getoption("--calculationtype")




