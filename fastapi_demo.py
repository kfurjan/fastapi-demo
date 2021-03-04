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


@app.get("/perf")
async def perf_test():
    start_time = time.perf_counter()

    await asyncio.gather(async_sleep(), async_sleep(), async_sleep())

    elapsed = time.perf_counter() - start_time
    return {"Time elapsed": f"{elapsed:0.2f} seconds"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}


if __name__ == "__main__":
    uvicorn.run("fastapi_demo:app", port=5000, reload=True)
