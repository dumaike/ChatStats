class GenericMessage:
    user_id = ""
    message_text = ""
    timestamp = 0    

class GenericConversation:
    message_list = [] # An array of GenericMessages

class GenericUserStats:
    user_id = ""
    message_count = ""
    
class GenericConversationStats:
    start_timestamp = 0
    end_timestamp = 0
    message_count = 0

class GenericStatBlock:
    user_stats = {} # A map of user_ids to GenericUserStats
    global_stats = GenericConversationStats()