import enum
from typing import List
import mysql.connector


# Opening JSON file


class BodyShapeType(enum.Enum):
    shredded = 1
    fit = 2
    average = 3
    above_average = 4


class BodyShape(enum.Enum):
    shredded = 1
    fit = 2
    average = 3
    above_average = 4


class Taste:

    def __init__(self, location, select_box, closet: Item, returns,
                 description):
        self.returns = returns
        self.closet = closet
        self.description = description
        self.select_box = select_box
        self.location = location


class User:

    def __int__(self, name: str, height: int, weight: int, body_shape):
        self.name = name
        self.height = height
        self.weight = weight
        self.body_shape = body_shape


if __name__ == '__main__':
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234huji"
    )
    cursor = conn.cursor()

    create_user_sql = '''CREATE TABLE USER(
       FIRST_NAME VARCHAR(20) NOT NULL,
       PASSWORD VARCHAR(20) NOT NULL,
       HEIGHT INT,
       WEIGHT INTEGER,
       BODY_SHAPE VARCHAR(20)
    )'''

    cursor.execute("CREATE DATABASE IF NOT EXISTS huji")
    cursor.execute("USE huji")
    cursor.execute(create_user_sql)
    conn.close()
