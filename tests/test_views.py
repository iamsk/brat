import unittest
from brat import Brat
from brat import BratHandler
from tornado.testing import AsyncHTTPTestCase


class HelloWorld(BratHandler):
    def get(self):
        return {'hello': 'world'}


class Test(AsyncHTTPTestCase):
    def get_app(self):
        brat = Brat()
        brat.add_handler('/', HelloWorld)
        self.app = brat.get_app()
        return self.app

    def test_get(self):
        request_url = '/'
        response = self.fetch(request_url)
        self.assertEqual(response.code, 200)


if __name__ == '__main__':
    testsuite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(testsuite)
