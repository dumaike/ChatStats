import datetime

class GenericMessage:
    user_id = ""
    message_text = ""
    timestamp = 0    

class GenericConversation:
    message_list = [] # An array of GenericMessages

class GenericUserStats:
    def __init__(self):
        self.user_id = ""
        self.message_count = 0
        self.question_count = 0    
        self.response_count = 0
        self.total_char_count = 0
        self.longest_message = 0
        self.first_message_of_day_count = 0
        self.image_count = 0
        self.longest_chain = 0
        self.longest_delay_caused = 0
        self.am_pm_ratio = 0
        self.emoji_count_map = {} # A map of emoji to their count.
        self.url_count = 0
        self.exclamation_mark_count = 0
        self.reaction_count = 0
        self.most_obscure_word_used = ""
        self.longest_sentence = 0
        self.first_message_timestamp = datetime.timedelta.max.total_seconds()
        self.last_message_timestamp = datetime.timedelta.min.total_seconds()
    
class GenericConversationStats:
    start_timestamp = datetime.timedelta.max.total_seconds()
    end_timestamp = datetime.timedelta.min.total_seconds()
    longest_lull = 0
    message_count = 0

class GenericStatBlock:
    user_stats = {} # A map of user_ids to GenericUserStats
    conversation_stats = GenericConversationStats()