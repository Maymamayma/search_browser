import aiohttp
import asyncio

class AsyncCrawler:
    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def crawl(self, urls):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in urls]
            return await asyncio.gather(*tasks)
