# coding: UTF-8
'''
Created on Nov 13, 2018

@author: Yusuke_Tokugawa
'''
from data_formatter import DataFormatter
from bs4 import BeautifulSoup
import random
import sys
import os
import json
import urllib
import requests

class GetTweets:
    URL_FOR_HASHTAG = 'https://twitter.com/i/search/timeline?f=tweets&vertical='\
                      'default&include_available_features=1&include_entities=1&'\
                      'reset_error_state=false&src=typd&max_position={pos}&q={q}'
    URL_FOR_USER_NAME = 'https://twitter.com/i/profiles/show/{q}'\
                        '/timeline/tweets?include_available_features=1&include_entities=1'\
                        '&max_position={pos}&reset_error_state=false'

    def __init__(self):
        pass

    # Without the header, can not get tweet data with 'URL_FOR_USER_NAME' URL
    HEADERS_LIST = [
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
    ]
    HEADER = {'User-Agent': random.choice(HEADERS_LIST)}

    def get_dict_tweets_list(self, limit,query, url):
        data_formatter = DataFormatter()
        dict_tweets_list=[]
        i = 0
        while i < limit:
            if(i == 0):
                base_url = url.format(q=query,pos="")
            else:
                base_url = url.format(q=query,pos=next_position)
            url_data = requests.get(base_url, headers=self.HEADER)
            content = json.loads(url_data.text)
            next_position = content['min_position']
            html_data = content['items_html']
            soup = BeautifulSoup(html_data)
            tweet_blocks = soup.select('.tweet')
            for tweet_block in tweet_blocks:
                if(i < limit):
                    dict_tweets_list.append(data_formatter.get_dict_one_tweet_data(tweet_block))
                    i+=1
                else:
                    break
        return dict_tweets_list

    def get_tweets_by_hashtags(self, hashtag, limit):
         hashtag = '%23'+hashtag #Add hash mark
         dict_tweets_list = self.get_dict_tweets_list(limit, hashtag, self.URL_FOR_HASHTAG)
         return dict_tweets_list

    def get_user_tweets(self, user_name, limit):
         dict_tweets_list = self.get_dict_tweets_list(limit, user_name, self.URL_FOR_USER_NAME)
         return dict_tweets_list