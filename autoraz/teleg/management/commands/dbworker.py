# coding=utf-8
from vedis import Vedis

db_file = 'db.vdb'

# Установка файла
def set_dbfile(dbfile):
    db_file = dbfile

# Считываем
def get_state(user_id):
    with Vedis(db_file) as db:
        try:
            return db[user_id].decode()
        except KeyError:
            return 0

# Сохраняем
def set_state(user_id, value):
    with Vedis(db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            return False
           
# Считываем
def get_stat(tag):
    with Vedis(db_file) as db:
        try:
            return db[tag].decode()
        except:
            return '0'

# Сохраняем
def set_stat(tag, value):
    with Vedis(db_file) as db:
        try:
            db[tag] = value
            return True
        except:
            return False