import json

from GenericChatClasses import GenericStatBlock
import GenericChatUtils


def process_stats(stat_block: GenericStatBlock):
    for user_stats in stat_block.user_stats.values():
        print("User: " + user_stats.user_id + " - Message Count: " +
              pretty_string(user_stats.message_count))

        top_ten_emoji = []
        for emoji in user_stats.emoji_count_map:
            top_ten_emoji.append(
                {'emoji': emoji, 'count': user_stats.emoji_count_map[emoji]})

        top_ten_emoji = sorted(
            top_ten_emoji, key=lambda x: x['count'], reverse=True)
        top_ten_emoji = top_ten_emoji[0:10]
        print(top_ten_emoji)

    print('Total Messages: ' + pretty_string(
        stat_block.conversation_stats.message_count))
    print('First Messages: ' + str(GenericChatUtils.timestamp_to_datetime(
        stat_block.conversation_stats.start_timestamp)))
    print('Last Message: ' + str(GenericChatUtils.timestamp_to_datetime(
        stat_block.conversation_stats.end_timestamp)))

    elapsed_time = stat_block.conversation_stats.end_timestamp - \
        stat_block.conversation_stats.start_timestamp
    print('Elapsed Time: ' + str(GenericChatUtils.timestamp_to_timedelta(elapsed_time)))
    msgs_per_second = stat_block.conversation_stats.message_count / \
        elapsed_time
    print('Messages Per Hour: ' + str(msgs_per_second*60*60))
    print('Messages Per Waking Hour (16 hours/day): ' + str(
        msgs_per_second*60*60*3/2))

    json_stats_str = json.dumps(stats_to_json(stat_block),
                                indent=4, sort_keys=True,  ensure_ascii=False)

    with open('text_stats.json', 'w', encoding='utf-8') as out_file:
        out_file.write(str(json_stats_str))


def pretty_string(input):
    return '{:,}'.format(input)


def stats_to_json(stat_block: GenericStatBlock):

    user_stats_array = []
    for single_user_stat in stat_block.user_stats.values():
        single_user_stat_dict = single_user_stat.__dict__
        # Add nested dictionaries.
        single_user_stat_dict['emoji_count_map'] = \
            single_user_stat.emoji_count_map

        user_stats_array.append(single_user_stat_dict)

    stats_dict = {'generic_stat_block': {
        'user_stats': user_stats_array, 'conversation_stats': stat_block.conversation_stats.__dict__}}

    return stats_dict
