from app.src.utilities.genericUtilities import generatte_email_and_pw
from app.src.utilities.requestUtility import RequestUtility


class CustomerHelper:
    def __init__(self) -> None:
        self.request_utilities = RequestUtility()

    def create_customer(self, email=None, password='Password1', **kwargs):
        if not email:
            res = generatte_email_and_pw()
            email = res['email']

        payload = {'email': email, 'password': password}
        print(payload)
        payload.update(kwargs)

        return self.request_utilities.post('customers', payload=payload, expected_status_code=201)

