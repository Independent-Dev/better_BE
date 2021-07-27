import pytest, logging
from app.src.helpers.orders_helper import OrdersHelper
from app.src.utilities.wooAPIUtility import WooAPIUtility

pytestmark = [pytest.mark.orders, pytest.mark.regression]

# paramatrize 예시
# 정석으로 한다면 두 개의 테스트 테이스를 모두 실행시키고 싶은 경우 pytest -m test_0727로 하는 게 맞는 것 같지만
# pytest -m parametrize로 해도 두 개 모두 실행되기는 함.
@pytest.mark.test_0727
@pytest.mark.parametrize("new_status", [
    pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.ex_list]),
    pytest.param('completed', marks=pytest.mark.tcid56),
    pytest.param('on-hold', marks=pytest.mark.tcid57)
    ])
def test_update_order_status(new_status):
    logging.debug(f"new_status: {new_status}")
    # create order
    order_helper = OrdersHelper()
    order_json = OrdersHelper().create_order()
    cur_status = order_json['status']
    assert cur_status != new_status, "status is already equal"

    # update the status
    payload = {'status': new_status}
    rs_update = order_helper.update_order(order_json["id"], payload=payload)

    # get order information
    new_order_info = order_helper.retrieve_order(order_json["id"])
    
    # verifies information
    assert new_status == new_order_info['status']

@pytest.mark.tcid58
def test_update_order_status_to_random_string():
    new_status = 'afadadfa'  # this should be 
    # create order
    order_helper = OrdersHelper()
    order_json = OrdersHelper().create_order()
    cur_status = order_json['status']
    assert cur_status != new_status, "status is already equal"

    # update the status
    payload = {'status': new_status}
    rs_api = WooAPIUtility().put(f'orders/{order_json["id"]}', params=payload,expected_status_code=400)
    logging.debug(f"rs_api['code']: {rs_api['code']}")
    assert rs_api['code'] == 'rest_invalid_param'

