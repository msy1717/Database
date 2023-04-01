# copyright 2022 (@kaif-00z)

import firebase_admin
from firebase_admin import credentials, db

LOGS.info("Trying to connect with db")
if not Var.FIREBASE_SERVICE_ACCOUNT_FILE.startswith(
    "https://"
) and not Var.FIREBASE_SERVICE_ACCOUNT_FILE.endswith(".json"):
    LOGS.info("firebase service account file link is wrong !")
    exit()

if os.path.exists("serviceAccountKey.json"):
    os.remove("serviceAccountKey.json")

os.system(f"wget {Var.FIREBASE_SERVICE_ACCOUNT_FILE} -O serviceAccountKey.json")

try:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {"databaseURL": Var.FIREBASE_URL})
    fdB = db.reference(Var.FIREBASE_DIR)
    LOGS.info("Successfully Connected With Database..")
except BaseException:
    try:
        cred = credentials.Certificate("serviceAccountKey.json")
        fdB = db.reference(Var.FIREBASE_DIR)
        LOGS.info("Successfully Connected With Database..")
    except Exception as ero:
        LOGS.info(str(ero))
        exit()


class fireDB:
    def __init__(self):
        self.db = fdB

    def __repr__(self):
        return f"<FireBaseDB\n -total_keys: {len(self.keys())}\n>"

    def getall(self):
        return self.db.get()

    def keys(self):
        return list(self.db.get().keys())

    def get(self, key):
        return self.db.child(key).get()

    def set(self, key, value):
        return self.db.update({str(key): value})

    def delete(self, key):
        _data = self.getall()
        if key in _data:
            _data.pop(key)
            return self.db.set(_data)
        return False

    def flushall(self):
        return self.db.delete()
