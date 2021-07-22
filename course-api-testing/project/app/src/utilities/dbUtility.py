import pymysql
import logging as logger
from app.src.utilities.credentialsUtility import CredentialsUtility


class DBUtility:
    def __init__(self) -> None:
        self.host = 'localhost'
        self.socket = '/Users/jonathan/Library/Application Support/Local/run/8Tx4d8szF/mysql/mysqld.sock'
        self.creds = CredentialsUtility.get_db_credentials()

    def create_connection(self):
        connection = pymysql.connect(
            host=self.host, 
            user=self.creds['db_user'], 
            password=self.creds['db_password'],
            unix_socket=self.socket
        )
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            logger.debug(f"executing sql: {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)  # 일종의 session 같은 것
            cur.execute(sql)
            rs_dict = cur.fetchall()
            
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)}")
        finally:
            cur.close()
        
        return rs_dict

    def execute_sql(self, sql):
        pass