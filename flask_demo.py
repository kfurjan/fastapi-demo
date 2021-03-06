import time

from flask import Flask

from utils import blocking_sleep

app = Flask(__name__)


@app.route("/")
def home():
    return {"Hello": "Flask!"}


@app.route("/perf")
def perf_test():
    start_time = time.perf_counter()

    for _ in range(3):
        blocking_sleep()

    elapsed = time.perf_counter() - start_time
    return {"Time elapsed": f"{elapsed:0.2f} seconds"}


if __name__ == "__main__":
    app.run()
