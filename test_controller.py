# coding: UTF-8
'''
Created on Nov 14, 2018

@author: Yusuke_Tokugawa
'''
import unittest
import json
import controller
import re

class TestController(unittest.TestCase):


    def setUp(self):
        self.app = controller.app.test_client()


    def test_get_tweets_by_hashtags(self):
        response = self.app.get('/hashtags/test?limit=2')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        content_body_dict = json.loads(response.data)
        match_hashtag = False
        p = re.compile("#test", re.IGNORECASE)
        for hashtag in content_body_dict[0]['hashtags']:
            if p.match(hashtag) != None:
                match_hashtag = True
        assert match_hashtag
        assert len(content_body_dict) == 2



    def test_get_user_tweets(self):
        response = self.app.get('/users/YusukeT98804728?limit=2')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        content_body_dict = json.loads(response.data)
        assert content_body_dict[0]['account']['fullname']=="YusukeT"
        assert len(content_body_dict) == 2

if __name__ == "__main__":
    unittest.main()