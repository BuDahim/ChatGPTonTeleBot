from telebot import TeleBot

from api import get_rep


bot_token = '-----' # Telegram Bot Token

bot = TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def on_start(message):
    chat_id = message.chat.id
    text = "Welcome!"
    bot.send_message(chat_id, text)
    return


@bot.message_handler(func=lambda message: message.chat.id == 0000000001)
def on_send(message):
    chat_id = message.chat.id
    text = message.text

    bot.send_message(0000000002, text)
    bot.send_message(chat_id, "Done")

    return

@bot.message_handler(func=lambda message: message.chat.id not in [5958397353, 0000000001])
def on_starc(message):
    chat_id = message.chat.id
    text = "You are not authorized to access this bot."
    bot.send_message(chat_id, text)
    return

conversation_dict = {}

max_conversation_length = 5

def trim_conversation(chat_id):
    if len(conversation_dict[chat_id].split('\n')) > max_conversation_length:
        conversation_lines = conversation_dict[chat_id].split('\n')
        conversation_dict[chat_id] = '\n'.join(conversation_lines[-max_conversation_length:])

@bot.message_handler()
def on_message(message):
    chat_id = message.chat.id

    if chat_id not in conversation_dict:
        conversation_dict[chat_id] = ''

    prompt = message.text[:200]
    conversation_dict[chat_id] += prompt + '\n'
    bot.send_chat_action(chat_id, 'typing')
    response = get_rep(conversation_dict[chat_id])

    conversation_dict[chat_id] += response + '\n'

    bot.send_message(chat_id, response)

    trim_conversation(chat_id)

    #bot.send_message(0000000001, f"{chat_id} - {message.text}")
    #bot.send_message(0000000001, f"{chat_id} - {response}")

bot.infinity_polling()
