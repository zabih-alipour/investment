import sqlite3

from utils import dict_factory

db_path = "./financial.db"


def add_user(user):
    sql = ''' INSERT INTO user ("name") VALUES (?) '''
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(sql, (user.get('name'),))
        conn.commit()
        return cur.lastrowid


def get_user(user_id):
    sql = ''' select * from user where id = ? '''
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        return cur.fetchone()


def get_users(name):
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        sql = ''' select * from user '''
        if name:
            sql += ''' where name like ? '''
            cur.execute(sql, (name,))
        else:
            cur.execute(sql)
        return cur.fetchall()
