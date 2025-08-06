from flask import Flask, request
import pandas as pd
import requests
app = Flask(__name__)
import time
   

@app.route('/addtwointegers/<int:c>/<float:d>', methods=['POST'])
def addtwo(c,d):
  time.sleep(5)
  print(request)
  print(request.json)
  a = request.json.get('a')
  b = request.json.get('b')
  request_to_save = {"a": a, "b": b}
  data_pipeline_url = "http://127.0.0.1:5001/saveToCSV"
  data_payload = request_to_save
  data_req_save_response = requests.post(data_pipeline_url,json=data_payload )
  print(data_req_save_response.content)
  #save_into_csv(request_to_save)
  output = {"response": a+b+c+d}
  #save_response(output)
  return output

if __name__ == "__main__":
    app.run(debug=True)



# route paramaters -> c
# query paramets -> a,b