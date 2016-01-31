import tweepy

_CONSUMER_KEY = 'iuDTSs5njyqtN0PnL302nX6A9'
_CONSUMER_SECRET = 'qRg1GNjobvJMUKK54r9OFPNBZmSkm7TC1bM4wTB2EIrf6D5hns'

_ACCESS_TOKEN = '1169383382-x8LJxJ6NhniQ8uN4LbRCNLT1Iw76F5HY8Rkxa1j'
_ACCESS_TOKEN_SECRET = 'PYv3dxOj45zdJ5Qwaon0kUDo8aSAgWaTfTiafgX3t9NDR'


def get_api():
    auth = tweepy.OAuthHandler(_CONSUMER_KEY, _CONSUMER_SECRET)
    auth.set_access_token(_ACCESS_TOKEN, _ACCESS_TOKEN_SECRET)
    return tweepy.API(auth, retry_count=10, retry_delay=60, retry_errors=['104'], wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
