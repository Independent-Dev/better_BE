import pytest
from datetime import datetime, timedelta
from app.src.helpers.products_helper import ProductsHelper
from app.src.dao.products_dao import ProductDAO

@pytest.mark.regression
class TestListProductWithFilter:

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
        # create data
        x_days_from_today = 30
        tmp_date = datetime.now() - timedelta(days=x_days_from_today)
        after_created_date = tmp_date.strftime(f'%Y-%m-%dT%H:%M:%S')

        # make the call
        payload = {'after': after_created_date}
        breakpoint()
        rs_api = ProductsHelper().call_list_products(payload)
        
        # get data from db
        db_products = ProductDAO().get_products_created_after_given_date(after_created_date)

        # verify response

        assert len(rs_api) == len(db_products), f"list products with filter 'after' returned unexpected number of products."
        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]

        assert set(ids_in_api) == set(ids_in_db)