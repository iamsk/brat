from restful import Api
from restful.basehandler import BaseHandler

api = Api()


class HelloWorld(BaseHandler):
    def real_get(self):
        return {'hello': 'world'}

api.add_handler('/', HelloWorld)

if __name__ == '__main__':
    api.run()
