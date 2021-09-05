import pytest
import conftest

def test_FirstTest():
    print("fIRST-fIRST")

@pytest.mark.smoke
def test_SecondTest():
    print("Second-Second")

@pytest.mark.skip
@pytest.mark.smoke
def test_BirdTest():
    strings = 'SING'
    assert strings == '''FANCY''', "Did not match"




