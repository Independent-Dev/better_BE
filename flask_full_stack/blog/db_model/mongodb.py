import pymongo

ip_address = 'localhost'
connection = pymongo.MongoClient('mongodb://%s' % (ip_address))

def conn_mongodb():
    try:
        connection.admin.command('ismaster')
    except:
        connection = pymongo.MongoClient('mongodb://%s' % (ip_address))

    return connection.blog_session_db.blog_ab