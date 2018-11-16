'''
Created on Nov 16, 2018

@author: Yusuke Tokugawa
'''
from setuptools import setup

setup(
    name='twitter-api',
    version='1.0.0',
    description='API to get tweets from Twitter in real-time',
    author='Yusuke Tokugawa',
    author_email='goodfairy2012@gmail.com',
    license='MIT',
    install_requires=['Flask', 'requests', 'bs4'],
    packages=['twitter-api']
)