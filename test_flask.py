 
url = "http://127.0.0.1:5000"

def test_addtwo_function(): 
    testdata_a = 20
    testdata_b = 30
    expected = 40
    actual = addtwo(testdata_a, testdata_b)

    assert actual == expected
    # pass or fail