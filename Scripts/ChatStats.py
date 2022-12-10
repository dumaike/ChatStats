import Config
import RawChatIntakeConverter
import GenericChatAnalyzer
import StatBlockProcessor
import ConversationViewerProcessor

conversation = RawChatIntakeConverter.google_messages_to_generic(
    Config.file_path)

stat_block = GenericChatAnalyzer.conversation_to_stat_blocks(conversation)

if Config.output_type == Config.Output.STATS:
    StatBlockProcessor.process_stats(stat_block)
elif Config.output_type == Config.Output.VIEWER:
    ConversationViewerProcessor.conversation_to_viewer(conversation)
else:    
    StatBlockProcessor.process_stats(stat_block)