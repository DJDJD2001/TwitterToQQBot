# Define functions for twitter related

import tweepy

from shokobot.plugins.settings import twitter_consumer_key as consumer_key
from shokobot.plugins.settings import twitter_consumer_secret as consumer_secret
from shokobot.plugins.settings import twitter_access_token as access_token
from shokobot.plugins.settings import twitter_access_token_secret as access_token_secret
from shokobot.plugins.settings import ssr_proxy_http as proxy
from shokobot.plugins.settings import twitter_id as ID

def twitter_get_api():
    # Parameter:
    #   None
    # Return:
    #   API object

    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        twitter_api = tweepy.API(auth, proxy=proxy, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    except Exception as e:
        print('Some errors occured when logging in twitter: ', e)
    return twitter_api
