from GenericChatClasses import GenericConversation
from GenericChatClasses import GenericMessage
import GenericChatUtils
import Config
import json

def google_messages_to_generic(file_path):
    with open(file_path, mode='r', encoding=Config.google_messages_encoding) \
        as messages_file:
        data = json.load(messages_file)

    chat_record = GenericConversation()

    for message_key in data:
        if 'Message' in data[message_key] \
            and 'SenderId' in data[message_key] \
                and 'Timestamp' in data[message_key]:

            new_chat_message = GenericMessage()            
            new_chat_message.user_id = data[message_key]['SenderId']
            new_chat_message.timestamp = GenericChatUtils.string_to_datetime(
                data[message_key]['Timestamp'], "%Y-%m-%d %H:%M:%S")
            new_chat_message.message_text = data[message_key]['Message']      \
            # Google Messages lists in reverse order, so we insert new 
            # messages at the front, not the back.
            chat_record.message_list.insert(0, new_chat_message)

    return chat_record
            