import json
import uuid
import pandas as pd

from flask import Flask, request
app = Flask(__name__)

csv_df = pd.DataFrame(columns=["a", "b"])
csv_df.to_csv("DB/CSV/requests.csv", index=False)

def save_request_as_json(req_json: dict):
   
   with open(f"DB/requests/req_json_{uuid.uuid4()}.json", "w") as f:
      json.dump(req_json, f, indent=4)
   return None

def save_response_as_json(resp_json: dict):
   
   with open(f"DB/responses/resp_json_{uuid.uuid4()}.json", "w") as f:
      json.dump(resp_json, f, indent=4)
   return None

@app.route('/saveToCSV/', methods=['POST'])
def save_into_csv():
   a = request.json.get('a')
   b = request.json.get('b')
   df = pd.read_csv("DB/CSV/requests.csv")
   current_index = df.shape[0]
   index_to_insert = current_index + 1
   df.loc[index_to_insert] = [a, b]
   df.to_csv("DB/CSV/requests.csv", index=False)
   return {"response": "Success"}

if __name__ == "__main__":
    app.run(debug=True, port=5001)