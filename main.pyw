''' Program to run when the Copilot key is pressed. '''

APP_NAME: str = 'Copilot'
VERSION: str = '0.0.1'
REL_DATE: str = '20/12/2025'
AUTHOR: str = 'Damion James Edwards'
EMAIL: str = 'damion@bluegf.com'
COPYRIGHT: str = AUTHOR + ' & ' + 'BlueGF'
CHANGELOG: str = '''
0.0.1   DJE     20/12/2025  Initial commit
0.0.2   DJE     20/12/2025  Open pyside6 window
0.0.3   DJE     20/12/2025  Add text message to window, centre horizontally & vertically.
1.0.0   DJE     21/12/2025  First RC
1.0.1   DJE     21/12/2025  Fixed dates in changelog that have incorrect year
1.0.2   DJE     21/12/2025  Add "planned" versions
1.1.0   DJE     21/12/2025  Make window open in centre of the screen
PLANNED:
1.1.1   DJE     ??/12/2025  Complete notes explaining how to open this program from the Copilot key
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

try:  # Shows my icon in Windows Explorer & Taskbar:
    from ctypes import windll  # Only exists on Windows hence using try/except
except ImportError:  # When not on windows - how will this work with generating executable with PyInstaller or similar?
    pass
else:
    myappid: str = 'com.bluegf.copilot'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QScreen  #, QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel('No.')
        font = label.font()
        font.setBold(True)
        label.setFont(font)

        button = QPushButton('OK')
        button.clicked.connect(app.quit)

        layout = QVBoxLayout(self)
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        icon = QIcon('bluegf.ico')
        self.setWindowIcon(icon)
        self.setWindowTitle('Copilot button')
        self.setFixedSize(QSize(250, 100))

        self.setCentralWidget(MainWidget())


if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()

    # Place the window in the centre of the primary monitor:
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geometry = window.frameGeometry()
    geometry.moveCenter(center)
    window.move(geometry.topLeft())

    window.show()

    sys.exit(app.exec())  # Start the event loop

else:
    sys.exit('This is not a module, it should be run directly and not imported')
