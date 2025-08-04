 

import requests

url = "http://127.0.0.1:5000/addtwointegers"

def test_addtwo_function(): 
    testdata_a = 20
    testdata_b = 30
    testdata_c = 100
    testdata_d = 4.5

    url_1 = url + "/" + str(testdata_c) + "/" + str(testdata_d)
    print("Updated URl", url_1)

    data_payload = {"a": testdata_a, "b": testdata_b}
    expected = 154.5
    output = requests.post(url=url_1, json=data_payload)
    output_dict = output.json()
    #print("response_code",output.response_code)
    actual = output_dict["response"]
    print(actual,expected)

    assert actual == expected

test_addtwo_function()