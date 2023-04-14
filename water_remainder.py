"""
Python based voice reminder app.

Image sources :
	1. https://www.clipartmax.com/middle/m2i8K9H7K9Z5H7K9_cup-clipart-silhouette-coffee-cup-clip-art/
	2. Pngguru.com.
"""


# Import the necessary packages
import notify2  # pip3 install notfiy2
import getpass  # get the name of the system
import os
import schedule  # pip3 install schedule
import time


def water_notification():
    print("Drink Water!!!")
    pwd = os.getcwd()  # get the current working directory.
    path_to_icon = pwd + "images/water.jpg"  # path to the water drop image.
    name = getpass.getuser()
    message = "Hello " + name
    notify2.init(message)
    n = notify2.Notification(message + " please drink water....", icon=path_to_icon)
    task = "espeak " + "'" + message + "please drink water" + "'" + " -s 150"
    os.system(task)  # execute the command using os module.
    n.set_urgency(notify2.URGENCY_NORMAL)  # set the urgency of the notification.
    n.set_timeout(100)  # set the time for
    n.show()  # show the notification to the user.


def wish():  # method to wish the user a morning or after noon or night based on time and give the date, day and time .
    pwd = os.getcwd()  # get the current working directory.
    name = getpass.getuser()
    current_time = time.localtime()
    if current_time[3] < 12:
        message = " Good Morining " + name
        task = "espeak " + "'" + message + " Have a nice day" + "'" + " -s 150"
    elif current_time[3] in range(12, 18):
        message = " Good Afternoon " + name
        task = "espeak " + "'" + message + " Hope you are fine" + "'" + " -s 150"
    else:
        message = " Good Evening " + name
        task = "espeak " + "'" + message + " Have a pleasant evening " + "'" + " -s 150"
    os.system(task)  # execute the command using os module.


def take_a_break():
    print("Take a break")
    pwd = os.getcwd()  # get the current working directory.
    path_to_icon = pwd + "images/break.jpeg"  # path to the water drop image.
    name = getpass.getuser()
    message = "Hello " + name
    notify2.init(message)
    n = notify2.Notification(message + " Take a break....", icon=path_to_icon)
    task = (
        "espeak " + "'" + message + "I think you need to take a break" + "'" + " -s 150"
    )
    os.system(task)  # execute the command using os module.
    n.set_urgency(notify2.URGENCY_NORMAL)  # set the urgency of the notification.
    n.set_timeout(100)  # set the time for
    n.show()  # show the notification to the user.


if __name__ == "__main__":
    wish()
    print("Hey there....")
    print("This is a simple reminder app in python!!!")
    # we schedule for every one hour to make a notification related to drink water.
    schedule.every().hour.do(water_notification)
    # for every 35 minutes we schedule the user to take a break
    schedule.every(35).minutes.do(take_a_break)
    schedule.every(480).minutes.do(wish)
    while True:
        schedule.run_pending()
        time.sleep(1)
