from flask import Flask, request

app = Flask(__name__)

@app.route('/addtwointegers/<int:c>', methods=['GET'])
def addtwo(c):
  print(request)
  print(request.json)
  a = request.json.get('a')
  b = request.json.get('b')
  return {"response": a+b+c}

if __name__ == "__main__":
    app.run(debug=True)