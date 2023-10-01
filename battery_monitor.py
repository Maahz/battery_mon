"""
This module monitors the battery percentage of a Windows PC and 
displays a notification when the battery is low.
"""
import sys
import psutil
import win10toast

BATTERY_LOW_PERCENTAGE = 20

# Create a ToastNotifier object
toaster = win10toast.ToastNotifier()

def get_battery_percentage():
    """
    Returns the current battery percentage of the PC.
    """
    battery = psutil.sensors_battery()
    percent = str(battery.percent)
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
        toaster.show_toast("Battery Low", "Your battery is at " + get_battery_percentage() + "%", duration=10)
        sys.exit()
