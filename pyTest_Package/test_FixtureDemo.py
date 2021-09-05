import pytest

from pyTest_Package.baseClass import baseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("setupClass")
class TestExample:
    def test_fixtureUsage1(self):
        print("TESTCASE_1")

    def test_fixtureUsage2(self):
        print("TESTCASE_2")

    def test_fixtureUsage3(self):
        print("TESTCASE_3")

    def test_fixtureUsage4(self):
        print("TESTCASE_4")


@pytest.mark.usefixtures("Dataload")
class TestDataclass(baseClass):
    def test_editprofile(self, Dataload):
        logs = self.getLoggerObj()
        logs.info(Dataload[1])
        logs.warning(Dataload[0])
        logs.critical(Dataload[2])


@pytest.mark.usefixtures("crossBrowser")
def test_crossbrowsers(crossBrowser):
    print(crossBrowser)

@pytest.mark.usefixtures("crossBrowser")
def test_crossbrowsersMultiplevalues(crossBrowser):
    print(crossBrowser[1])