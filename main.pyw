''' Program to run when the Copilot key is pressed. '''

APP_NAME: str = 'Copilot'
VERSION: str = '0.0.1'
REL_DATE: str = '20/12/2025'
AUTHOR: str = 'Damion James Edwards'
EMAIL: str = 'damion@bluegf.com'
COPYRIGHT: str = AUTHOR + ' & ' + 'BlueGF'
CHANGELOG: str = '''
0.0.1   DJE     30/12/2025  Initial commit
0.0.2   DJE     30/12/2026  Open pyside6 window
0.0.3   DJE     30/12/2026  Add text message to window, centre horizontally & vertically.
'''

'''
This program will need to be linked to the Copilot (or another) key.
On Linux Mint 22.2 Cinnamon:
    1. Start Menu > Peferences > Keyboard
    2. In the Keyboard app, select the "Shortcuts" pane
    3. Click the "Add custom shortcut" button
    4. In the dialog box that opens, put a humsn readable "Name" in the 1st box
    5. Enter this command to run this program: "python main.pyw ??? TODO
    6. "Custom Shortcuts" in the left hand menu should now be selected, if not then select it
    7. At the bottom right, in the "Keyboard bindings" pane, click on the top "unassigned"
    8. Click on "unassigned" again so it changes to "Pick an accelerator"
    9. Press the Copilot key (or whatever ey you want)
    10. It should now read "Shift+Super+TouchpadOff"
    11. Now, if you press the Copilot key, the program will open
    Note: I entered "gnome-system-monitor" to run System Monitor (command found in Properties for the start menu entry)
To view or edit your customer shortcuts in the future, select "Custom Shortcuts" on the left hand side of the "Keyboard" application

TODO:
* How to package up the venv to be distributed / used elsewhere / bound to a key?
* Open the window in the centre of the screen
* Add an icon for the app?

'''

import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Copilot Button')
        self.setFixedSize(QSize(300, 200))

        label = QLabel('No.')

        button = QPushButton('OK!', self)
        button.setFixedSize(QSize(100, 40))
        button.clicked.connect(app.quit)

        #main_widget = QWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(button)

        # Set the central widget of the Window.
        self.setCentralWidget(layout)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  # Start the event loop.
else:
    sys.exit('This is not a module, it should be run directly and not imported')
