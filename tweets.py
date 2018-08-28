import tweepy
from textblob import TextBlob
Consumer_Key= "your consumer key"
Consumer_Secret="your consumer secret"
Access_Token	="your access token"
AccessToken_Secret=	"your access token secret"
authen=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
authen.set_access_token(Access_Token,AccessToken_Secret)



api=tweepy.API(authen);
tweets=api.search("trump")
for tweet in tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)
