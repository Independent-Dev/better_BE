from woocommerce import API

wcapi = API(
    url="http://mystore.local",
    consumer_key="ck_251265ede1e0855d3ad53a0b1c778eb01c4b22c5",
    consumer_secret="cs_d90d0b6a3814cdc16e7ea9271c1dbfd410ef20e1",
    version="wc/v3"
)

r = wcapi.get('products')
import pprint
pprint.pprint(r.json())