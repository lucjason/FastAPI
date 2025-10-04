from fastapi import FastAPI, HTTPException

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
    if item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

