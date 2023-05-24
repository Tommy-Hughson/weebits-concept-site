import sqlite3
from flask import Flask, render_template
# from flask_bcrypt import Bcrypt

DATABASE = "static\other\site.db"
app = Flask("__main__")
# bcrypt = Bcrypt(app)
# app.secret_key = "alkjaslkgjwleakhg lkwhlhwlklkhw"

# Temporay to immediately print to console.
def aprint(x):
    """Temporary"""
    print(x, flush=True)

def connect(db_file):
    """
    Returns a connection to the database.
    """
    try:
        # Create the connection to the database.
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        # Print the sqlite error, e, to the console.
        print(e)
        return None


def fetchall(query, *arg):
    """
    To fetch data from database.
    query: A SQL select query.
    arg: Values for query.
    returns: Information from database with regard to query.
    """
    # Create connection to the database.
    con = connect(DATABASE)
    # Create cursor to access the data in database.
    cur = con.cursor()
    cur.execute(query, arg)
    # Fetch all the data from the database at the query arguments.
    data = cur.fetchall()
    # Close the connection to the database.
    con.close()
    return data


def execute(query, *arg):
    """
    To alter the database using either a INSERT, UPDATE or DELETE query.
    query: An INSERT, UPDATE or DELETE SQL query.
    arg: SQL arguments.
    returns: Nothing.
    """
    # Create a connection to the database.
    con = connect(DATABASE)
    # Create a cursor to access the data in the database.
    cur = con.cursor()
    # Execute the changes made in the database by the query.
    cur.execute(query, arg)
    # Commit these changes in the database.
    con.commit()
    con.close()


# Make the function name more specific for the type of execution the query is doing.
insert = update = delete = execute


@app.errorhandler(404)
def render_error(e):
    # print the error to connsole
    aprint(e)
    return render_template("404.html")


@app.route("/")
def render_main():
    # Get feature products
    # get_products = ['baby-leggings', 'sheepskin-play-rug', 'chunky-knit-boots', 'travel-rug']
    # feature_products = [fetchall("SELECT name, image, price from product where product_id = ?", product_name)[0] for product_name in get_products]
    # aprint(feature_products)
    return render_template("index.html")


@app.route("/collections/")
@app.route("/collections/<collection>")
def render_collection(collection=None):
    products = fetchall("SELECT name, image, price, product_id from product")
    aprint(products)
    return render_template("collection.html", products=products)

@app.route("/products/<product>")
def render_product(product):
    info = fetchall("SELECT name, image, price from product where product_id = ?", product)
    return render_template("product.html", info=info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
