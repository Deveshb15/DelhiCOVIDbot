import tweepy
import time

auth = tweepy.OAuthHandler('onQcdIYs1Rm59GlHJZoPhAj1F', 'p3mX4SuEbzIeQlGaKSxHIJQ7joack9BWS8kewolcAMRJ7zZ3dE')

auth.set_access_token('1385468960473157632-MziDMJYqL9cBNOYpl8OIB0gRuAOQ9B', 'zjyGa8oorQSfXTmkmPW6mPo7OZVf3cufLGpScKBqgeubv')


api = tweepy.API(auth)

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


