from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSystemTrayIcon, QMenu, QAction, QStyleFactory
from threading import Thread
from pythoncom import CoInitialize
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import win32com.client
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStyleFactory, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class EmailThread(Thread):
    def __init__(self, app):
        Thread.__init__(self)
        self.app = app
        self.is_running = False

    def run(self):
        CoInitialize()  # Initialize COM in this thread

        # Connect to Outlook
        outlook = win32com.client.Dispatch("Outlook.Application")
        namespace = outlook.GetNamespace("MAPI")

        # Access the main Inbox folder
        inbox = namespace.GetDefaultFolder(6)

        # Access the "Support Tickets" subfolder
        inbox = inbox.Folders['Support Tickets']

        while self.is_running:
            try:
                # Get all the unread emails in the inbox
                messages = inbox.Items.Restrict("[Unread] = True")

                for message in messages:
                    if self.app.target_subject in message.Subject:
                        # Mark the email as read
                        message.UnRead = False

                        # Check if all words in a target phrase are in the email body
                        body_lower = message.Body.lower()
                        for phrase in self.app.target_phrases:
                            if all(word.lower() in body_lower for word in phrase.split()):
                                # Perform ticket handling action
                                self.app.handle_ticket()
            except Exception as e:
                print("An error occurred while processing emails:", str(e))
                time.sleep(2)  # Wait for 2 seconds before trying again

        print("Email monitoring stopped.")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set the subject of the emails you want to monitor
        self.target_subject = "Your Ticket Has Been Received"

        # Set the phrases to detect in the email body
        self.target_phrases = ["email release", "release email", "proofpoint release", "release from proofpoint", 
                          "release an email", "Proofpoint Quarantine", "proofpoint", "release an email"]

        # Initialize the email thread
        #self.email_thread = EmailThread(self)

    def setup(self):
        # Setup Selenium
        try:
            options = webdriver.ChromeOptions() 
            options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Suppress USB error logs
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            print("Selenium setup completed.")
        except Exception as e:
            print("Error setting up Selenium:", str(e))

        # Create the system tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))  # Set icon to a standard icon
        self.tray_icon.setVisible(True)
        self.tray_icon.setToolTip('Email Monitoring App')  # Tooltip for the tray icon

        # Create a menu for the system tray icon
        self.tray_menu = QMenu(self)
        self.tray_action = QAction('Show/Hide', self)
        self.tray_action.triggered.connect(self.toggle_visibility)
        self.tray_menu.addAction(self.tray_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()

        # Start the email thread
        self.email_thread.is_running = True
        self.email_thread.start()
        print("Starting email monitoring...")

def main():
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))

    main_win = MainWindow()
    main_win.show()

    main_win.setup()  # Call the setup method after showing the window

    app.exec_()
