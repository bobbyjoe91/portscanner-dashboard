'''
    This file contains miscellanous functions
    used for converting and transforming data
    which will be returned by views.py to the
    HTML page.
'''

from .models import Status
import datetime as dt
import pytz
import re



'''
    string_to_time converts time parameter, which is in string,
    to Python 3 datetime object. Bound parameter could be set to
    "stop", which means the time inputted in the function is the upper
    bound of a particular date range
'''
def string_to_time(time, bound=None):
    split_time = re.findall(r"[0-9]{2,4}", time)
    time_list =  list(map(int, split_time))

    time = dt.datetime(
        year=time_list[2], month=time_list[1], day=time_list[0],
        hour=time_list[3], minute=time_list[4], second=time_list[5],
        microsecond=0, tzinfo=pytz.UTC
    )

    '''
        if bound is set to "stop", the time parameter will recognize the input
        as the upper bound of a time range. To compensate the accuracy of Mongodb
        ISODate, the stop time is added 1 second.
    '''
    if bound == "stop":
         time = time + dt.timedelta(seconds=1)

    return time


'''
    remove_page deletes "page" parameter form a url
    this will prevent the current path to be appended
    by another "page" parameter. The function receives
    path in string as the parameter
'''
def remove_page(path):
    if 'page' in path:
        new_path = re.sub('&page=[0-9]*', '', path)
        return new_path

    return path

'''
    get_hosts_and_ports return unique host, its ports, and every status
    of each port.

    Each host has one or more ports. Each port has status, whether 1 or 0.
    Get_hosts_and_ports provide the latest status information for each hosts
    and ports.
'''
def get_hosts_and_ports():
    query_sets = list(Status.objects.values('host','port').distinct())
    hosts_and_ports = dict()

    for query in query_sets:
        if query['host'] not in hosts_and_ports:
            hosts_and_ports[query['host']] = list()

    for query in query_sets:
        if query['port'] not in hosts_and_ports[query['host']]:
            hosts_and_ports[query['host']].append(
                {'port': query['port'],
                 'status': Status.objects.order_by("-timestamp").filter(host=query['host'],
                        port=query['port']).values('status')[0]['status']
                }
            )

    return hosts_and_ports


'''
    pageinate receives n_page as current page position,
    page_range as python 3 range from 1 to last pagination,
    and n as number of page generated.

    paginate returns list of number that will be
    rendered in the pagination around the current page.
'''
def paginate(n_page, page_range, n=4):
    p_range = list()

    count = 0
    while count < n:
        if n_page+count in page_range:
            p_range.append(n_page+count)
        count += 1

    return p_range
