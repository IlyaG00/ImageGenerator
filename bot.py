import config
import telebot
import fusion

API_TOKEN = config.bot_key


bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    fusion.generate_image(message.text)
    image = open('decoded_image.jpg', 'rb')
    bot.send_photo(message.chat.id , image)

bot.infinity_polling()