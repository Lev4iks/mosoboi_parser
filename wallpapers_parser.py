from bs4 import BeautifulSoup

from helpers import get_pages_count
import settings

import aiohttp
import asyncio

import db_connector as db

items = []


async def get_page_data(session, page):
    url = f"{settings.URL}?PAGEN_1={page}"
    async with session.get(url=url, headers=settings.headers) as response:
        global items

        response_txt = await response.text()
        soup = BeautifulSoup(response_txt, "html.parser")

        temp_items = soup.find("div", class_="js-wrap-catalog-items wrap-catalog-items").find(
            "div", class_="row").find_all("div", class_="row")[:-1]

        for item in temp_items:
            try:
                name = item.find("div", class_="product-item__fabric-name").find("span").text
            except:
                name = "Нет наименования"
            try:
                price = ''.join(item.find("div", class_="new_price").text.split()[:-1])
            except:
                price = "Нет цены"

            items.append([name, price, url])
        print(f"[INFO] Обработал страницу : {page}")


async def gather_data(url):
    async with aiohttp.ClientSession() as session:
        tasks = []

        pages_count = get_pages_count(url)

        for page in range(1, pages_count + 1):
            task = asyncio.create_task(get_page_data(session, page))
            tasks.append(task)

        await asyncio.gather(*tasks)


def run():
    asyncio.get_event_loop().run_until_complete(gather_data(settings.URL))
    db.add_items(items)
