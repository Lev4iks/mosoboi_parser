import sqlite3
import settings

try:
    db = sqlite3.connect("database.db", check_same_thread=False)
    cursor = db.cursor()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)


def add_items(items):
    cursor.executemany(
        """INSERT INTO oboi(name, price, url) VALUES(?, ?, ?)""",
        items
    )
    db.commit()


def get_items():
    cursor.execute(
        """SELECT name, price FROM oboi"""
    )
    items = [value[:2] for value in cursor.fetchall()]
    return items


def get_first_five_items():
    cursor.execute(
        """SELECT name, price FROM oboi WHERE url = ? LIMIT 5""", (settings.FIRST_PAGE_URL,)
    )
    items = [value[:2] for value in cursor.fetchall()]
    return items


def get_last_five_items():
    cursor.execute(
        """SELECT name, price FROM oboi WHERE url = ? ORDER BY name DESC LIMIT 5""", (settings.LAST_PAGE_URL,)
    )
    items = [value[:2] for value in cursor.fetchall()]
    return items
