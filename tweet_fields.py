# coding: UTF-8
'''
Created on Nov 13, 2018

@author: Yusuke_Tokugawa
'''
import dataclasses
from typing import List

@dataclasses.dataclass
class TweetFields:
    fullname: str
    href: str
    id: int
    date: str
    hashtags: List[str]
    likes: int
    replies: int
    retweets: int
    text: str