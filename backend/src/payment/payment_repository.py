from .db_factory import get_db


def add_payment(payment):
    sql = ''' insert into payment (user_id, payment_type_id, amount, shamsi_date, description) 
                values (?, ?, ?, ?, ?) '''

    values = (
        payment["user"]["id"],
        payment["type"]["id"],
        payment["amount"],
        payment["date"],
        payment["description"]
    )

    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        return get_payment_by_id(cur.lastrowid)


def edit_payment(payment):
    sql = ''' UPDATE payment set '''
    values = ()
    if payment["amount"]:
        sql += ''' amount = ? '''
        values += (payment["amount"],)
    if payment.get("date") is not None:
        if len(values) > 0:
            sql += ''', '''
        sql += ''' shamsi_date = ? '''
        values += (payment["date"],)
    if payment.get("description"):
        if len(values) > 0:
            sql += ''', '''
        sql += ''' description = ? '''
        values += (payment["description"],)

    sql += ''' where id = ? '''
    values += (payment["id"],)
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        return get_payment_by_id(cur.lastrowid)


def get_payment_by_id(payment_id):
    sql = ''' select * from payment where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (payment_id,))
        return cur.fetchone()


# fixme implement searchable method
def get_payments(name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = ''' select * from payment '''
        if name:
            sql += ''' where name like ? '''
            cur.execute(sql, (name + '%',))
        else:
            cur.execute(sql)
        return cur.fetchall()


def delete_payment(payment_id):
    sql = ''' delete from payment where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (payment_id,))
        conn.commit()
        return cur.lastrowid
