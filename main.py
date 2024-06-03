import asyncio
import asyncpg

from typing import List, Tuple, Union
from random import sample


def load_common_words():
    with open("common_words.txt") as common_words:
        return common_words.readlines()


def generate_brand_names(words: List[str]):
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection):
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)


async def main():
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        database="products",
        password="admin",
    )
    common_words = load_common_words()

    await insert_brands(common_words, connection)


asyncio.run(main())
