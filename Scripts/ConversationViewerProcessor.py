from GenericChatClasses import GenericConversation, GenericConversationStats, GenericMessage, GenericStatBlock
from GenericChatClasses import GenericUserStats

import GenericChatUtils
import Config
import emoji


def conversation_to_viewer(conversation: GenericConversation):
    # Some chat services don't sort their messages by time, so sort them
    # now.
    conversation.message_list = sorted(
        conversation.message_list, key=lambda x: x.timestamp)

    next_idx = 0
    while (next_idx != -1):
        first_message = conversation.message_list[next_idx]
        first_timestamp = GenericChatUtils.timestamp_to_datetime(
            first_message.timestamp)
        
        new_idx = new_conversation_segment(next_idx, str(
            first_timestamp.year) + "-" + str(first_timestamp.month) + "-conversation", conversation)
        next_idx = new_idx


def new_conversation_segment(start_idx, filename, conversation: GenericConversation):

    return_idx = start_idx
    with open(filename + ".html", 'w', encoding='utf-8') as out_file:

        conversation_as_str = ""        
        out_file.write(get_html_header())

        current_month = -1

        # Read each message and append it to the output
        for idx in range(len(conversation.message_list)): 
            adjusted_idx = idx + start_idx

            # If this is the last message, return -1 to terminate the conversation loop
            total_messages = len(conversation.message_list)
            if adjusted_idx == total_messages - 1:
                return_idx = -1
                break
            else:
                return_idx = adjusted_idx

            # Message preprocessing.
            message = conversation.message_list[adjusted_idx]
            if len(message.message_text) == 0:
                message.message_text = "*Image*"
            timestamp = GenericChatUtils.timestamp_to_datetime(
                message.timestamp)

            # Swap User IDs for good ones.
            user_id = "Mike" if message.user_id == "Self" else "Elena"

            # Make sure a month hasn't elapsed.
            if current_month == -1:
                current_month = timestamp.month
            past_segment_limit = timestamp.month != current_month

            if not past_segment_limit:
                # Before formatting for html, save the string for the txt file.
                conversation_as_str += user_id + " " + \
                    str(timestamp) + ":\n" + message.message_text + "\n\n"

                # Reformat emoji for HTML
                emoji_count = emoji.emoji_count(message.message_text)
                if emoji_count > 0:
                    #message.message_text = convert_emoji_to_html(message.message_text)
                    message.message_text = emoji.replace_emoji(message.message_text, replace=xml_escape)

                # CSS Styling
                message_html_block = ""
                if user_id == "Mike":
                    message_html_block = """            
                        <li class="in">
                            <div class="chat-img">
                                <img alt="Avtar" src="https://drive.google.com/uc?id=1lnyZIBUytbzahvRm4R34LUEZzM80Xibg">
                            </div>
                            <div class="chat-body">
                                <div class="chat-message">
                                    <h5>{user_id} - {timestamp}</h5>
                                    <p>{message_text}</p>
                                </div>
                            </div>
                        </li>                
                    """.format(user_id=user_id, message_text=message.message_text, timestamp=timestamp)
                else:
                    message_html_block = """
                        <li class="out">
                            <div class="chat-img">
                                <img alt="Avtar" src="https://drive.google.com/uc?id=1Tb1l7laME_PFm6EQBafm9-1nyJxGX_Li">
                            </div>
                            <div class="chat-body">
                                <div class="chat-message">
                                    <h5>{user_id} - {timestamp}</h5>
                                    <p>{message_text}</p>
                                </div>
                            </div>
                        </li>        
                    """.format(user_id=user_id, message_text=message.message_text, timestamp=timestamp)
                out_file.write(message_html_block)

            if past_segment_limit:
                break

        out_file.write("""
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </body>
        </html>"""
                       )

    with open(filename + '.txt', 'w', encoding='utf-8') as out_file:
        out_file.write(conversation_as_str)

    return return_idx

def xml_escape(chars, data_dict):
    return chars.encode('ascii', 'xmlcharrefreplace').decode()

def convert_emoji_to_html(input_string):
    output_string = ""
    for char in input_string:
        if emoji.is_emoji(char):
            output_string += "{E}"
        else:
            output_string += char
    return output_string

def get_html_header():
    return """
            <!DOCTYPE html>
            <html>
                <head>
                    <style>
                        body{
                            background:#eee;    
                        }
                        .chat-list {
                            padding: 0;
                            font-size: .8rem;
                        }

                        .chat-list li {
                            margin-bottom: 10px;
                            overflow: auto;
                            color: #ffffff;
                        }

                        .chat-list .chat-img {
                            float: left;
                            width: 80px;
                        }

                        .chat-list .chat-img img {
                            -webkit-border-radius: 50px;
                            -moz-border-radius: 50px;
                            border-radius: 50px;
                            width: 100%;
                        }

                        .chat-list .chat-message {
                            -webkit-border-radius: 50px;
                            -moz-border-radius: 50px;
                            border-radius: 50px;
                            background: #5a99ee;
                            display: inline-block;
                            padding: 10px 20px;
                            position: relative;
                            font: 1.2em "Fira Sans", sans-serif;
                            font-size: 49px;
                        }

                        .chat-list .chat-message:before {
                            content: "";
                            position: absolute;
                            top: 15px;
                            width: 0;
                            height: 0;
                        }

                        .chat-list .chat-message h5 {
                            margin: 0 0 5px 0;
                            font-weight: 600;
                            line-height: 100%;
                            font-size: 49px;
                        }

                        .chat-list .chat-message p {
                            margin: 0;
                            padding: 0;
                        }

                        .chat-list .chat-body {
                            margin-left: 20px;
                            float: left;
                            width: 70%;
                        }

                        .chat-list .in .chat-message:before {
                            left: -6px;
                            border-bottom: 20px solid transparent;
                            border-right: 20px solid #5a99ee;
                        }

                        .chat-list .out .chat-img {
                            float: right;
                        }

                        .chat-list .out .chat-body {
                            float: right;
                            margin-right: 20px;
                            text-align: right;
                        }

                        .chat-list .out .chat-message {
                            background: #fc6d4c;
                        }

                        .chat-list .out .chat-message:before {
                            right: -6px;
                            border-bottom: 20px solid transparent;
                            border-left: 20px solid #fc6d4c;
                        }

                        .card .card-header:first-child {
                            -webkit-border-radius: 0.3rem 0.3rem 0 0;
                            -moz-border-radius: 0.3rem 0.3rem 0 0;
                            border-radius: 0.3rem 0.3rem 0 0;
                        }
                        .card .card-header {
                            background: #17202b;
                            border: 0;
                            font-size: 1rem;
                            padding: .65rem 1rem;
                            position: relative;
                            font-weight: 600;
                            color: #ffffff;
                        }

                        .content{
                            margin-top:40px;    
                        }
                    </style>
                </head>
                <body>
                <div class="container content">
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12">
                            <div class="card">
                                <div class="card-body height3">
                                    <ul class="chat-list">
        """