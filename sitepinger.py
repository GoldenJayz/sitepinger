import requests
import time
import os
import tkinter as tk
from tkinter import *

app = tk.Tk()


app.title("Website Monitor")
app.minsize(width=400, height=400)
app.maxsize(width=750, height=750)



BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"



def sitemonitor(enter):
    while True:
        time.sleep(5)
        r = requests.get(enter)
        os.system('color 4')
        print(int(r.status_code))
        
        if r.status_code == requests.codes.ok:
            print(BLUE + "Site is up")
            
        else:
            print(YELLOW + "Site is down")


enter = tk.Entry(font=40)
enter.place(relwidth=0.65, relheight=1)
enter.pack()


label = tk.Label(text="Site Status:")
label.pack()

button1 = tk.Button(text="Ping site name", font=40, command=lambda: sitemonitor(enter.get()))
button1.pack()



app.mainloop()




