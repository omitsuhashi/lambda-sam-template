import unittest
from handlers.create_user import app


class TestCreateUser(unittest.TestCase):
    def test_app(self):
        body = '{"name": "tester"}'
        res = app.lambda_handler({'body': body}, None)
        self.assertEqual(res['statusCode'], 200)


if __name__ == '__main__':
    unittest.main()
