import tweepy
import utils
import neo

api = utils.auth.get_api()


def get_user_timeline_cursor(api_method, user, count):
    return


def get_all_tweets(screen_name, save_func):
    usr_id = screen_name
    cursor = tweepy.Cursor(api.user_timeline, id=usr_id, count=200).items()
    user_tweets_iterator = utils.limit_handler(cursor)

    for tweet in user_tweets_iterator:
        save_func(tweet)


def get_all_friends(screen_name, save_func):
    usr_id = screen_name
    cursor = tweepy.Cursor(api.friends, id=usr_id, count=200).items()
    user_tweets_iterator = utils.limit_handler(cursor)

    for tweet in user_tweets_iterator:
        save_func(tweet)


c = 0
total = 0

friends = []

def print_tweet(tweet):
    print(tweet.text)

def count_tweets(tweet):
    global c
    c += 1
    print(c)

def print_friend_and_save_wlist(friend):
    global friends
    neo.add_friend(friend)
    friends.append(friend)
    global total
    global c
    c += 1
    print(c, end='/')
    print(total, end='\t')
    print(friend.name)

def print_friend_and_save(friend):
    neo.add_friend(friend)
    global c
    global total
    c += 1
    print(c, end='/')
    print(total, end='\t')
    print(friend.name)

def process_friends(screen_name, prc_func):
    global c
    c = 0
    user = api.get_user(screen_name)
    global total
    total = user.friends_count
    neo.init_friends_list(user)
    print('Saving friends of user {}, total: {}'.format(user.name, user.friends_count))
    get_all_friends(screen_name, prc_func)


