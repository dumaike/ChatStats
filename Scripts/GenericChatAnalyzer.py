from GenericChatClasses import GenericConversation, GenericMessage, GenericStatBlock
from GenericChatClasses import GenericUserStats

import GenericChatUtils
import Config
import emoji


def conversation_to_stat_blocks(conversation: GenericConversation):
    # Some chat services don't sort their messages by time, so sort them
    # now.
    conversation.message_list = sorted(
        conversation.message_list, key=lambda x: x.timestamp)

    stat_block = GenericStatBlock()

    # Process the entire conversation.
    for idx, message in enumerate(conversation.message_list):
        user_id = message.user_id
        if (user_id not in stat_block.user_stats):
            new_user_stats = GenericUserStats()
            new_user_stats.user_id = user_id
            new_user_stats.message_count = 0
            stat_block.user_stats[user_id] = new_user_stats

        user_stats = stat_block.user_stats[user_id]
        track_message_count_stats(user_stats)
        track_emoji_stats(conversation, idx, user_stats)
        track_first_message_count(conversation, idx, user_stats)

        # Update global stats.
        stat_block.conversation_stats.message_count += 1
        if stat_block.conversation_stats.start_timestamp > message.timestamp:
            stat_block.conversation_stats.start_timestamp = message.timestamp
        if stat_block.conversation_stats.end_timestamp < message.timestamp:
            stat_block.conversation_stats.end_timestamp = message.timestamp

    return stat_block


def track_message_count_stats(user_stats: GenericUserStats):
    user_stats.message_count += 1


def track_emoji_stats(conversation: GenericConversation, idx, user_stats: GenericUserStats):
    message = conversation.message_list[idx]
    for character in message.message_text:
        if emoji.is_emoji(character) \
                and character not in Config.ignored_emoji_list:
            emoji_string = str(character)
            if emoji_string not in user_stats.emoji_count_map:
                user_stats.emoji_count_map[emoji_string] = 0
            user_stats.emoji_count_map[emoji_string] += 1


def track_first_message_count(conversation: GenericConversation, idx, user_stats: GenericUserStats):
    # If this is the first message of the conversation, it's the first of the day.
    if idx == 0:
        user_stats.first_message_of_day_count += 1
        return

    prev_message = conversation.message_list[idx - 1]
    prev_timestamp = GenericChatUtils.timestamp_to_datetime(
        prev_message.timestamp)
    cur_message = conversation.message_list[idx]
    cur_timestamp = GenericChatUtils.timestamp_to_datetime(
        cur_message.timestamp)

    if (prev_timestamp > cur_timestamp):
        print("ERROR: Unsorted Messages")

    if prev_timestamp.day != cur_timestamp.day:
        user_stats.first_message_of_day_count += 1

def debug_write_conversation(conversation: GenericConversation):
    out_file_text = ''
    for message in conversation.message_list:
        out_file_text += str(GenericChatUtils.timestamp_to_datetime(
            message.timestamp)) + ': ' + message.message_text + "\n"
    with open('conversation.json', 'w', encoding='utf-8') as out_file:
        out_file.write(out_file_text)