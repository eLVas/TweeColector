from neo4jrestclient.client import GraphDatabase

db = GraphDatabase("http://localhost:7474", username="neo4j", password="electro")

# Create some nodes with labels
label_user = db.labels.create("User")


def add_user(user):
    u = label_user.get(screen_name=user.screen_name)
    print(u)
    if not u:
        u = db.nodes.create(name=user.name, screen_name=user.screen_name)
        label_user.add(u)
    else:
        u = u.next()

    return u


def add_connection(user1, user2, rel_type):
    return user1.relationships.create(rel_type, user2)


def init_friends_list(user):
    global me
    me = add_user(user)


def add_friend(user):
    friend = add_user(user)
    if friend not in [rel.end for rel in me.relationships.outgoing(types=['FOLLOWS'])]:
        add_connection(me, friend, 'FOLLOWS')


