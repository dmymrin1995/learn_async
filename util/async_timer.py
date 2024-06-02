import asyncio
import functools
import time
from datetime import datetime
from typing import Callable, Any


def get_timestamp():
    return f'[{datetime.now().strftime("%H:%M:%S")}]:'


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"{get_timestamp()} выполняется {func} с аргументами {args} {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"{get_timestamp()} {func} завершилась за {total:.4f} с")

        return wrapped

    return wrapper


@async_timed()
async def delay(delay_seconds: int):
    print(f"{get_timestamp()} засыпаю на {delay_seconds} с")
    await asyncio.sleep(delay_seconds)
    print(f"{get_timestamp()} сон в течение {delay_seconds} c закончился")
    return delay_seconds
