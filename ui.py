import streamlit as st
import requests

number1 = st.number_input("Enter the first number:")
number2 = st.number_input("Enter the second number:")

url = "https://ganuganesh.pythonanywhere.com/addtwointegers"
testdata_c = 100
testdata_d = 4.5

url_1 = url + "/" + str(testdata_c) + "/" + str(testdata_d)
print("Updated URl", url_1)

data_payload = {"a": number1, "b": number2}
output = requests.post(url=url_1, json=data_payload)
output_dict = output.json()
#print("response_code",output.response_code)
sum_result = output_dict["response"]
st.write("The sum is:", sum_result)