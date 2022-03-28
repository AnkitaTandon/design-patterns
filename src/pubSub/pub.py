class Publisher(object):

    def __init__(self):
        self.subscriptions = {}

    def subscribe(self, subscriber, topic):

        if topic not in self.subscriptions :
            self.subscriptions[topic] = []
        if subscriber not in self.subscriptions[topic]:
            self.subscriptions[topic].append(subscriber)

        print('\n\nsubscribing {0} to topic \'{1}\''.format(subscriber.id_, topic))

    def publish(self, data, topic):

        print('\n\npublishing \'{0}\' in topic \'{1}\''.format(data, topic ))
        for subscriber in self.subscriptions[topic]:
            subscriber.update(data)



