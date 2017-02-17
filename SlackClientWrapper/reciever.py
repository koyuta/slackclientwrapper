# -*- coding: utf-8 -*-

class Reciever(object):
    def __init__(self):
        pass

    full_recieves = [];
    commands = {};

    @classmethod
    def match(cls, command, prefix=None):
        if prefix is not None:
            command = '{0} {1}'.format(prefix, command)
        command = '^{0}$'.format(command)
        def wrapper(func):
            Reciever.commands[command] = func
            return func
        return wrapper

    @classmethod
    def full_recieve(cls, func):
        Reciever.full_recieves.append(func)
