import telebot
from email import message_from_file
import random
from telebot.apihelper import send_photo

bot = telebot.TeleBot("903291505:AAGLOqbRaGHEaGzkMTcq3b9cI6WQoa-zbbg")
cont=0
@bot.message_handler(commands=['start', 'help'])
def joc(message):
    #while(cont<10):
    bot.send_message(message.chat.id, "Cual es este pokemon?")
    buscaPokemon(message)
       
    


def buscaPokemon(message):
    with open("LlistaNoms.txt") as f:
        #a=random.randint(1,151)
        a=7
        bot.send_photo(message.chat.id, "https://drive.google.com/open?id=1UHq7u5Czg1-bKt6mqx7TxmHrLFFZpMVD")
        
        for i in range(151):
            nom= f.readline()[4:]
            if i == a-1:
                print(nom)
                break

bot.polling(none_stop=True)