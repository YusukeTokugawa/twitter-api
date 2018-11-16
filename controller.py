# coding: UTF-8
'''
Created on Nov 13, 2018

@author: Yusuke_Tokugawa
'''
from get_tweets import GetTweets
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/hashtags/<hashtag>', methods=['GET'])
def get_tweets_by_hashtags(hashtag):
    limit = request.args.get('limit', default = 30, type = int)
    tweets_by_hashtags = get_tweets.get_tweets_by_hashtags(hashtag, limit)
    return jsonify(tweets_by_hashtags)

@app.route('/users/<user_name>', methods=['GET'])
def get_user_tweets(user_name):
    limit = request.args.get('limit', default = 30, type = int)
    user_tweets = get_tweets.get_user_tweets(user_name, limit)
    return jsonify(user_tweets)

if __name__ == '__main__':
    get_tweets = GetTweets()
    app.run("localhost", debug=True)

#for test script
if __name__== 'controller':
    get_tweets = GetTweets()