import pymysql, os
import logging as logger
from app.src.configs.hosts_config import DB_HOST
from app.src.utilities.credentialsUtility import CredentialsUtility


class DBUtility:

    def __init__(self) -> None:
        self.machine = os.environ.get('MACHINE')
        assert self.machine, "environ variable 'machine' must be set"
        
        self.wp_host = os.environ.get('WP_HOST')
        assert self.wp_host, "environ variable 'machine' must be set"
        
        if self.machine == 'docker' and self.wp_host == 'local':
            raise Exception(f"Can not run test in docker if WP_HOST is local")
        
        self.env = os.environ.get('ENV', 'test')

        self.host = DB_HOST[self.machine][self.env]['host']
        self.socket = DB_HOST[self.machine][self.env]['socket']
        self.port = DB_HOST[self.machine][self.env]['port']
        self.database = DB_HOST[self.machine][self.env]['database']
        self.table_prefix = DB_HOST[self.machine][self.env]['table_prefix']
        # self.socket = '/Users/jonathan/Library/Application Support/Local/run/8Tx4d8szF/mysql/mysqld.sock'
        self.creds = CredentialsUtility.get_db_credentials()

    def create_connection(self):
        if self.wp_host == 'local':
            connection = pymysql.connect(
                host=self.host, 
                user=self.creds['db_user'], 
                password=self.creds['db_password'],
                unix_socket=self.socket
            )
        elif self.wp_host == 'ampps':
            connection = pymysql.connect(
                host=self.host, 
                user=self.creds['db_user'], 
                password=self.creds['db_password'],
                port=self.port
            )
        else:
            raise Exception("Unknown WP_HOST")
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