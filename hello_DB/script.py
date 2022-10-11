from code import compile_command
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    host="localhost",
    database="airlines",
    user="ashkan",
    password="mapsa1234")

cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS myuser cascade")

cur.execute("""
                CREATE TABLE myuser(
                user_id serial PRIMARY KEY, 
                username VARCHAR ( 50 ) UNIQUE NOT NULL, 
                age INT CHECK(age > 0))
            """
            )

cur.execute("DROP TABLE IF EXISTS product cascade")

cur.execute("""
                CREATE TABLE product(
                product_id serial PRIMARY KEY, 
                name VARCHAR ( 50 ) UNIQUE NOT NULL, 
                price INT CHECK(price > 0),
                qty INT CHECK(qty >= 0),
                category VARCHAR(10) NOT NULL)
            """
            )

cur.execute("DROP TABLE IF EXISTS cart cascade")

cur.execute("""
                CREATE TABLE cart(
                cart_id serial PRIMARY KEY, 
                user_id INT NOT NULL, 
                FOREIGN KEY (user_id) 
                    REFERENCES myuser (user_id))
            """
            )

cur.execute("DROP TABLE IF EXISTS cartItem")

cur.execute("""
                CREATE TABLE cartItem(
                id serial PRIMARY KEY, 
                cart_id INT NOT NULL, 
                product_id INT NOT NULL,
                qty INT CHECK(qty >= 0), 
                FOREIGN KEY (cart_id) 
                    REFERENCES cart (cart_id),
                FOREIGN KEY (product_id) 
                    REFERENCES product (product_id))
            """
            )


cur.execute("""
                INSERT INTO myuser(
                    username, age
                )VALUES ('ashkan', 20), ('asghar', 12)
            """
            )

cur.execute("""
                INSERT INTO product(
                    name, price, qty, category
                )VALUES ('panir', 20000, 10, 'ghaza'), ('pofak', 12000, 5, 'tanagholat'), ('adams', 1000, 30, 'tanagholat')
            """
            )

cur.execute("""
                INSERT INTO cart(
                    user_id
                )VALUES (1), (2), (1)
            """
            )

cur.execute("""
                INSERT INTO cartItem(
                    cart_id, product_id, qty
                )VALUES (1, 1, 3), (1, 2, 3), (2, 1, 3), (3, 3, 2)
            """
            )

conn.commit()
conn.close()