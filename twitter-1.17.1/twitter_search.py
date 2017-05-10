try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '858382724670791680-TfD9BR4nAJx3axZAhHrBCAiIrc4kt3M'
ACCESS_SECRET = 'K4rlf15YJqt74HfUYPSM3O0dfY41Sb8DTVrJI7UK4zBtx'
CONSUMER_KEY = 'MS1k7HZMExVrBhzcVinNGRmKg'
CONSUMER_SECRET = 'IdtNtF1EvlC1YaNic3urRoniretU1xVl5XGOjAOVTGMcz8GRrj'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

# Search for latest tweets about "#nlproc"
#twitter.search.tweets(q='girl')
output  = twitter.search.tweets(q='#nlproc', result_type='recent', lang='en', count=10)
for tweet in output:
    # Twitter Pyth on Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
