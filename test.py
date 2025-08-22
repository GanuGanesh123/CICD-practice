
from sum import addtwo  
print("asserting test.py")
def test_addtwo_function(): # Renamed to follow 'test_' convention
    testdata_a = 20
    testdata_b = 30
    expected = 50
    actual = addtwo(testdata_a, testdata_b)

    assert actual == expected
    # pass or fail
test_addtwo_function()
