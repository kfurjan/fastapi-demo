import asyncio
import time
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from utils import async_sleep

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    in_stock: Optional[bool] = None


@app.get("/")
def home():
    return {"Hello": "FastAPI!"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/perf")
async def perf_test():
    time_now = time.perf_counter()

    await asyncio.gather(async_sleep(), async_sleep(), async_sleep())

    elapsed = time.perf_counter() - time_now
    return {"Time elapsed": f"{elapsed:0.2f} seconds"}


if __name__ == "__main__":
    uvicorn.run("fastapi_demo:app", port=5000, reload=True)
