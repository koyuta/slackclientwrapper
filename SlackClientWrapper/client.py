# -*- coding: utf-8 -*-
import time, re, os
from slackclient import SlackClient
import SlackClientWrapper


class Client(object):
    def __init__(self, bot_name, icon_url):
        self.token = os.environ["SLACK_API_TOKEN"]
        self.sc = SlackClient(self.token)
        self.bot_name = bot_name
        self.icon_url = icon_url

    def connect(self):
        if self.sc.rtm_connect():
            while True:
                post = self.sc.rtm_read()
                if not post or 'text' not in post[0]:
                    time.sleep(1)
                    continue
                else:
                    self.full_reciever(post[0])
                    self.command_reciever(post[0])
        else:
            print("Connection Failed, invalid token?")

    def full_reciever(self, post):
        for full_recieve in SlackClientWrapper.Reciever.full_recieves:
            channel, text = full_recieve(post)
            if channel is None:
                channel = post['channel']
            if text is None:
                continue
            self.sc.api_call('chat.postMessage', channel=channel, text=text,
                             username=self.bot_name, icon_url=self.icon_url)

    def command_reciever(self, post):
        for pattern, command in SlackClientWrapper.Reciever.commands.items():
            if not re.match(re.compile(pattern), post['text']):
                continue
            channel, text = command(post)
            if channel is None:
                channel = post['channel']
            if text is None:
                continue
            self.sc.api_call('chat.postMessage', channel=channel, text=text,
                             username=self.bot_name, icon_url=self.icon_url)

if __name__ == '__main__':
    m = Client()
    m.connect()
