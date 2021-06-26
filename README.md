# Retweets covid resources when mentioned in the reply!

## How to setup for your State

Just fill in your API keys which you'll need to apply for a [Twitter developer account](https://developer.twitter.com/en/apply-for-access). It usually get's approved within 5 minutes.

```
CONSUMER_KEY = environ['YOUR CONSUMER_KEY']
CONSUMER_SECRET = environ['YOUR CONSUMER_SECRET']
ACCESS_KEY = environ['YOUR ACCESS_KEY']
ACCESS_SECRET = environ['YOUR ACCESS_SECRET']

```

## Run the script

Install dependencies:
```
npm install
```

Start the app:

```
node index.js
```
or
```
npm start
```

Keep it running or deploy it on heroku for free and have fun!
P.S. If you need any help to deploy it on heroku DM me on Twitter [@Deveshb15](https://twitter.com/Deveshb15).


## How the script works

Summary:

1. Fetchs your all the tweets that you've been tagged in you Twitter timeline.
2. Get's the original tweet that you were tagged.
3. Check's if the tweet is already retweeted.
4. If not retweeted it will retweet again or else continue.

P.S. Don't forget to give me credits:D

