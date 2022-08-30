from telegram.ext import *


def stm(u,c):
    u.message.reply_text(f"Hey {u.message.from_user.first_name},Welcome To This Bot")
    print(f"{u.message.from_user.username} Called Start")
def sh(u,c):
    a = ['Hacking...','Name:'+u.message.from_user.name,'tg id:'+u.message.from_user.username,'
