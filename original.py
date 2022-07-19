import telebot
import os
import dotenv

dotenv.load_dotenv('.env')

bot = telebot.TeleBot(os.environ['API_KEY'])
users = set()

@bot.message_handler(func=lambda message: not message.from_user.is_bot)
def on_message(message):
    print(message)
    bot.send_message(message.from_user.id, "Ваше сообщение отправлено!")
    users.add(message.from_user.id)
    for user in users:
        if user != message.from_user.id:
            bot.send_message(user, message.text)


bot.polling(none_stop=True)