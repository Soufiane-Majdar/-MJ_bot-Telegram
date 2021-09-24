import schedule
import time
import telegram_send 
from threading import Thread
def wake_up():
    try:
        
        def wakeup():
            telegram_send.send(messages=['it is time to wake up ..'])
            telegram_send.send(messages=["wake up !!!"])
            telegram_send.send(messages=["wake up !!"])
            telegram_send.send(messages=["wake up !"])

        schedule.every().day.at('07:00').do(wakeup)
 

        while True:
            schedule.run_pending()
            time.sleep(1)

                


    except:
        print('erreur!..')
        wake_up()

wake_up()