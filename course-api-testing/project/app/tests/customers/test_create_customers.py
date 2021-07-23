import pytest
import logging as logger

from app.src.utilities.genericUtilities import generatte_email_and_pw
from app.src.helpers.customers_helper import CustomerHelper
from app.src.dao.customers_dao import CustomersDAO
from app.src.utilities.requestUtility import RequestUtility

@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_success():
    logger.info("Test: Create new customer with emai and password")

    rand_info = generatte_email_and_pw()
    email = rand_info['email']  # 이메일 생성하는 것은 여러 테스트에서 쓰일 것이므로 helper로 만들기
    password = rand_info['password']

    # create payload
    payload = dict(rand_info)  # 이런 식으로 하면 새로운 dict 객체가 만들어짐!!

    # make the call  여기에도 Helper가 필요함.
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(**payload)

    # verify email in the response
    assert cust_api_info['email'] == email, f'Create customer api return wrong email. Email: {email}, '
    assert cust_api_info['first_name'] == ''

    # verify customer is created in database  여기에도 Helper가 필요함.
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, "Create customer response 'id' not same as 'ID' in DB"

@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail():
    # get existing customer
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    req_helper = RequestUtility()
    payload = {"email": existing_email, "password": "Password1"}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)
    
    assert cust_api_info['code'] == 'registration-error-email-exists', f"create customer with existing user 'error code' is not correct. expected: registration-error-email-exists but got {cust_api_info['code']}"
