import time
from threading import Thread
from pythoncom import CoInitialize

import pyautogui
import win32com.client
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QTimer

# Set the coordinates of the refresh button in Chrome
refresh_button_x = 91
refresh_button_y = 207

# Set the coordinates for the Chrome tab
tab_x = 126
tab_y = 13

# Initialize the program state
is_running = False

# Function to perform auto-refresh
def refresh_website():
    # Activate the tab
    pyautogui.click(tab_x, tab_y)
    time.sleep(0.25)  # Add half-second delay

    # Activate the Chrome window
    pyautogui.click(refresh_button_x, refresh_button_y)

    # Wait for the website to load (adjust if needed)
    time.sleep(2)

# Function to handle program start/stop
def toggle_program():
    global is_running

    if is_running:
        is_running = False
        start_stop_btn.setText("Start")
        print("Program deactivated")
    else:
        is_running = True
        start_stop_btn.setText("Stop")
        print("Program activated")

    # Refresh the website whenever the state changes
    refresh_website()

# Create the main UI window using PyQt5
app = QApplication([])
window = QWidget()
window.setWindowTitle("Email Monitor")
window.setGeometry(100, 100, 200, 100)

# Set a dark color theme for the window
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
palette.setColor(QPalette.Text, QColor(255, 255, 255))
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
palette.setColor(QPalette.Highlight, QColor(142, 45, 197).lighter())
palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
app.setPalette(palette)

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

# Minimize the Python console window
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

# Run the application event loop
app.exec_()
