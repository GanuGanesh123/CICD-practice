from flask import Flask, request
import pandas as pd
import requests
app = Flask(__name__)
import time
import logging

class AddTwoException(Exception):
   pass
# .db file
global_app_cache = {}
@app.route('/addtwointegers/<int:c>/<float:d>', methods=['POST'])
def addtwo(c,d):
  if "c" in app_cache: # .db file query for cache data
     return app_cache["c"]

  time.sleep(5)
  print(request)
  print(request.json)
  a = request.json.get('a')
  b = request.json.get('b')
  request_to_save = {"a": a, "b": b}
  if a is None or b is None:
     logging.error("Both are non")
  if a is 0 and b is 0:
     logging.debug("Both are zero")
  try:
     op = a + b
  except Exception as e:
     logging.critical(f"Cannot proceed")
     # customize with my own type of exception and my message
     raise AddTwoException(f"Raised because one of the data type is invalid. {type(a)}")
  data_pipeline_url = "http://127.0.0.1:5001/saveToCSV"
  data_payload = request_to_save
  data_req_save_response = requests.post(data_pipeline_url,json=data_payload )
  logging.info(data_req_save_response.content)
  # save_square_values(a*a, b*b)
  #UserDBAPI.save_into_csv(request_to_save)
  # read_some_other_values()
  # write_
  output = {"response": a*a + b+c+d}
  app_cache = {"c": output}
  #save_response(output)
  return output

if __name__ == "__main__":
    app.run(debug=True)



# route paramaters -> c
# query paramets -> a,b