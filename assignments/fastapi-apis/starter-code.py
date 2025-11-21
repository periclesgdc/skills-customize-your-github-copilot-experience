from fastapi import FastAPI

app = FastAPI()

# Define your Pydantic models here

# Example endpoints
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}