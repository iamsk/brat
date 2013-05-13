import unittest
from restful import Api
from restful.basehandler import BaseHandler
from tornado.testing import AsyncHTTPTestCase


class HelloWorld(BaseHandler):
    def real_get(self):
        return {'hello': 'world'}


class Test(AsyncHTTPTestCase):
    def get_app(self):
        api = Api()
        api.add_handler('/', HelloWorld)
        self.app = api.get_app()
        return self.app

    def test_get(self):
        request_url = '/'
        response = self.fetch(request_url)
        self.assertEqual(response.code, 200)


if __name__ == '__main__':
    testsuite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(testsuite)
