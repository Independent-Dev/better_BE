import pytest
from app.src.dao.products_dao import ProductDAO
from app.src.helpers.orders_helper import OrdersHelper
from app.src.helpers.customers_helper import CustomerHelper

pytestmark = [pytest.mark.smoke, pytest.mark.orders]

@pytest.fixture
def my_orders_smoke_setup(scope='module'):
    # get a product from db
    rand_product = ProductDAO().get_random_product_from_db(1)
    
    product_id = rand_product[0]['ID']
    info = {'product_id': product_id}
    return info


@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_orders_smoke_setup):
    my_orders_smoke_setup
    # make a call
    info = {
        "line_items": [
            {
                "product_id": my_orders_smoke_setup['product_id'],
                "quantity": 1
            }
        ]
    }
    order_json = OrdersHelper().create_order(additional_args=info)
    # breakpoint()
    # verify response
    expected_products = [{'product_id': my_orders_smoke_setup['product_id']}]
    OrdersHelper().verify_order_is_created(order_json, 0, expected_products)

@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(my_orders_smoke_setup):
    product_id = my_orders_smoke_setup['product_id']
    # make a call
    cust_info = CustomerHelper().create_customer()
    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ],
        'customer_id': cust_info['id']
    }
    order_json = OrdersHelper().create_order(additional_args=info)
    # breakpoint()
    # verify response
    expected_products = [{'product_id': product_id}]
    OrdersHelper().verify_order_is_created(order_json, cust_info['id'], expected_products)