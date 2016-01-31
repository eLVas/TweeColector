import collect
import time

collect.process_friends('eLVasiunyk', collect.print_friend_and_save_wlist)

for friend in collect.friends:
    while True:
        try:
            collect.process_friends(friend.screen_name, collect.print_friend_and_save)
        except BaseException as e:
            print(e)
            time.sleep(10)
            continue
        break
