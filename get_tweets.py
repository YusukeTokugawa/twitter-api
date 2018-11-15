# coding: UTF-8
'''
Created on Nov 13, 2018

@author: Yusuke_Tokugawa
'''
from tweet_fields import TweetFields
from data_formatter import DataFormatter
from bs4 import BeautifulSoup
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

    def get_dict_tweets_list(self, limit,query, url):
        data_formatter = DataFormatter()
        dict_tweets_list=[]
        i = 0
        while i < limit:
            if(i == 0):
                base_url = url.format(q=query,pos="")
            else:
                base_url = url.format(q=query,pos=next_position)
            url_data = urllib.request.urlopen(base_url)
            content = json.loads(url_data.read().decode('utf8'))
            next_position = content['min_position']
            html_data = content['items_html']
            soup = BeautifulSoup(html_data)
            tweet_blocks = soup.select('.tweet')
            for tweet_block in tweet_blocks:
                if(i < limit):
                    fullname = tweet_block.select('.fullname')[0].text
                    href = tweet_block.find('a', 'account-group js-account-group js-action-profile js-user-profile-link js-nav')['href']
                    id = int(tweet_block.find('a', 'account-group js-account-group js-action-profile js-user-profile-link js-nav')['data-user-id'])
                    date = tweet_block.find('a', 'tweet-timestamp js-permalink js-nav js-tooltip')['title']
                    body_hashtags = tweet_block.find_all('a', 'twitter-hashtag pretty-link js-nav')
                    hashtags = []
                    for body_hashtag in body_hashtags:
                        hashtags.append('#'+body_hashtag.find('b').text)
                    likes = int(tweet_block.find('span', 'ProfileTweet-action--favorite u-hiddenVisually').find('span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0')
                    replies = int(tweet_block.find('span', 'ProfileTweet-action--reply u-hiddenVisually').find('span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0')
                    retweets = int(tweet_block.find('span', 'ProfileTweet-action--retweet u-hiddenVisually').find('span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0')
                    text = tweet_block.select('.tweet-text')[0].text
                    one_tweet_data = TweetFields(fullname, href, id, date, hashtags, likes, replies, retweets, text)
                    dict_one_tweet_data= data_formatter.convert_to_dict(one_tweet_data)
                    dict_tweets_list.append(dict_one_tweet_data)
                    i+=1
                else:
                    break
        return dict_tweets_list

    def get_tweets_by_hashtags(self, hashtag, limit):
         dict_tweets_list = self.get_dict_tweets_list(limit, hashtag, self.URL_FOR_HASHTAG)
         return dict_tweets_list

    def get_user_tweets(self, user_name, limit):
         dict_tweets_list = self.get_dict_tweets_list(limit, user_name, self.URL_FOR_USER_NAME)
         return dict_tweets_list