import tweepy
import time
import os
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


api = tweepy.API(auth, wait_on_rate_limit=True)

def check_mentions(api):
  for tweet in tweepy.Cursor(api.mentions_timeline).items():
    tweetID = tweet.in_reply_to_status_id
    print(tweet.text)
    if not tweet.retweeted:
      try:
        api.retweet(tweetID)
        print('retweeted')
        time.sleep(10)
      except tweepy.TweepError as e:
        print(e.reason)
        continue
      
  return "Done!" 

def main():
  print("Now working")
  while True:
    try: 
      check_mentions(api)
      print("retweet")
      time.sleep(60)
    except tweepy.TweepError as e:
      print(e.reason)
    except StopIteration:
      break

if __name__ == "__main__":
  main()


