from pyodbc import connect as py_connect
from yaml import load

with open("server.yaml", "r") as stream:
    credentials = load(stream)["credentials"]
    server = credentials["server"]
    database = credentials["database"]
    uid = credentials["uid"]
    password = credentials["password"]


def connect():
    return py_connect('DRIVER={SQL Server};SERVER=' + server +
                      ';DATABASE=' + database +
                      ';UID=' + uid +
                      ';PWD=' + password +
                      ';Trusted_Connection=yes')
