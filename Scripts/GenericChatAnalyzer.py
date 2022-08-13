from GenericChatUtil import GenericStatBlock
from GenericChatUtil import GenericConversationStats
from GenericChatUtil import GenericUserStats

def conversation_to_stat_blocks(conversation):

    stat_block = GenericStatBlock()
    for message in conversation.message_list:
        user_id = message.user_id
        if (user_id not in stat_block.user_stats):
            new_user_stats = GenericUserStats()
            new_user_stats.user_id = user_id
            new_user_stats.message_count = 0
            stat_block.user_stats[user_id] = new_user_stats

        # Update individual user stats.
        user_stats = stat_block.user_stats[user_id]
        user_stats.message_count += 1

        # Update global stats.
        stat_block.global_stats.message_count += 1

    return stat_block


