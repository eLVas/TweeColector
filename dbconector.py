from py2neo import authenticate, Graph, Path

authenticate('localhost:7474', 'neo4j', 'electro')
graph = Graph('http://localhost:7474/db/data/')

tx = graph.cypher.begin()

createUStmt = 'MERGE (k:Person {name:{N}}) RETURN {k}'
createRStmt = 'CREATE (p1)-[:FOLLOW]->(p2)'

s = ''


def add_user(user):
    return graph.cypher.execute('MERGE (n' + user.screen_name + ':User {name:{N}})', {'N': user.name})


def add_connection(user1, user2, rel_type):
    return Path(user1, rel_type, user2)


def init_friends_list(user):
    global me
    me = add_user(user)


def add_friend(user):
    graph.create(add_connection(me, add_user(user), 'FOLLOW'))


def commit_friends_list():
    return ''


