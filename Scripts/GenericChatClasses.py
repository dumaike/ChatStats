import datetime

class GenericMessage:
    user_id = ""
    message_text = ""
    timestamp = 0    

class GenericConversation:
    message_list = [] # An array of GenericMessages

class GenericUserStats:
    user_id = ""
    message_count = 0
    question_count = 0    
    response_count = 0
    total_char_count = 0
    longest_message = 0
    image_count = 0
    longest_chain = 0
    longest_delay_caused = 0
    am_pm_ratio = 0
    emoji_count = 0
    url_count = 0
    exclamation_mark_count = 0
    reaction_count = 0
    most_obscure_word_used = ""
    longest_sentence = 0
    
class GenericConversationStats:
    start_timestamp = datetime.datetime.max
    end_timestamp = datetime.datetime.min
    message_count = 0

class GenericStatBlock:
    user_stats = {} # A map of user_ids to GenericUserStats
    global_stats = GenericConversationStats()