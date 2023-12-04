from tkinter import *
import os

shut_down_window = Tk()

shut_down_window.title("shut down app")
shut_down_window.geometry("200x200")
shut_down_window.config(bg="yellow")

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def log_out():
    os.system("shutdown /l")
def shut_down():
    os.system("shutdown /s /t 1")

restart_button = Button(shut_down_window, text="restart", font=("Time New Roman", 10, "bold"), relief=RAISED, cursor="plus", command=restart)
restart_button.place(x=50, y=60, height=20, width=100)

restart_time_button = Button(shut_down_window, text="restart time", font=("Time New Roman", 10, "bold"), relief=RAISED, cursor="plus",command=restart_time)
restart_time_button.place(x=50, y=81, height=20, width=100)

log_out_button = Button(shut_down_window, text="log out", font=("Time New Roman", 10, "bold"), relief=RAISED, cursor="plus", command=log_out)
log_out_button.place(x=50, y=102, height=20, width=100)

shut_down_button = Button(shut_down_window, text="shut down", font=("Time New Roman", 10, "bold"), relief=RAISED, cursor="plus", command=shut_down)
shut_down_button.place(x=50, y=123, height=20, width=100)



shut_down_window.mainloop()