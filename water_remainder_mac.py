import pync
import time


def remainder():
    pync.notify(
        "Water time!",
        title="Water Reminder",
        message="It's time to drink some water!",
        sound="Ping",
        timeout=5,
    )


while True:
    time.sleep(10)
    remainder()
