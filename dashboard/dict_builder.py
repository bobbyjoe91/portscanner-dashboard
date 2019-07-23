from pymongo import MongoClient

# HOST = "10.8.30.69"
HOST = 'mongodb+srv://bobby:irebelthereforeiexist@asli-ri-monitoring-wtiiq.gcp.mongodb.net/test?retryWrites=true&w=majority'
DB_NAME = 'asli_ri_services'

CLIENT = MongoClient(HOST)
DB = CLIENT[DB_NAME]

def is_ip_address(collection_name):
    import re
    if re.match(r'\b[0-9]*.[0-9]*.[0-9]*.[0-9]\b', collection_name) != None:
        return True
    else:
        return False

IP = [ip for ip in DB.list_collection_names() if is_ip_address(ip)]
PORT = dict()
for ip in IP:
    PORT[ip] = DB[ip].distinct('port')

def retrieve(nrow='All'):
    data = dict()
    for collection in IP:
        data[collection] = dict()
        for port in PORT[collection]:
            # status data will start from the latest
            data[collection][port] = list(DB[collection].find({'port':port}).sort('timestamp', -1))

    return data

ALL_RECORD = retrieve()

def retrieve_by_ip_and_port(ip, port):
    result = list()

    data = ALL_RECORD[ip][port]
    for datum in data:
        result.append(datum)

    return data

def retrieve_latest_ip_and_port():
    data = dict()

    for ip in IP:
        status = list()
        for port in PORT[ip]:
            # get the latest record based on ip and port
            status.append(ALL_RECORD[ip][port][0])
        data[ip] = status

    return data

def retrieve_by_ip_port_and_daterange(ip, port, daterange):
    try:
        startDate, stopDate = daterange.split(" - ")
    except ValueError:
        return []

    data = list(DB[ip].find({
        "port": port,
        "timestamp": {
            "$gte": startDate,
            "$lte": stopDate
        }
    }))

    return data
