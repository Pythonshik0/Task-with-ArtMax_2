from bs4 import BeautifulSoup
import requests
import lxml
import json
from loguru import logger
import logging
import sqlite3
import asyncio
import aiohttp

logging.basicConfig(level=logging.DEBUG)


async def gather_data():

    headers = {"Accept": "*/*",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    url = 'https://2gis.ru/ufa/firm/70000001006794970/tab/reviews'

    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')
        cards = soup.find_all('div', class_='_1i94jn5')
        print(cards)

        all_categories_dict = {}
        for item in cards:
            item_text = 'Первый филиал. Отзыв сайта "Вкусно и Точка!"   ' + item.text
            item_id = item.id
            all_categories_dict[item_text] = item_id
            logger = logging.getLogger('Ошибки нет!')
            logger.debug(f'{item_text} {item_id}')

    # Сохраняю с json
    with open('all_categories_dict_1', 'w', encoding="utf-8") as file:
        json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        #cursor.execute('CREATE TABLE Parser_2 (item_text)')
        cursor.executemany("INSERT INTO Parser_2 (item_text) VALUES (?)", zip(all_categories_dict))
        sqlite_connection.commit()
        print("Запись успешно вставлена в таблицу")

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


async def gather_data_2():

    headers = {"Accept": "*/*",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    url = 'https://2gis.ru/ufa/firm/2393065583018884/tab/reviews'

    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')
        cards = soup.find_all('div', class_='_1i94jn5')
        print(cards)

        all_categories_dict = {}
        for item in cards:
            item_text = 'Второй филиал. Отзыв сайта "Вкусно и Точка!"   ' + item.text
            item_id = item.id
            all_categories_dict[item_text] = item_id
            logger = logging.getLogger('Ошибки нет!')
            logger.debug(f'{item_text} {item_id}')

    # Сохраняю с json
    with open('all_categories_dict_1', 'w', encoding="utf-8") as file:
        json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        #cursor.execute('CREATE TABLE Parser_2 (item_text)')
        cursor.executemany("INSERT INTO Parser_2 (item_text) VALUES (?)", zip(all_categories_dict))
        sqlite_connection.commit()
        print("Запись успешно вставлена в таблицу")

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


async def gather_data_3():

    headers = {"Accept": "*/*",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    url = 'https://2gis.ru/ufa/firm/2393065583018883/tab/reviews'

    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')
        cards = soup.find_all('div', class_='_1i94jn5')
        print(cards)

        all_categories_dict = {}
        for item in cards:
            item_text = 'Третий филиал. Отзыв сайта "Вкусно и Точка!"   ' + item.text
            item_id = item.id
            all_categories_dict[item_text] = item_id
            logger = logging.getLogger('Ошибки нет!')
            logger.debug(f'{item_text} {item_id}')

    # Сохраняю с json
    with open('all_categories_dict_1', 'w', encoding="utf-8") as file:
        json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        #cursor.execute('CREATE TABLE Parser_2 (item_text)')
        cursor.executemany("INSERT INTO Parser_2 (item_text) VALUES (?)", zip(all_categories_dict))
        sqlite_connection.commit()
        print("Запись успешно вставлена в таблицу")

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


async def main():
    await gather_data()
    await gather_data_2()
    await gather_data_3()

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())



