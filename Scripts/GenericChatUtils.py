import datetime

# TODO: Make this take a config for message type.
def string_to_datetime(date, format):    
    raw_datetime = datetime.datetime.strptime(date, format)    
    # TODO: Make this part of a config somehow
    # For Google Messages, subtract two hours to get local time.
    time_zone_adjusted_datetime = raw_datetime - datetime.timedelta(hours=2)

    return time_zone_adjusted_datetime

def datetime_to_string(date):
    return date
