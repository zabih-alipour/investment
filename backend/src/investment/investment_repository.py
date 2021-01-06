from .db_factory import get_db


def add_investment(investment):
    sql = ''' INSERT INTO investment ("name") VALUES (?) '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, tuple(investment.values()))
        conn.commit()
        return get_investment_by_id(cur.lastrowid)


def edit_investment(investment):
    sql = ''' UPDATE investment set name = ? where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (investment["name"], investment["id"],))
        conn.commit()
        return get_investment_by_id(cur.lastrowid)


def get_investment_by_id(investment_id):
    sql = ''' select * from investment where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (investment_id,))
        return cur.fetchone()


def get_investments(name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = ''' select * from investment '''
        if name:
            sql += ''' where name like ? '''
            cur.execute(sql, (name + '%',))
        else:
            cur.execute(sql)
        return cur.fetchall()


def delete_investment(investment_id):
    sql = ''' delete from investment where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (investment_id,))
        conn.commit()
        return cur.lastrowid
