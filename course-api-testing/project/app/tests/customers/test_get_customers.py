import pytest, logging as logger
from app.src.utilities.requestUtility import RequestUtility

@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtility()
    rs_api = req_helper.get('customers')

    assert rs_api, f"Response of list all customers is empty"  # 추가로 테스트를 작성할 수도 있을 것. 몇 명의 customer가 있는지 등...
