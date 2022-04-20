import settings

import requests
from bs4 import BeautifulSoup


def get_pages_count(url) -> int:
    response = requests.get(url, headers=settings.headers)
    soup = BeautifulSoup(response.text, "html.parser")

    items_count = int(soup.find("div", class_="count_products").get_text().split()[0])
    pages_count = items_count // 60 if not items_count % 60 else (items_count // 60) + 1
    settings.FIRST_PAGE_URL = f"{settings.URL}?PAGEN_1=1"
    settings.LAST_PAGE_URL = f"{settings.URL}?PAGEN_1={pages_count}"
    return pages_count
