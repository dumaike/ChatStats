import json
import Config

with open(Config.file_path, mode='r', encoding=Config.google_messages_encoding) as messages_file:
    data = json.load(messages_file)

total_message_count = 0
user_to_count_dict = {}
for message_key in data:
    if 'Message' in data[message_key] and 'SenderId' in data[message_key]:
        sender_id = data[message_key]['SenderId']
        #print (data[message_key]['Message'])
        if (sender_id not in user_to_count_dict):
            user_to_count_dict[sender_id] = 0
        user_to_count_dict[sender_id] += 1
        total_message_count += 1

print('Messages by User: ' + str(user_to_count_dict))
print('Total Messages: ' + str(total_message_count))