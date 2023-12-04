from plyer import notification
import time

def notifier(t, m):
    notification.notify(title=t, message=m, app_name="not-an-app", timeout=5)



if __name__ == "__main__":
    warm = "big w"
    cold = "random explanation of the notification"
    while True:
        notifier(warm, cold)
        time.sleep(10)


'''
we can add any desired condition or input we like instead of this timely notification which works more like an alarm that goes off in it's own time infinitely but the whole point of adding this quote was to just write the quote because remember, this is a series of dummy projects, nothing matters.
'''

#addotionally, we can write pythonw {this file's path.py} in command prompt to make this notification program run in background with terminal closed. to close it, use task manager and end python task