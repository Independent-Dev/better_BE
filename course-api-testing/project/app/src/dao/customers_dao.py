from app.src.utilities.dbUtility import DBUtility
import random

class CustomersDAO:
    def __init__(self) -> None:
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * from local.wp_users where user_email='{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_random_customer_from_db(self, qty=1):
        sql = 'select * from local.wp_users order by id desc limit 5000'
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, qty)