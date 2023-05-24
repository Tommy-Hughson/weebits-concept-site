import sqlite3
import csv

DATABASE = "flask-site\static\other\site.db"

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


# Write code here
r = dict()

with open("flask-site\static/other/weebits_product_list.csv", "r") as file:
    content = csv.DictReader(file)
    for row in content:
        value = [row["Image Src"], row["Handle"]]
        if value[1] not in r:
            r[value[1]] = value[0]
print(r.values())

for k, v in r.items():            
    update("update product set image = ? where product_id = ?", v, k)
