import telebot
from dotenv import load_dotenv
import os
import screenshot



# send photos to bot
def main():
    load_dotenv('.env')
    TOKEN = os.getenv("TG_TOKEN")
    ID_TG1 = os.getenv("ID_TG1")
    bot = telebot.TeleBot(TOKEN, parse_mode=None)
    for i in range(1, 6):
        photo = f'ss{i}.png'
        with open(photo, 'rb') as photo_file:
            bot.send_photo(ID_TG1, photo_file)

if __name__=='__main__':
    main()