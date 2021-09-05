import pytest

@pytest.fixture(scope='class')
def setupClass():
    print("STARTED in Class\n")
    yield
    print("\nENDED in Class")


@pytest.fixture()
def setup():
    print("STARTED\n")
    yield
    print("\nENDED")

@pytest.fixture()
def Dataload():
    return ["Dev", "Mishra", 28]

@pytest.fixture(params = [["Chrome", "Google"], ("Firefox", "Redhat"), ("Edge", 22)])
def crossBrowser(request):
    return request.param

