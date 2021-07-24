import os, json
from app.src.utilities.wooAPIUtility import WooAPIUtility
from app.src.dao.orders_dao import OrdersDAO

class OrdersHelper:
    def __init__(self) -> None:
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooAPIUtility()

    # 여기서 additional_args의 default로 {}를 주면 문제가 생김
    def create_order(self, additional_args=None):
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as f:
            payload = json.load(f)
        
        if additional_args:
            assert isinstance(additional_args, dict), "parameter must be dictionary"
            payload.update(additional_args)

        return self.woo_helper.post('orders', params=payload)

    def verify_order_is_created(self, order_json, exp_cust_id, exp_products):
        order_dao = OrdersDAO()
        assert order_json, 'order json must not be empty'
        assert order_json['customer_id'] == exp_cust_id, f'customer id should be {exp_cust_id} but got {order_json["customer_id"]}'

        # verify db
        line_info = order_dao.get_order_lines_by_order_id(order_json['id'])
        assert line_info, "create order, line item not found in DB"
        line_details = order_dao.get_order_items_details(line_info[0]['order_item_id'])

        # breakpoint()
