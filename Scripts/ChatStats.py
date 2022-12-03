import Config
import RawChatIntakeConverter
import GenericChatAnalyzer
import StatBlockProcessor
import ConversationReaderProcessor

conversation = RawChatIntakeConverter.google_messages_to_generic(
    Config.file_path)

stat_block = GenericChatAnalyzer.conversation_to_stat_blocks(conversation)

ConversationReaderProcessor.conversation_to_reader(conversation)
#StatBlockProcessor.process_stats(stat_block)