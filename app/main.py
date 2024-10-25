# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import HTTPException
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from app.routers import example

items = []
model_items = []
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items/")
def create_item(item: str):
    items.append(item)
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.get("/items/")
def list_item(limit: int):
    return items[0: limit]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/create_model_item/")
async def create_model_item(item: Item):
    model_items.append(item)
    return item


@app.get("/model_items/{item}")
def get_model_item(item_id: Item):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.get("/model_items/")
def list_model_item(limit: int):
    return model_items[0: limit]

# Include additional routers
app.include_router(example.router)
