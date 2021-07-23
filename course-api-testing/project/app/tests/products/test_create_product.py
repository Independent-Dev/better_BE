import pytest
from app.src.utilities.genericUtilities import generate_rand_str
from app.src.helpers.products_helper import ProductsHelper
from app.src.dao.products_dao import ProductDAO

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid26
def test_create_1_simple_product():
    # generate some data
    payload = {'name': generate_rand_str(20), 'type': 'simple', 'regular_price': "10.99"}
    # make a call
    product_rs = ProductsHelper().call_create_product(payload)

    # verify the response is not empty
    assert product_rs, "create product api response is empty"
    assert payload['name'] == product_rs['name']

    # verify the product exists in DB
    db_product = ProductDAO().get_product_by_id(product_rs['id'])
    assert db_product[0]['post_title'] == payload['name'], f"name does not match. created name: {payload['name']}, db name: {db_product['post_title']}"


