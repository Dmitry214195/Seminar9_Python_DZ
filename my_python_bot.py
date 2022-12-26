from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

bot = Bot(token = '5821296480:AAGbqEKoUMa94q_-jqeQ-of-qukQzjOZJjU')
updater = Updater(token = '5821296480:AAGbqEKoUMa94q_-jqeQ-of-qukQzjOZJjU')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id,"Отправте мне текст, и я удалю из текста все слова, содержащие 'абв'." )

def delete_words(update, context):
    string = update.message.text
    context.bot.send_message(update.effective_chat.id, f"{' '.join(filter(lambda word: 'абв' not in word.lower(), string.split()))}")   


start_handler = CommandHandler("start", start)
message_handler = MessageHandler(Filters.text, delete_words)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()