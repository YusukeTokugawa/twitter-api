# coding: UTF-8
'''
Created on Nov 13, 2018

@author: Yusuke_Tokugawa
'''
from get_tweets import GetTweets
from flask import Flask
app = Flask(__name__)

@app.route('/hashtags', methods=['GET'])
def get_tweets_by_hashtags():
    tweets_by_hashtags = get_tweets.get_tweets_by_hashtags()
    return tweets_by_hashtags

@app.route('/users', methods=['GET'])
def get_user_tweets():
    user_tweets = get_tweets.get_user_tweets()
    return user_tweets

if __name__ == '__main__':
    get_tweets = GetTweets()
    app.run()