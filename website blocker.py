import time
from datetime import datetime

host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect_ip = "127.0.0.1"

start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute)
end_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute + 5)

site = "www.example.com"

while True:
    if datetime.now() < end_time:
        with open(host_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if site in lines:
                pass
            else:
                file.write(redirect_ip + " " + site + "\n")
            file.truncate()

    else:
        with open(host_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            if site in lines:
                file.truncate()

'''
it's giving me PermissionError, Errno 13, at line 14.
tried running command prompt as administrator and running the script directly from there.
please help.
'''