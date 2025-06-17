Como você mencionou Python e FastAPI na pergunta, acredito que houve um erro ao mencionar nodejs na especificação. Vou criar um código Python usando FastAPI com dois endpoints.


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

app = FastAPI()

items = {}

@app.post("/items/")
async def create_item(item: Item):
    """
    Create an item with all the information
    """
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.name] = item
    return item

@app.get("/items/{item_name}")
async def read_item(item_name: str):
    """
    Get a specific item by name
    """
    item = items.get(item_name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


Neste código, temos dois endpoints:

1. POST /items/ : Este endpoint espera um corpo de solicitação que corresponde ao modelo Item e adiciona o item a um dicionário. Se o item já existir, uma exceção HTTP 400 é levantada.

2. GET /items/{item_name} : Este endpoint recebe um parâmetro de caminho item_name e retorna o item correspondente do dicionário. Se nenhum item for encontrado, uma exceção HTTP 404 é levantada.