# Introduction #
`twitter-api` is API to get following tweets data as json file from Twitter in real-time.
1. Tweets with a particular hashtag
2. Particular user tweets (includes re-tweets)

# Installation #
1. Install latest Python 3.7 and pip
2. Run command as administrator:
 * `git clone https://github.com/YusukeTokugawa/twitter-api.git`
 * `cd twitter-api`
 * `python setup.py install`
 
 When running setup.py, if there is certificate error like `unable to get local issuer certificate`,
 upgrade `certifi` by this command `pip install --upgrade certifi` 

# Usage #
1. Run `python controller.py` as administrator
2. In a new terminal, send following sample request:
 * `curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:5000/hashtags/Python?limit=40`
 * `curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:5000/users/twitter?limit=20`
 
 You can decide search condition by changing `Python`, `twitter` and `limit number` in URL
