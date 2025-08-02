from fastapi import FastAPI

app = FastAPI()

@app.get("/addtwo")
async def addtwo(a,b):
  return a+b
