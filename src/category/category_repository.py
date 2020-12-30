from .db_factory import get_db


def add_category(category):
    sql = ''' INSERT INTO category ("name") VALUES (?) '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, tuple(category.values()))
        conn.commit()
        return get_category_by_id(cur.lastrowid)


def edit_category(category):
    sql = ''' UPDATE category set name = ? where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (category["name"], category["id"],))
        conn.commit()
        return get_category_by_id(cur.lastrowid)


def get_category_by_id(category_id):
    sql = ''' select * from category where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (category_id,))
        return cur.fetchone()


def get_categories(name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = ''' select * from category '''
        if name:
            sql += ''' where name like ? '''
            cur.execute(sql, (name + '%',))
        else:
            cur.execute(sql)
        return cur.fetchall()


def delete_category(category_id):
    sql = ''' delete from category where id = ? '''
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(sql, (category_id,))
        conn.commit()
        return cur.lastrowid
