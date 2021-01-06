from .db_factory import get_db


def add_payment_type(payment_type):
    sql = ''' INSERT INTO payment_type ("name", "category_id") VALUES (?, ?) '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, tuple(payment_type.values()))
        conn.commit()
        return get_payment_type_by_id(cur.lastrowid)


def edit_payment_type(payment_type):
    sql = ''' UPDATE payment_type set name = ? where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (payment_type["name"], payment_type["id"],))
        conn.commit()
        return get_payment_type_by_id(cur.lastrowid)


def get_payment_type_by_id(payment_type_id):
    sql = ''' select * from payment_type where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (payment_type_id,))
        return cur.fetchone()


def get_payment_types(name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = ''' select * from payment_type '''
        if name:
            sql += ''' where name like ? '''
            cur.execute(sql, (name + '%',))
        else:
            cur.execute(sql)
        return cur.fetchall()


def delete_payment_type(payment_type_id):
    sql = ''' delete from payment_type where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (payment_type_id,))
        conn.commit()
        return cur.lastrowid
