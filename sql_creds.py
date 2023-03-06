import json

# DB Credentials
DATABASE = ""
DB_USERNAME = ""
DB_PASSWORD = ""
HOST = ""
PORT = ""
DB_NAME = ""

with open('sql_creds.json') as f:
    data = json.load(f)
    # print(data)
    DATABASE = data["database"]
    DB_USERNAME = data["db_un"]
    DB_PASSWORD = data["db_pw"]
    HOST = data["host"]
    PORT = data["port"]
    DB_NAME = data["db_name"]

# print("Printing DB Credentials...")
# print(DATABASE)
# print(DB_USERNAME)
# print(DB_PASSWORD)
# print(HOST)
# print(PORT)
# print(DB_NAME)
