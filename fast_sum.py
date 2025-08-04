# This is flask code for adding two numbers

from fastapi import FastAPI

app = FastAPI()

@app.get("/addtwo")
async def addtwo(a,b):
  return a+b
