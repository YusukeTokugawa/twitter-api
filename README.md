# Introduction #
`twitter-api` is API to get following tweets from Twitter in real-time.
1. Tweets with a particular hashtag
2. Particular user tweets

# Installation #
1. Install latest Python 3.7
2. Execute command:
 * `git clone https://github.com/YusukeTokugawa/twitter-api.git`
 * `cd twitter-api`
 * `python setup.py install`

# Usage #
1. Run `python controller.py` or double click `controller.py`
2. In a new terminal, send following request:
 * `curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:5000/hashtags/Python?limit=40`
 * `curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:5000/users/twitter?limit=20`