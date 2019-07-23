from pymongo import MongoClient

# HOST = "10.8.30.69"
# db_name = 'asli_ri_services'
HOST = 'mongodb+srv://bobby:irebelthereforeiexist@asli-ri-monitoring-wtiiq.gcp.mongodb.net/test?retryWrites=true&w=majority'
db_name = 'asli_ri_services'
client = MongoClient(HOST)
db = client[db_name]

def is_match(collection_name):
    import re
    if re.match(r'\b[0-9]*.[0-9]*.[0-9]*.[0-9]\b', collection_name) != None:
        return True
    else:
        return False

def retrieve(nrow='All'):
    data = dict()
    for collection in db.list_collection_names():
        # status data will start from the latest
        if is_match(collection):
            if nrow != 'All':
                data[collection] = list(db[collection].find().sort('timestamp', -1).limit(nrow))
            else:
                data[collection] = list(db[collection].find().sort('timestamp', -1))

    return data

def retrieve_by_ip_and_port(ip, port):
    data = list(db[ip].find({"port":port}))

    return data

def retrieve_by_ip_port_and_daterange(ip, port, daterange):
    # Dummy date sample, there should be a PARSER and VALIDATOR of daterange input after this
    # startDate = "16-07-2019 15:27:00"
    # stopDate = "16-07-2019 15:30:00"
    startDate, stopDate = daterange.split(" - ")
    
    data = list(db[ip].find({
        "port": port,
        "timestamp": {
            "$gte": startDate,
            "$lte": stopDate
        }
    }))

    return data
