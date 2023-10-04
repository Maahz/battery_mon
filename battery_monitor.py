"""
This module monitors the battery percentage of a Windows PC and 
displays a notification when the battery is low.
"""
import sys
import time
import psutil
import win10toast

import console

BATTERY_LOW_PERCENTAGE = 20

console.hide()

# Create a ToastNotifier object
toaster = win10toast.ToastNotifier()

def get_battery_percentage():
    """
    Returns the current battery percentage of the PC.
    """
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    return percent

def is_battery_low():
    """
    Returns True if the battery percentage is lower than or equal to 
    the BATTERY_LOW_PERCENTAGE constant, False otherwise.
    """
    percent = get_battery_percentage()
    if percent <= BATTERY_LOW_PERCENTAGE:
        return True
    else:
        return False
    

while True:
    if is_battery_low():
        toaster.show_toast("Battery Low", "Your battery is at " + str(get_battery_percentage()) + "%", duration=10)
        sys.exit()
    time.sleep(10)
