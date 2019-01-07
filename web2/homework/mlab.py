import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds237669.mlab.com:37669/moviedb

host = "ds145093.mlab.com"
port = 45093
db_name = "accountdb"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())