from GenericChatClasses import GenericConversation, GenericMessage, GenericStatBlock
from GenericChatClasses import GenericUserStats

import Config
import emoji

def conversation_to_stat_blocks(conversation: GenericConversation):
    stat_block = GenericStatBlock()

    # Process the entire conversation.
    for message in conversation.message_list:
        user_id = message.user_id
        if (user_id not in stat_block.user_stats):
            new_user_stats = GenericUserStats()
            new_user_stats.user_id = user_id
            new_user_stats.message_count = 0
            stat_block.user_stats[user_id] = new_user_stats

        user_stats = stat_block.user_stats[user_id]
        track_message_count_stats(user_stats)
        track_emoji_stats(message, user_stats)

        # Update global stats.
        stat_block.conversation_stats.message_count += 1
        if stat_block.conversation_stats.start_timestamp > message.timestamp:
            stat_block.conversation_stats.start_timestamp = message.timestamp
        if stat_block.conversation_stats.end_timestamp < message.timestamp:
            stat_block.conversation_stats.end_timestamp = message.timestamp

    return stat_block

def track_message_count_stats(user_stats : GenericUserStats):
    user_stats.message_count += 1

def track_emoji_stats(message : GenericMessage, user_stats : GenericUserStats):
    for character in message.message_text:
        if emoji.is_emoji(character) \
            and character not in Config.ignored_emoji_list:
            emoji_string = str(character)
            if emoji_string not in user_stats.emoji_count_map:
                user_stats.emoji_count_map[emoji_string] = 0
            user_stats.emoji_count_map[emoji_string] += 1