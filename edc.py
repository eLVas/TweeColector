import tweepy
import time

auth = tweepy.OAuthHandler('iuDTSs5njyqtN0PnL302nX6A9', 'qRg1GNjobvJMUKK54r9OFPNBZmSkm7TC1bM4wTB2EIrf6D5hns')
auth.set_access_token('1169383382-x8LJxJ6NhniQ8uN4LbRCNLT1Iw76F5HY8Rkxa1j', 'PYv3dxOj45zdJ5Qwaon0kUDo8aSAgWaTfTiafgX3t9NDR')

"""try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token')

print('request url:')
print(redirect_url, end='\n\n')

verifier = input('Verifier:')

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print('Error! Failed to get access token')"""

api = tweepy.API(auth)


"""def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15*60)

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.friends_count < 300:
        print(follower.screen_name)"""

public_tweets = api.home_timeline()
print(dir(public_tweets[0].user))
#for key in public_tweets[0].user.keys():
#    print(key)

"""for tweet in public_tweets:
    print(tweet.user.screen_name)"""