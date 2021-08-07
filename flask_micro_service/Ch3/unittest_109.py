import unittest, json, sys
sys.path.append("/Users/jonathan/study/better_BE/flask_micro_service/Ch2")
from flask_basic import app

class TestApp(unittest.TestCase):
    def test_help(self):
        app.testing = True
        client = app.test_client()

        hello = client.get('/test')
        print(dir(hello), type(hello))
        body = json.loads(str(hello.data, 'utf-8'))
        self.assertEqual(body["Hello"], 'World')

if __name__ == '__main__':
    unittest.main()