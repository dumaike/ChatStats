import json

from GenericChatClasses import GenericStatBlock
import GenericChatUtils
import Config


def process_stats(stat_block: GenericStatBlock):
    for user_stats in stat_block.user_stats.values():
        # If the user has a config alias, set it now.
        if user_stats.user_id in Config.username_aliases:
            user_stats.user_id = Config.username_aliases[user_stats.user_id]

        print("User: " + user_stats.user_id + " - Message Count: " +
              GenericChatUtils.pretty_string(user_stats.message_count))

        sorted_emoji = []
        total_emoji_count = 0
        for emoji_char in user_stats.emoji_count_map:
            total_emoji_count += user_stats.emoji_count_map[emoji_char]
            sorted_emoji.append(
                {'emoji': emoji_char, 'count': user_stats.emoji_count_map[emoji_char]})

        sorted_emoji = sorted(
            sorted_emoji, key=lambda x: x['count'], reverse=True)

        output_results = "Top 10 Emoji: "
        for emoji_char in sorted_emoji[0:10]:
            output_results += emoji_char['emoji'] + \
                ": " + str(emoji_char['count']) + ", "
        print(output_results)
        print('Emoji Count: ' \
            + GenericChatUtils.pretty_string(total_emoji_count))
        print('Unique Emoji Used: ' \
            + GenericChatUtils.pretty_string(len(sorted_emoji)))
        user_stats.emoji_count_map = sorted_emoji

        # To indicate the end of stats for one user.
        print('***********************************************************')

    print('Total Messages: ' + GenericChatUtils.pretty_string(
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
    print('Messages Per Day: ' + str(msgs_per_second*60*60*24))

    json_stats_str = json.dumps(stats_to_json(stat_block),
                                indent=4, sort_keys=True,  ensure_ascii=False)

    with open('text_stats.json', 'w', encoding='utf-8') as out_file:
        out_file.write(str(json_stats_str))


def stats_to_json(stat_block: GenericStatBlock):

    user_stats_array = {}
    for single_user_stat in stat_block.user_stats.values():
        single_user_stat_dict = single_user_stat.__dict__
        # Add nested dictionaries.
        single_user_stat_dict['emoji_count_map'] = \
            single_user_stat.emoji_count_map

        user_stats_array[single_user_stat.user_id] = single_user_stat_dict

    stats_dict = {'generic_stat_block': {
        'user_stats': user_stats_array, 'conversation_stats': stat_block.conversation_stats.__dict__}}

    return stats_dict
