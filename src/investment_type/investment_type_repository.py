from .db_factory import get_db


def add_investment_type(investment_type):
    sql = ''' INSERT INTO investment_type ("name") VALUES (?) '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, tuple(investment_type.values()))
        conn.commit()
        return get_investment_type_by_id(cur.lastrowid)


def edit_investment_type(investment_type):
    sql = ''' UPDATE investment_type set name = ? where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (investment_type["name"], investment_type["id"],))
        conn.commit()
        return get_investment_type_by_id(cur.lastrowid)


def get_investment_type_by_id(investment_type_id):
    sql = ''' select * from investment_type where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (investment_type_id,))
        return cur.fetchone()


def get_investment_types(name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = ''' select * from investment_type '''
        if name:
            sql += ''' where name like ? '''
            cur.execute(sql, (name + '%',))
        else:
            cur.execute(sql)
        return cur.fetchall()


def delete_investment_type(investment_type_id):
    sql = ''' delete from investment_type where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (investment_type_id,))
        conn.commit()
        return cur.lastrowid
