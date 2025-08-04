from flask import Flask, request

app = Flask(__name__)

@app.route('/addtwointegers/<int:c>/<float:d>', methods=['POST'])
def addtwo(c,d):
  print(request)
  print(request.json)
  a = request.json.get('a')
  b = request.json.get('b')
  return {"response": a+b+c+d}

if __name__ == "__main__":
    app.run(debug=True)



# route paramaters -> c
# query paramets -> a,b