import datetime
import time

# TODO: Make this take a config for message type.
def string_to_datetime(date):
    #format_string_old = '%A, %B %d, %Y at %I:%M:%S %p UTC' 
    format_string = "%Y-%m-%d %H:%M:%S"
    raw_datetime = datetime.datetime.strptime(date, format_string)    
    # TODO: Make this part of a config somehow
    # For Google Messages, subtract two hours to get local time.
    time_zone_adjusted_datetime = raw_datetime - datetime.timedelta(hours=2)

    return time_zone_adjusted_datetime

def datetime_to_string(date):
    return date
