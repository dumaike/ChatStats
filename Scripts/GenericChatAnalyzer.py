from GenericChatClasses import GenericConversation, GenericStatBlock
from GenericChatClasses import GenericUserStats

import emoji

def conversation_to_stat_blocks(conversation : GenericConversation):
    stat_block = GenericStatBlock()

    # Process the entire conversation.
    for message in conversation.message_list:
        user_id = message.user_id
        if (user_id not in stat_block.user_stats):
            new_user_stats = GenericUserStats()
            new_user_stats.user_id = user_id
            new_user_stats.message_count = 0
            stat_block.user_stats[user_id] = new_user_stats

        # TODO: Break each stat calculation into a function.
        # Update individual user stats.
        user_stats = stat_block.user_stats[user_id]
        user_stats.message_count += 1

        # Count the Emoji!
        for character in message.message_text:            
            # TODO: Filter out modifier emoji like skin tone and gender, as
            # their count isn't reflective of a single emoji instance.
            if emoji.is_emoji(character):
                emoji_string = str(character)
                if emoji_string not in user_stats.emoji_count_map:
                    user_stats.emoji_count_map[emoji_string] = 0
                user_stats.emoji_count_map[emoji_string] += 1

        # Update global stats.
        stat_block.conversation_stats.message_count += 1
        if stat_block.conversation_stats.start_timestamp > message.timestamp:
            stat_block.conversation_stats.start_timestamp = message.timestamp
        if stat_block.conversation_stats.end_timestamp < message.timestamp:
            stat_block.conversation_stats.end_timestamp = message.timestamp

    return stat_block

    