import asyncio
import time

START = "START"
STOP = "STOP"
ONE_SECOND = 1


def blocking_sleep():
    print(START)
    time.sleep(ONE_SECOND)
    print(STOP)


async def async_sleep():
    print(START)
    await asyncio.sleep(ONE_SECOND)
    print(STOP)
