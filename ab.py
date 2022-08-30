from telegram.ext import *
import time


def stm(u,c):
    u.message.reply_text(f"Hey {u.message.from_user.first_name},Welcome To This Bot")
    print(f"{u.message.from_user.username} Called Start")
def sh(u,c):
    a = ['Name:'+u.message.from_user.first_name,'tg id:'+'@'+u.message.from_user.username,'Tracking Connected Mobile Number...','Mobile:01902611354','Tracking Email','Failed','Failed','One Email Found!','email:shihabalter@gmail.com','Hacking More.....']
    m = "Hacking..."
    mg = u.message.reply_text(m)
    for i in a:
        time.sleep(0.5)
        m = m+'\n'+i
        mg.edit_text(m)
    time.sleep(3)
    mg.edit_text("Hacked......Bye Bye")
    print(f"{u.message.from_user.username} Called Sh")
def hlp(u,c):
    u.message.reply_text("Bot Chalaite Janena abar bot chalaite aise....vag shala")
    print(f"{u.message.from_user.username} Called Help")

upd = Updater("5691718016:AAHdL1iSJV994xw2gv7qtzAyfwPEBYLXA5A", use_context=True)

upd.dispatcher.add_handler(CommandHandler("start",stm))
upd.dispatcher.add_handler(CommandHandler("sahos_thakle_ei_command_run_kor",sh))
upd.dispatcher.add_handler(CommandHandler("help",hlp))

upd.start_polling()
upd.idle()





