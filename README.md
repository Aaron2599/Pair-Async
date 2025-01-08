# PairAsync | Seamless Async-Sync Integration for Python

[![PyPI - Version](https://img.shields.io/pypi/v/pairasync)](https://pypi.org/project/pairasync/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**PairAsync** is a Python library that combines asynchronous (async) with synchronous (sync) code, enabling developers to execute async functions within sync environments. Ideal for enhancing Python applications from version 3.7 onwards, PairAsync simplifies the integration of asynchronous operations into traditional synchronous codebases.

## Installation
Get started with PairAsync by installing it via pip:

```bash
pip install pairasync
```

## Key Features

- **Run Async Functions Sync**: Execute simple async functions synchronously and retrieve results instantly.
- **Custom Async Handling**: For more complex async tasks, create tailored async functions and pair them with your sync code without converting your entire codebase to async.



## Usage
### Simple Async Function Execution
use PairAsync to run basic async functions in a sync context:
```python
from pairasync import sync
import asyncio

async def simple_async_func():
    await asyncio.sleep(1)
    return "Hello from async!"

result = sync(simple_async_func())
print(result)  # Output: Hello from async!
```
### Complex Async Scenarios
For complex scenarios running side effect prone functions or when using a larger event driven library (selenium, aiohttp, asyncpg) define your async function then run it in a sync context:
```python
from pairasync import sync
import aiohttp

async def get_text(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

class SomeClass:

    def __init__(self):
        result = sync(get_text("https://example.com"))
        print(result)

object = SomeClass() 
```
