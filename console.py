import ctypes

# Constants
SW_HIDE = 0
SW_SHOW = 5

def hide(bool = True):

    # Get a handle to the console window
    console_handle = ctypes.windll.kernel32.GetConsoleWindow()

    #Check if bool was true or false
    if bool:
        # Show the console window
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), SW_HIDE)
    else:
        # Hide the console window
        ctypes.windll.user32.ShowWindow(console_handle, SW_SHOW)