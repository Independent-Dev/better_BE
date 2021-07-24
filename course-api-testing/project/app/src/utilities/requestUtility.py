import os, json, requests
import logging as logger
from app.src.configs.hosts_config import API_HOST
from app.src.utilities.credentialsUtility import CredentialsUtility
from requests_oauthlib import OAuth1



class RequestUtility:
    def __init__(self) -> None:
        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOST[self.env]
        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

    def assert_status_code(self):
        assert self.rs_status_code == self.expected_status_code, f"Bad Status code. Expected {self.expected_status_code}, Actual status code: {self.rs_status_code}, URL: {self.url}, Response Json: {self.rs_json}"
    
    def post(self, endpoint, payload=None, headers=None, expected_status_code=201):
        if not headers:
            headers = {'Content-Type': "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.post(url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.rs_status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.url = url
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API POST response: {self.rs_json}")
        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {'Content-Type': "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.get(url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.rs_status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.url = url
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API GET response: {self.rs_json}")
        return self.rs_json
