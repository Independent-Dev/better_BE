import os, logging as logger
from app.src.utilities.credentialsUtility import CredentialsUtility
from woocommerce import API
from app.src.configs.hosts_config import WOO_API_HOST


class WooAPIUtility:
    def __init__(self) -> None:
        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOST[self.env]
        self.wcapi = API(
            url=WOO_API_HOST[self.env],
            consumer_key=wc_creds['wc_key'],
            consumer_secret=wc_creds['wc_secret'],
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.rs_status_code == self.expected_status_code, f"Bad Status code. Expected {self.expected_status_code}, Actual status code: {self.rs_status_code}, URL: {self.url}, Response Json: {self.rs_json}"
    

    def post(self, endpoint, params=None, expected_status_code=201):
        rs_api = self.wcapi.post(endpoint, params)
        self.rs_status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.url = endpoint
        self.rs_json = rs_api.json()
        self.assert_status_code()

        return self.rs_json
    def get(self, endpoint, params=None, expected_status_code=200):
        rs_api = self.wcapi.get(endpoint, params=params)
        self.rs_status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.url = endpoint
        self.rs_json = rs_api.json()
        self.assert_status_code()

        return self.rs_json

if __name__ == '__main__':
    rs_api = WooAPIUtility().get('products')
    breakpoint()
