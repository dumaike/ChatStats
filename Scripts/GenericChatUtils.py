import datetime

# TODO: Make this take a config for message type.
def string_to_timestamp(date, format):
    raw_datetime = datetime.datetime.strptime(date, format)
    # TODO: Make this part of a config somehow
    # For Google Messages, subtract two hours to get local time.
    time_zone_adjusted_datetime = raw_datetime - datetime.timedelta(hours=2)

    epoch_date_time = datetime.datetime(1970, 1, 1)
    time_since_epoch_seconds = time_zone_adjusted_datetime - epoch_date_time

    return time_since_epoch_seconds.total_seconds()

def timestamp_to_datetime(timestamp):    
    epoch_date_time = datetime.datetime(1970, 1, 1)    
    return epoch_date_time + datetime.timedelta(seconds=timestamp)
    
def timestamp_to_timedelta(timestamp):    
    return datetime.timedelta(seconds=timestamp)

def pretty_string(input):
    return '{:,}'.format(input)