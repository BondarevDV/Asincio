# реализовать чтение файлов

from time import sleep
from time import time
import asyncio

start = time()


# возвращает сопрограмму или корутину
async def get_pages(site_name):
    await asyncio.sleep(0.5)
    print("Get pages for {}".format(site_name))
    return range(1, 6)


# возвращает сопрограмму или корутину
async def get_pages_data(site_name, page):
    await asyncio.sleep(1)
    return "Data from pages {} ({})".format(page, site_name)


# возвращает сопрограмму или корутину
async def spider(site_name):
    all_data = []
    pages = await get_pages(site_name)
    for page in pages:
        data = await get_pages_data(site_name, page)
        all_data.append(data)
        print(data)
    return all_data

if __name__ == "__main__":
    print(globals())
    spiders = [
        asyncio.ensure_future(spider("blog")),
        asyncio.ensure_future(spider("News")),
        asyncio.ensure_future(spider("Forum")),
    ]

    event_loop = asyncio.get_event_loop()
    result = event_loop.run_until_complete(spider("API"))
    print(result)
    event_loop.close()
    print("{:.2F}".format(time() - start))
