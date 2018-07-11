import time
from datetime import datetime as dt

host_path = r"C:\Windows\hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "www.google.com", "www.yahoo.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print ("working hours")
        with open(host_path, 'r+') as hfile:
            content = hfile.read()
            for w in websites:
                if w in content:
                    pass
                else:
                    hfile.write(redirect + "  " + w + '\n')
    else:
        print ("fun hours")
        with open(host_path, 'r+') as hfile:
            content = hfile.readlines()
            hfile.seek(0)
            for lines in content:
                if not any(w in lines for w in websites):
                    hfile.write(lines)
            hfile.truncate()

    time.sleep(3)
