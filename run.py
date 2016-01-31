if __name__ == '__main__':

    c = 0

    def print_tweet(tweet):
        print(tweet.text)

    def count_tweets(tweet):
        global c
        c += 1
        print(c)

    def print_friend(friend):
        print(friend.name)

    neo.init_friends_list(api.get_user('eLVasiunyk'))
    get_all_friends('eLVasiunyk', neo.add_friend)