import sqlite3

from flask import g
DATABASE = "backend/src/financial.db"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        print("Database is not initialized")
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = make_dicts
    else:
        print("Database connection fetched from g")
    return db


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))
