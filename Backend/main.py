from fastapi import FastAPI

app = FastAPI()

#Closes the API
@app.get("/")
async def root():
    return {"message": "Hello World"}