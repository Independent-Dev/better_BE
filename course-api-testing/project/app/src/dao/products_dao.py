from attr import s
from app.src.utilities.dbUtility import DBUtility
import random

class ProductDAO:
    def __init__(self) -> None:
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):
        sql = 'select * from local.wp_posts where post_type = "product" limit 5000'
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, qty)

    def get_product_by_id(self, id):
        sql = f'select * from local.wp_posts where id = {id}'
        return self.db_helper.execute_select(sql)

    def get_products_created_after_given_date(self, date):
        sql = f'select * from local.wp_posts where post_type = "product" and post_date > "{date}"'
        return self.db_helper.execute_select(sql)