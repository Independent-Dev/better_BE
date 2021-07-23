import pytest, logging as logger
from app.src.utilities.requestUtility import RequestUtility
from app.src.dao.products_dao import ProductDAO
from app.src.helpers.products_helper import ProductsHelper

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid24
def test_get_all_products():
    req_obj = RequestUtility()
    rs_api = req_obj.get(endpoint='products')
    logger.debug(f"get_all_product_result: {rs_api}")
    # breakpoint()
    assert rs_api, f"Response of list all products is empty"

@pytest.mark.tcid25
def test_get_product_by_id():
    # get product from db
    rand_product = ProductDAO().get_random_product_from_db()
    rand_product_id = rand_product[0]['ID']
    # make a call
    rs_api = ProductsHelper().get_product_by_id(rand_product_id)
    
    # verify the response
    assert rand_product[0]['post_title'] == rs_api['name'], f"Get product by id returned wrong product."

