from settings import *
import psycopg2

conn = psycopg2.connect(
    host=ip,
    port=port,

    database=db_name,
    user=user_name,
    password=password)

cursor = conn.cursor()
cursor.execute("Insert into region (name) values \
('Toshkent shahri'),\
('Toshkent viloyati');")

for row in cursor:
    print(*row)
