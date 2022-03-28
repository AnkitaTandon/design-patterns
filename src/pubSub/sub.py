

class Subscriber(object):
 
    def __init__(self, id_):
        self.id_ = id_
 
    def update(self, data):
        print('subscriber {0} got \'{1}\''.format(self.id_, data), )

