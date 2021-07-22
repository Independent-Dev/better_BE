from app.src.utilities.dbUtility import DBUtility


class CustomersDAO:
    def __init__(self) -> None:
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * from local.wp_users where user_email='{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql