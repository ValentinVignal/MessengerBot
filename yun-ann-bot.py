from fbchat import Client, log, models
from epicpath import EPath
import json
import random
import time
import functools
import langdetect
import getpass

with open(EPath('data', 'users.json'), 'r') as f:
    users = json.load(f)


def is_lang(text, lang):
    lang_list = langdetect.detect_langs(text)
    return functools.reduce(lambda x, y: x or y.lang == lang, lang_list, False)


class YunAnnBot(Client):
    """

    """

    def sleep(self):
        time.sleep(random.uniform(0.5, 2))

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
        bad_words = ['berlin', 'menfred', 'harry', 'style']

        # toggle = self.fetchThreadMessages(thread_id=self.uid, limit=1)  # Own account
        if message_object.text is not None:
            # print('author', author_id, 'message object', message_object, 'threadid', thread_id)
            if author_id == users['yun_ann']:
                # If some bad words are said
                text = message_object.text.lower()
                angry = functools.reduce(lambda x, y: x or y in text, bad_words, False)
                if angry:
                    # Answer it
                    self.sleep()
                    self.send(
                        message=models.Message(text='幹恁娘雞掰', reply_to_id=message_object.uid),
                        thread_id=thread_id,
                        thread_type=thread_type,
                    )
                    # Angry react
                    self.sleep()
                    self.reactToMessage(
                        message_id=message_object.uid,
                        reaction=models.MessageReaction.ANGRY
                    )
                if is_lang(message_object.text, 'es'):
                    # If some Spanish is written
                    self.sleep()
                    self.reactToMessage(
                        message_id=message_object.uid,
                        reaction=models.MessageReaction.ANGRY
                    )
                    self.sleep()
                    self.send(
                        message=models.Message(
                            text='我们说中文',
                            reply_to_id=message_object.uid
                        ),
                        thread_id=thread_id,
                        thread_type=thread_type,
                    )
                elif is_lang(message_object.text, 'fr'):
                    # If some French is written
                    self.sleep()
                    self.reactToMessage(
                        message_id=message_object.uid,
                        reaction=models.MessageReaction.HEART
                    )
                if 'usually' in message_object.text:
                    self.sleep()
                    self.send(
                        message=models.Message(
                            text='It depends',
                            reply_to_id=message_object.uid
                        ),
                        thread_id=thread_id,
                        thread_type=thread_type,
                    )


if __name__ == '__main__':
    email = input('Email: ')
    password = getpass.getpass()
    bot = YunAnnBot(email=email, password=password)
    bot.listen()
