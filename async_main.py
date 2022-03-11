import asyncio

import aiohttp

headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': '*/*'
    }

async def create_task():
    url = 'https://www.embroplace.com/ru/embroidery-1'
    async with aiohttp.ClientSession() as session:
        categories = await session.get(url)
        print( await categories.text())


if __name__ == '__main__':
     asyncio.run(create_task())