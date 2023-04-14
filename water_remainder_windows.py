from plyer import notification
import time


def remainder():
    notification.notify(
        title="Water Reminder",
        message="It's time to drink some water!",
        app_icon="water.ico",
        timeout=5,
    )


while True:
    time.sleep(10)
    remainder()
