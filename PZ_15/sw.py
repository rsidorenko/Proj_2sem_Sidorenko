from numpy import printoptions
import sqlite3 as sq
from inf_bd import info_stores
from inf_bd import info_items
from inf_bd import info_store_requests
from inf_bd import info_stock
from inf_bd import info_composition

with sq.connect("wholesale_warehouse.db") as con:
    con.execute("""CREATE TABLE IF NOT EXISTS items(
            it_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR NOT NULL,
            information VARCHAR,
            unit VARCHAR
            )""")

with sq.connect("wholesale_warehouse.db") as con:
    con.execute("""CREATE TABLE IF NOT EXISTS stores(
            st_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR,
            addresses_stores VARCHAR,
            phone_number VARCHAR
            )""")

with sq.connect("wholesale_warehouse.db") as con:
    con.execute("""CREATE TABLE IF NOT EXISTS store_requests(
            req_id INTEGER PRIMARY KEY AUTOINCREMENT,
            st_id INTEGER,
            dates_requests DATE,
            FOREIGN KEY (st_id) REFERENCES stores(st_id) ON DELETE CASCADE ON UPDATE CASCADE
            )""")

with sq.connect("wholesale_warehouse.db") as con:
    con.execute("""CREATE TABLE IF NOT EXISTS stock(
            stock_id INTEGER PRIMARY KEY,
            it_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY (it_id) REFERENCES items(it_id) ON DELETE CASCADE ON UPDATE CASCADE
            )""")

with sq.connect("wholesale_warehouse.db") as con:
    con.execute("""CREATE TABLE IF NOT EXISTS composition(
            comp_id INTEGER PRIMARY KEY,
            req_id INTEGER,
            it_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY (req_id) REFERENCES store_requests(req_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (it_id) REFERENCES items(it_id) ON DELETE CASCADE ON UPDATE CASCADE
            )""")

with sq.connect("wholesale_warehouse.db") as con:
    cur = con.cursor()
    con.executemany("INSERT INTO items VALUES (?, ?, ?, ?)", info_items)

with sq.connect("wholesale_warehouse.db") as con:
    cur = con.cursor()
    con.executemany("INSERT INTO stores VALUES (?, ?, ?, ?)", info_stores)

with sq.connect("wholesale_warehouse.db") as con:
    cur = con.cursor()
    con.executemany("INSERT INTO store_requests VALUES (?, ?, ?)", info_store_requests)

with sq.connect("wholesale_warehouse.db") as con:
    cur = con.cursor()
    con.executemany("INSERT INTO stock VALUES (?, ?, ?)", info_stock)

with sq.connect("wholesale_warehouse.db") as con:
    cur = con.cursor()
    con.executemany("INSERT INTO composition VALUES (?, ?, ?, ?)", info_composition)

                            #SELECT'ы

#1

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT title, information FROM items")
#     res = cur.fetchall()
# print(res)

#2

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT title, addresses_stores FROM stores")
#     res = cur.fetchall()
# print(res)

#3

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT stores.title, store_requests.dates_requests FROM stores INNER JOIN store_requests ON stores.st_id = store_requests.st_id")
#     res = cur.fetchall()
# print(res)

#4

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT items.title, stock.quantity FROM items INNER JOIN stock ON items.it_id = stock.it_id")
#     res = cur.fetchall()
# print(res)

#5

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT items.title, stock.quantity FROM items INNER JOIN stock ON items.it_id = stock.it_id ORDER BY stock.quantity DESC")
#     res = cur.fetchall()
# print(res)

#6

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT store_requests.req_id, stores.title, items.title FROM store_requests JOIN stores ON store_requests.st_id = stores.st_id JOIN composition ON store_requests.req_id = composition.req_id JOIN items ON composition.it_id = items.it_id")
#     res = cur.fetchall()
# print(res)

#7

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM store_requests WHERE dates_requests BETWEEN '2023-01-01' AND '2023-04-16'")
#     res = cur.fetchall()
# print(res)

#8

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT stores.title FROM stores JOIN stock ON stores.st_id = stock.stock_id GROUP BY stores.st_id HAVING SUM(stock.quantity) < 10")
#     res = cur.fetchall()
# print(res)

#9

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("SELECT title FROM stock JOIN items ON stock.it_id = items.it_id WHERE quantity < 10")
#     res = cur.fetchall()
# print(res)

                        #UPDAT'ы

#1

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE stock SET quantity = 30 WHERE it_id = 2")

#2

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE composition SET it_id = 3 WHERE it_id = 2")

#3

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE composition SET quantity = 10 WHERE it_id = 1")

#4

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE stores SET addresses_stores = 'ул. ГВидона ХМельницкого, д. 15' WHERE st_id = 2")

#5

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE store_requests SET dates_requests = '2023-03-28' WHERE st_id = 1")

#6

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE stock SET quantity = 100 WHERE stock_id in (1, 2)")

#7

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE items SET information = 'SWAGA' WHERE it_id = 1")
#     cur.execute("UPDATE stock SET quantity = 100 WHERE stock_id = 1")

#10

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE stores SET title = 'Gera', addresses_stores = 'ул. Артема, д. 15' WHERE st_id = 1")

#11

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE store_requests SET st_id = 2 WHERE st_id = 1")

#12

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE stores SET addresses_stores = 'ул. Вагулина' WHERE st_id = 1")
#     cur.execute("UPDATE composition SET quantity = 30 WHERE comp_id = 1")

#13

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("UPDATE items SET information = 'UWU' WHERE it_id in (1, 2)")
#     cur.execute("UPDATE stock SET quantity = 30 WHERE it_id in (1, 2)")

                            #DELETE'ы

#4

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM store_requests WHERE st_id IN (SELECT st_id FROM stores WHERE addresses_stores LIKE 'ул. Ленина%')")
#     res = cur.fetchall()
# print(res)

#5

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM composition WHERE composition.it_id IN (SELECT composition.it_id FROM composition INNER JOIN stock ON composition.it_id = stock.it_id WHERE stock.quantity = 0)")
#     res = cur.fetchall()
# print(res)

#6

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM stores WHERE stores.st_id IN (SELECT stores.st_id FROM stores INNER JOIN store_requests ON stores.st_id = store_requests.st_id WHERE store_requests.dates_requests BETWEEN '2023-02-01' AND '2023-02-30')")
#     res = cur.fetchall()
# print(res)

#7

# with sq.connect("wholesale_warehouse.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM stores WHERE stores.st_id IN (SELECT stores.st_id FROM stores INNER JOIN store_requests ON stores.st_id = store_requests.st_id WHERE store_requests.dates_requests BETWEEN '2023-02-01' AND '2023-02-30')")
#     res = cur.fetchall()
# print(res)
