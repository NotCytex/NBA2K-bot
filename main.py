import bot
import threading
import keyboard

flag = [True]

def stop():
    global flag
    keyboard.wait('q')
    flag[0] = False

bot_thread = threading.Thread(target=bot.main, args=(flag,), daemon=True)
stop_thread = threading.Thread(target=stop)

print("NBA2K Bot\nPress Q to end")
bot_thread.start()
stop_thread.start()

stop_thread.join()



