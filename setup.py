# -*- coding:utf-8 -*-
from setuptools import setup

setup(name='slackclientwrapper',
      version="1.0.0",
      author="koyuta",
      packages=['SlackClientWrapper'],
      install_requires=[
          'slackclient',
      ],
      zip_safe=False)
