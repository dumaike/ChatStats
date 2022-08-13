def process_stats(stat_block):

    for user_stats in stat_block.user_stats.values():
        print ("User: " + user_stats.user_id + " - Message Count: " +
         pretty_string(user_stats.message_count))

    print ('Total Messages: ' + pretty_string(
        stat_block.global_stats.message_count))

def pretty_string(input):
    return '{:,}'.format(input)