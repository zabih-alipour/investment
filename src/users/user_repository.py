from .db_factory import get_db


def add_user(user):
    sql = ''' INSERT INTO user ("name") VALUES (?) '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, tuple(user.values()))
        conn.commit()
        return get_user_by_id(cur.lastrowid)


def edit_user(user):
    sql = ''' UPDATE user set name = ? where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (user["name"], user["id"],))
        conn.commit()
        return get_user_by_id(cur.lastrowid)


def get_user_by_id(user_id):
    sql = ''' select * from user where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        return cur.fetchone()


def get_users(name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = ''' select * from user '''
        if name:
            sql += ''' where name like ? '''
            cur.execute(sql, (name + '%',))
        else:
            cur.execute(sql)
        return cur.fetchall()


def delete_user(user_id):
    sql = ''' delete from user where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        conn.commit()
        return cur.lastrowid
