# support above python3.9.7
# < (c) 2022 @kaif-00z >


# pip3 install pymongo[srv]


from time import time
from pymongo import MongoClient

class Var:
    DB_NAME = ""
    COLL_NAME = ""
    URI = ""


class MongoDb:
    def __init__(self, uri):
        self.DATABASE = MongoClient(uri)
        self.db = self.DATABASE[Var.DB_NAME][Var.COLL_NAME]

    def set(self, key, value):
        if not self.get(key):
            self.db.insert_one({"_id": key, "value": value})
            return True
        return False

    def original_set(self, set):
        m = set["_id"]
        if not self.get(m):
            self.db.insert_one(set)
            return True
        return False

    def get(self, key):
        return self.db.find_one({"_id": key})

    def delete(self, key):
        if self.get(key):
            self.db.delete_one({"_id": key})
            return True
        return False

    def getall(self):
        return list(self.db.find({}))

    def ping(self):
        x = time()
        self.sysinfo()
        return time() - x

    def flushall(self, drop=None):
        if not drop:
            return self.db.delete_many({})
        self.db.drop()

    def usage(self):
        return self.DATABASE[Var.DB_NAME].command("dbstats")["dataSize"]

    def sysinfo(self):
        return self.DATABASE.server_info()


def simplify(dict):
    key = dict["_id"]
    value = dict["value"]
    return key, value

try:
    dB = MongoDb(Var.URI)
except Exception as e:
    print(e)
