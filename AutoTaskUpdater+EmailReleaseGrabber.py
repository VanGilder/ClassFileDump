#Install these python libraries: use cmd prompt once python 3.11 is installed
# py -3.11 -m pip install pyautogui
# py -3.11 -m pip install PyQt5
# py -3.11 -m pip install pywin32


import time
from threading import Thread
from pythoncom import CoInitialize

import pyautogui
import win32com.client
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QTimer

# Set the coordinates of the refresh button in Chrome
refresh_button_x = 80
refresh_button_y = 197

# Set the coordinates for the Chrome tab
tab_x = 133
tab_y = 13

# Set the subject of the emails you want to monitor
target_subject = "Your Ticket Has Been Received"

# Set the phrases to detect in the email body
target_phrases = ["email release", "release email", "proofpoint release", "release from proofpoint", "release an email", "Proofpoint Quarantine", "proofpoint", "release an email"]

# Set the autoclick coordinates for each detected phrase
autoclick_coordinates = {
    "email release": [(36, 284), (58, 243), (113, 274)],
    "release email": [(36, 284), (58, 243), (113, 274)],
    "proofpoint release": [(36, 284), (58, 243), (113, 274)],
    "release from proofpoint": [(36, 284), (58, 243), (113, 274)],
    "release an email": [(36, 284), (58, 243), (113, 274)],
    "proofpoint": [(36, 284), (58, 243), (113, 274)],
    "release an email": [(36, 284), (58, 243), (113, 274)],
    "an email": [(36, 284), (58, 243), (113, 274)]
}

# Set the URL of the website you want to refresh
website_url = "https://ww15.autotask.net/Mvc/Framework/Navigation.mvc/Landing"

# Initialize the program state
is_running = False

class EmailThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        CoInitialize()  # Initialize COM in this thread

        # Connect to Outlook
        outlook = win32com.client.Dispatch("Outlook.Application")
        namespace = outlook.GetNamespace("MAPI")

        # Access the main Inbox folder
        inbox = namespace.GetDefaultFolder(6)

        # Access the "Support Tickets" subfolder
        inbox = inbox.Folders['Support Tickets']

        while is_running:
            try:
                # Get all the unread emails in the inbox
                messages = inbox.Items.Restrict("[Unread] = True")

                for message in messages:
                    if target_subject in message.Subject:
                        # Activate the tab
                        pyautogui.click(tab_x, tab_y)
                        time.sleep(0.2)  # Add half-second delay

                        # Activate the Chrome window
                        pyautogui.click(refresh_button_x, refresh_button_y)

                        # Wait for the website to load (adjust if needed)
                        time.sleep(2)

                        # Mark the email as read
                        message.UnRead = False

                        # Check if any target phrase is in the email body
                        for phrase in target_phrases:
                            if phrase.lower() in message.Body.lower():
                                # Perform autoclick actions based on the detected phrase
                                autoclick_coords = autoclick_coordinates[phrase]
                                for click_coords in autoclick_coords:
                                    pyautogui.click(click_coords[0], click_coords[1])
                                    time.sleep(0.5)  # Add half-second delay

            except Exception as e:
                print("An error occurred while processing emails:", str(e))
                time.sleep(2)  # Wait for 2 seconds before trying again

        print("Email monitoring stopped.")

# Create the main UI window using PyQt5
app = QApplication([])
window = QWidget()
window.setWindowTitle("Email Monitor")
window.setGeometry(100, 100, 200, 100)

# Function to handle program start/stop
def toggle_program():
    global is_running, email_thread

    if  is_running:
        is_running = False
        start_stop_btn.setText("Start")
    else:
        is_running = True
        start_stop_btn.setText("Stop")
        email_thread = EmailThread()
        email_thread.start()

# Function to perform auto-refresh
def refresh_website():
    # Activate the tab
    pyautogui.click(tab_x, tab_y)
    time.sleep(0.25)  # Add half-second delay

    # Activate the Chrome window
    pyautogui.click(refresh_button_x, refresh_button_y)

    # Wait for the website to load (adjust if needed)
    time.sleep(2)

# Create the start/stop button
start_stop_btn = QPushButton("Start", window)
start_stop_btn.setGeometry(50, 30, 100, 30)
start_stop_btn.clicked.connect(toggle_program)

# Schedule auto-refresh every 5 minutes
refresh_timer = QTimer()
refresh_timer.timeout.connect(refresh_website)
refresh_timer.start(5 * 60 * 1000)  # 5 minutes

# Show the UI window
window.show()

# Run the application event loop
app.exec_()
