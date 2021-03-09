import telebot, subprocess, requests, sys, os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
OWNER_CHAT_ID = os.getenv('OWNER_CHAT_ID')
bot = telebot.TeleBot(TOKEN)

#check all message chat id
def check_chat_id(message):
    if message.chat.id != int(OWNER_CHAT_ID):
        bot.send_message(message.chat.id, "em co nguoi yeu roi nhe. anh dung tan em nua")
        warning_message ="anh oi thang "+str(message.chat.first_name)+" "+str(message.chat.last_name)+" no tan em"
        bot.send_message(OWNER_CHAT_ID,warning_message)
        bot.send_message(OWNER_CHAT_ID,"id cua no day anh nhe\n"+str(message.chat.id))
        return False
    return True

@bot.message_handler(func=check_chat_id,commands=['start', 'help'])
def send_hello(message):
    bot.reply_to(message, "Hello anh thanh dep trai, em la bot le")

@bot.message_handler(func=check_chat_id,commands=['tmate'])
def send_ssh_code(message):
    cmd1 = subprocess.run('tmate -S /tmp/tmate.sock new-session -d', capture_output=True,shell=True,text=True)
    cmd2 = subprocess.run('tmate -S /tmp/tmate.sock wait tmate-ready', capture_output=True,shell=True,text=True)
    cmd3 = subprocess.run("tmate -S /tmp/tmate.sock display -p '#{tmate_ssh}'",capture_output=True,shell=True,text=True)
    result = cmd3.stdout
    bot.send_message(message.chat.id, result)

@bot.message_handler(func=check_chat_id,content_types=['text'])
def run_shell(message):
    cmd = subprocess.run(message.text,shell=True,capture_output=True,text=True)
    result = cmd.stdout+"\n"+cmd.stderr
    if result == '\n':
        bot.send_message(message.chat.id,"oke anh")
    else:
        bot.send_message(message.chat.id,result)

def loop_polling():
    try:
        bot.polling(none_stop=True)
    except KeyboardInterrupt:
        exit()

    except requests.exceptions.ReadTimeout:
        print("error of ReadTimeout")
        sys.exit(143)

    except requests.exceptions.ConnectionError:
        print("error of connection")
        sys.exit(143)

    except:
        print("unknow")
        sys.exit(143)

loop_polling()
