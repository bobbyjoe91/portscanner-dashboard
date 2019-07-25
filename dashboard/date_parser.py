import datetime
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
    if bound == "stop":
         if time_list[5] == 59:
             time_list[5] = 00
             time_list[4] += 1
         else:
             time_list[5] += 1

    return datetime.datetime(
        year=time_list[2], month=time_list[1], day=time_list[0],
        hour=time_list[3], minute=time_list[4], second=time_list[5],
        microsecond=0, tzinfo=pytz.UTC
    )
