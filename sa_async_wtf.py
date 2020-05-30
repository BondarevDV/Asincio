from time import sleep
from time import time
import asyncio

start = time()


def loader(url):
    print("Load {} at {:.2F}".format(url, time() - start))


# возвращает сопрограмму или корутину
async def spider(site_name):
    for page in range(1, 4):
        await asyncio.sleep(1)
        if site_name == "Forum":
            sleep(3)
        print(site_name, page)


if __name__ == "__main__":
    spiders = [
        asyncio.ensure_future(spider("blog")),
        asyncio.ensure_future(spider("News")),
        asyncio.ensure_future(spider("Forum")),
    ]

    event_loop = asyncio.get_event_loop()
    now = event_loop.time()

    event_loop.call_soon(loader, "url_1")
    event_loop.call_soon(loader, "url_2")

    event_loop.call_later(2, loader, "url_3")
    event_loop.call_at(now + 2, loader, "url_4")
    event_loop.run_until_complete(asyncio.gather(*spiders))

    event_loop.close()
    print("{:.2F}".format(time() - start))
