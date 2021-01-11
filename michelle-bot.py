from fbchat import Client, log, models
from epicpath import EPath
import json
import random
import time
import getpass

with open(EPath('data', 'users.json'), 'r') as f:
    users = json.load(f)


class MichelleBot(Client):
    """

    """

    def sleep(self):
        time.sleep(random.uniform(3, 10))

    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=models.ThreadType.USER,
                  **kwargs):
        """

        :param author_id:
        :param message_object:
        :param thread_id:
        :param thread_type:
        :param kwargs:
        :return:
        """

        if author_id == users['michelle']:
            self.sleep()
            self.reactToMessage(
                message_id=message_object.uid,
                reaction=models.MessageReaction.ANGRY
            )


if __name__ == '__main__':
    email = input('Email: ')
    password = getpass.getpass()
    bot = MichelleBot(email=email, password=password)
    bot.listen()
