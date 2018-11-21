from passlib.hash import pbkdf2_sha256 as sha256
from athlete.databaser import connect
# Connects to the login database using databaser.py
connection = connect()
# Creates a cursor from the connection, which can be used to execute queries
cursor = connection.cursor()


def user_exists(username):
    # SQL Query to be executed by the cursor
    query = "SELECT 1 FROM WebappUsers WHERE Username = ?"
    cursor.execute(query, username)
    return True if cursor.fetchone() is not None else False


# Generates a hash to be stored in the database, based on the password and a generated salt
def generate_hash(password):
    generated_hash = sha256.hash(password)
    return generated_hash


def add_user(username, password):
    if not user_exists(username):
        generated_hash = generate_hash(password)
        query = "INSERT INTO WebappUsers (Username, Hash) VALUES ( ? , ? )"
        cursor.execute(query, (username, generated_hash))


def get_permission_level(username):
    if user_exists(username):
        query = "SELECT PermissionLevel FROM WebappUsers WHERE Username = '" + username + "'"
        cursor.execute(query)
        fetch = cursor.fetchone()
        return fetch[0]
    else:
        return 0


# Checks a password against a parsed hash to verify that the password is correct.
# This hash should come from the login database and the users table
def verify_password(username, password):
    # SQL Query to be executed by the cursor
    query = "SELECT Hash FROM WebappUsers WHERE Username = ?"
    cursor.execute(query, username)
    fetch = cursor.fetchone()
    if fetch is not None:
        generated_hash = fetch[0]
        return sha256.verify(password, generated_hash)
    else:
        return False
