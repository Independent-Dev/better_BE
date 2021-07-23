from app.src.utilities.requestUtility import RequestUtility
import logging as logger

class ProductsHelper:
    def __init__(self) -> None:
        self.request_utilities = RequestUtility()

    def get_product_by_id(self, product_id):
        return self.request_utilities.get(f'products/{product_id}')
    
    def call_create_product(self, payload):
        return self.request_utilities.post('products', payload=payload, expected_status_code=201)

    def call_list_products(self, payload=None):
        max_pages = 1000
        all_products = []
        if not 'per_page' in payload.keys():
            payload['per_page'] = 100
        for i in range(1, max_pages + 1):
            payload['page'] = i
            rs_api = self.request_utilities.get('products', payload=payload)
            if not rs_api:
                break
            all_products.extend(rs_api)
        else:
            raise Exception(f"unable to find all products after {max_pages} page")
        return all_products