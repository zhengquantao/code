import pymysql
from settings import Config

def connect():
    conn = Config.POOL.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor

def close(conn, cursor):
    cursor.close()
    conn.close()

def fetch_one(sql,args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    sql_mes = cursor.fetchone()
    close(conn, cursor)
    return sql_mes

def fetch_all(sql,args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    sql_mes = cursor.fetchall()
    close(conn, cursor)
    return sql_mes

def insert_m(sql, args):
    conn, cursor = connect()
    cursor.execute(sql, args)
    conn.commit()
    close(conn, cursor)
