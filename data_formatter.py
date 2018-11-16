'''
Created on Nov 14, 2018

@author: Yusuke Tokugawa
'''
from tweet_fields import TweetFields

class DataFormatter:
    def __init__(self):
        pass

    def convert_to_dict(self, one_tweet_data):
        fullname  = one_tweet_data.fullname
        href  = one_tweet_data.href
        id  = one_tweet_data.id
        date  = one_tweet_data.date
        hashtags  = one_tweet_data.hashtags
        likes  = one_tweet_data.likes
        replies  = one_tweet_data.replies
        retweets  = one_tweet_data.retweets
        text  = one_tweet_data.text
        account = {"fullname":fullname, "href":href, "id":id}
        organized_one_tweet_data = {"account":account, "date":date, "hashtags": hashtags, "likes":likes, "replies":replies,
                                    "retweets":retweets, "text":text}
        return organized_one_tweet_data

    def get_dict_one_tweet_data(self, tweet_block):
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
        return self.convert_to_dict(one_tweet_data)