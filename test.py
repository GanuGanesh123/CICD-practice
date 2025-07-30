from sum import addtwo 

def testaddtwo():
    testdata_a = 20
    testdata_b = 30
    expected = 50
    actual = addtwo(testdata_a, testdata_b)

    if actual == expected:
      print("passed")
    else:
      print("failed")

testaddtwo()

  
