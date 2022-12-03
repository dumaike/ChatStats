from GenericChatClasses import GenericConversation, GenericConversationStats, GenericMessage, GenericStatBlock
from GenericChatClasses import GenericUserStats

import GenericChatUtils
import Config
import emoji


def conversation_to_reader(conversation: GenericConversation):
    # Some chat services don't sort their messages by time, so sort them
    # now.
    conversation.message_list = sorted(
        conversation.message_list, key=lambda x: x.timestamp)

    with open('conversation.html', 'w', encoding='utf-8') as out_file:      

        html_header = """
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
                            width: 48px;
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
                            font-size: .9rem;
                        }

                        .chat-list .chat-message p {
                            line-height: 18px;
                            margin: 0;
                            padding: 0;
                        }

                        .chat-list .chat-body {
                            margin-left: 20px;
                            float: left;
                            width: 70%;
                        }

                        .chat-list .in .chat-message:before {
                            left: -12px;
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
                            right: -12px;
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
                                <div class="card-header">Chat</div>
                                <div class="card-body height3">
                                    <ul class="chat-list">
        """
        out_file.write(html_header)
          
        # Read each message and append it to the output
        for idx, message in enumerate(conversation.message_list):
            user_id = "Mike" if message.user_id == "Self" else "Elena"

            # Message proprocessing            
            if len(message.message_text) == 0:
                message.message_text  = "*Image*"
            timestamp = GenericChatUtils.timestamp_to_datetime(message.timestamp)

            # CSS Styling
            message_html_block = ""
            if user_id == "Mike":
                message_html_block = """            
                    <li class="in">
                        <div class="chat-img">
                            <img alt="Avtar" src="michael_portrait_v03sm.jpg">
                        </div>
                        <div class="chat-body">
                            <div class="chat-message">
                                <h5>{user_id} - {timestamp}</h5>
                                <p>{message_text}</p>
                            </div>
                        </div>
                    </li>                
                """.format(user_id=user_id, message_text = message.message_text, timestamp=timestamp)
            else:
                message_html_block = """
                    <li class="out">
                        <div class="chat-img">
                            <img alt="Avtar" src="Elena.jpg">
                        </div>
                        <div class="chat-body">
                            <div class="chat-message">
                                <h5>{user_id} - {timestamp}</h5>
                                <p>{message_text}</p>
                            </div>
                        </div>
                    </li>        
                """.format(user_id=user_id, message_text = message.message_text, timestamp=timestamp)

            out_file.write(message_html_block)      

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
                  
            
