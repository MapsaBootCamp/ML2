import psycopg2
import psycopg2.extras

# Connect to your postgres DB
conn = psycopg2.connect(
    host="localhost",
    database="airlines",
    user="ashkan",
    password="mapsa1234")

# Open a cursor to perform database operations
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# find users
cur.execute("SELECT * FROM myuser")

# Retrieve query results
records = cur.fetchall()

# print("users: \n", [record["username"] for record in records])

########################## aggregation
# average price product

cur.execute("SELECT category, avg(price) AS price_ave, sum(price) as sum_products FROM product WHERE name LIKE 'p%' GROUP BY category")
result = cur.fetchall()
print([dict(res) for res in result])
