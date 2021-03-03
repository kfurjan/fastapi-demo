# fastapi-demo

Demo project showcasing FastAPI framework and comparing it to Flask framework

## "Hello World" example

### Flask

```python
# flask_demo.py

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"Hello": "Flask!"}


if __name__ == "__main__":
    app.run()
```

### FastAPI

```python
# fastapi_demo.py

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "FastAPI!"}


if __name__ == "__main__":
    uvicorn.run("fastapi_demo:app")
```

## Performance test example

### Flask

```python
# flask_demo.py

import time

from flask import Flask

app = Flask(__name__)


START = "START"
STOP = "STOP"
ONE_SECOND = 1


def blocking_sleep():
    print(START)
    time.sleep(ONE_SECOND)
    print(STOP)


@app.route("/perf")
def perf_test(): # response: {"Time elapsed": "3.00 seconds"}
    time_now = time.perf_counter()

    for _ in range(3):
        blocking_sleep()

    elapsed = time.perf_counter() - time_now
    return {"Time elapsed": f"{elapsed:0.2f} seconds"}


if __name__ == "__main__":
    app.run()
```

### FastAPI

```python
# fastapi_demo.py

import asyncio
import time

import uvicorn
from fastapi import FastAPI

app = FastAPI()


START = "START"
STOP = "STOP"
ONE_SECOND = 1


async def async_sleep():
    print(START)
    await asyncio.sleep(ONE_SECOND)
    print(STOP)


@app.get("/perf")
async def perf_test(): # response: {"Time elapsed": "1.00 seconds"}
    time_now = time.perf_counter()

    await asyncio.gather(async_sleep(), async_sleep(), async_sleep())

    elapsed = time.perf_counter() - time_now
    return {"Time elapsed": f"{elapsed:0.2f} seconds"}


if __name__ == "__main__":
    uvicorn.run("fastapi_demo:app")
```

## Data validation

One more advantage of FastAPI is data validation out of the box.

```python
# fastapi_demo.py

import time
from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    in_stock: Optional[bool] = None


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item): # Error code 422 if not all data is supplied on PUT request
    return {"item_name": item.name, "item_id": item_id}


if __name__ == "__main__":
    uvicorn.run("fastapi_demo:app")
```
