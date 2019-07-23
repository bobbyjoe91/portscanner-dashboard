from pymongo import MongoClient

# HOST = "10.8.30.69"
HOST = 'mongodb+srv://bobby:irebelthereforeiexist@asli-ri-monitoring-wtiiq.gcp.mongodb.net/test?retryWrites=true&w=majority'
db_name = 'asli_ri_services'

client = MongoClient(HOST)
db = client[db_name]

ips = db.list_collection_names()
ports = dict()
for ip in ips:
    ports[ip] = db[ip].distinct('port')

def is_ip_address(collection_name):
    import re
    if re.match(r'\b[0-9]*.[0-9]*.[0-9]*.[0-9]\b', collection_name) != None:
        return True
    else:
        return False

def retrieve(nrow='All'):
    data = dict()
    for collection in db.list_collection_names():
        # status data will start from the latest
        if is_ip_address(collection):
            if nrow != 'All':
                data[collection] = list(db[collection].find().sort('timestamp', -1).limit(nrow))
            else:
                data[collection] = list(db[collection].find().sort('timestamp', -1))

    return data

def retrieve_by_ip_and_port(ip, port):
    data = list(db[ip].find({"port":port}).sort('timestamp', -1))
    return data

def retrieve_latest_ip_and_port():
    data = dict()

    for ip in ips:
        status = list()
        for port in ports[ip]:
            status.append(retrieve_by_ip_and_port(ip, port)[0])
        data[ip] = status

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
