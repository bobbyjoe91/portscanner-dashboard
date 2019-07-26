import datetime as dt
import pytz
import re

def string_to_time(time, bound=None):
    split_time = re.findall(r"[0-9]{2,4}", time)
    time_list =  list(map(int, split_time))

    '''
        if bound is set to "stop", the time input is the upper bound
        of a time range. To compensate the accuracy of mongodb ISODate,
        the stop time is added 1 second.
    '''
    time = dt.datetime(
        year=time_list[2], month=time_list[1], day=time_list[0],
        hour=time_list[3], minute=time_list[4], second=time_list[5],
        microsecond=0, tzinfo=pytz.UTC
    )
    
    if bound == "stop":
         time = time + dt.timedelta(seconds=1)

    return time

def remove_page(path):
    if 'page' in path:
        new_path = re.sub('&page=[0-9]*', '', path)
        return new_path

    return path
