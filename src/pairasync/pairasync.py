import threading
from concurrent.futures import ThreadPoolExecutor

import asyncio
from typing import TypeVar, Coroutine, Any


def _run_in_new_loop(func):
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    try:
        return new_loop.run_until_complete(func)
    finally:
        new_loop.close()


T = TypeVar("T")


def sync(coroutine: Coroutine[Any, Any, T], timeout=None) -> T:
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coroutine)

    if threading.current_thread() is threading.main_thread():
        if not loop.is_running():
            return loop.run_until_complete(coroutine)
        else:
            with ThreadPoolExecutor() as pool:
                future = pool.submit(_run_in_new_loop, coroutine)
                return future.result(timeout=timeout)
    else:
        return asyncio.run_coroutine_threadsafe(coroutine, loop).result()

