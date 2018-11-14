# coding: UTF-8
'''
Created on Nov 13, 2018

@author: Yusuke_Tokugawa
'''
from tweet_fields import TweetFields
from data_formatter import DataFormatter

class GetTweets:
    def __init__(self):
        pass

    def make_url_with_hashtags(self, hashtag):
        return 'https://twitter.com/hashtag/' + hashtag

    def make_url_with_user_name(self, user_name):
        return 'https://twitter.com/' + user_name

    def get_one_tweet_data(self, url_data):
        #write the logic to get data from twitter
        one_tweet_data = TweetFields("DummyName","href",10,"2018/08",["aa","bb"],15,10,15,"dummy")
        return one_tweet_data

    def get_dict_tweets_list(self, url_data, limit):
        data_formatter = DataFormatter()
        dict_tweets_list=[]
        for i in range(limit):
            one_tweet_data = self.get_one_tweet_data(url_data)
            dict_one_tweet_data= data_formatter.convert_to_dict(one_tweet_data)
            dict_tweets_list.append(dict_one_tweet_data)
        return dict_tweets_list

    def get_tweets_by_hashtags(self, hashtag, limit):
         url = self.make_url_with_hashtags(hashtag)
         dict_tweets_list = self.get_dict_tweets_list(url, limit)
         return dict_tweets_list

    def get_user_tweets(self, user_name, limit):
         url = self.make_url_with_user_name(user_name)
         dict_tweets_list = self.get_dict_tweets_list(url, limit)
         return dict_tweets_list