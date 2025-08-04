from flask import Flask, request

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def addtwo():
  print(request)
  print(request.json)
  a = request.json.get('a')
  b = request.json.get('b')
  return {"response": a+b}

if __name__ == "__main__":
    app.run(debug=True, port=8000)