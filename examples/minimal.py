from brat import Brat
from brat import BratHandler

brat = Brat()


class HelloWorld(BratHandler):
    def get(self):
        return {'hello': 'world'}

brat.add_handler('/', HelloWorld)

if __name__ == '__main__':
    brat.run()
