from telegram.ext import *
import time


def stm(u,c):
    u.message.reply_text(f"Hey {u.message.from_user.first_name},Welcome To This Bot")
    print(f"{u.message.from_user.username} Called Start")
def sh(u,c):
    a = ['Name:'+u.message.from_user.name,'tg id:'+u.message.from_user.username,'Tracking Connected Mobile Number...','Mobile:01902611354','Tracking Email','Failed','Failed','One Email Found!','email:shihabalter@gmail.com','Hacking More.....']
    m = "Hacking..."
    mg = u.message.reply_text(m)
    for i in a:
        time.sleep(0.5)
        m = m+'\n'+i
        mg.edit_text(m)
    time.sleep(0.5)
    mg.edit_text("Bye Bye....")


