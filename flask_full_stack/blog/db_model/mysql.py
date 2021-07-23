import pymysql

db_conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='blog_db',
    charset='utf8'
)

def conn_mysqldb():
    if not db_conn.open:
        db_conn.ping(reconnect=True)
    return db_conn