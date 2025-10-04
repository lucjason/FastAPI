from fastapi import FastAPI

app = FastAPI()

items = []


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.post("/items")
def create_item(item: str):
    items.append(item)
    return item


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items[item_id]
