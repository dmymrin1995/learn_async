import asyncio

import aiohttp
from aiohttp import ClientSession 

from util import async_timed
from chapter_4 import fetch_status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.ru' for _ in range(15)]
        requests = [fetch_status(session, url, 10) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)

asyncio.run(main())