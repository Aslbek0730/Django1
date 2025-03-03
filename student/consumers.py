from channels.consumer import SyncConsumer


class studentConsumer(SyncConsumer):

    def app1_message(self, message):
        # do something with message
        pass