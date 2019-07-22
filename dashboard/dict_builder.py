from pymongo import MongoClient

def retrieve():
    username = "bobby"
    password = "indonesia!"
    HOST = "mongodb+srv://" + username + ":" + password + "@asli-ri-monitoring-wtiiq.gcp.mongodb.net/test?retryWrites=true&w=majority"

    db_name = 'asli_ri_services'
    client = MongoClient(HOST)
    db = client[db_name]

    data = dict()
    for collection in db.list_collection_names():
        data[collection] = list(db[collection].find())

    return data
