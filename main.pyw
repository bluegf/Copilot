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
0.0.3   DJE     xx/xx/2026  .
'''

'''
This program will need to be linked to the Copilot (or another) key.
On Linux Mint 22.2 Cinnamon:
    1. Start Menu > Peferences > Keyboard
    2. In the Keyboard app, select the "Shortcuts" pane
    3. Click the "Add custom shortcut" button
    4. In the dialog box that opens, put a humsn readable "Name" in the 1st box
    5. Enter this command to run this program: "python main.pyw ??? TODO
    Note: I entered "gnome-system-monitor" to run System Monitor (command found in Properties for the start menu entry)
To view or edit your customer shortcuts in the future, select "Custom Shortcuts" on the left hand side of the "Keyboard" application

TODO:
* How to package up the venv to be distributed / used elsewhere / bound to a key?

'''

import sys

from PySide6.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication([])
    window = QWidget()
    window.show()

    app.exec()  # Start the event loop.

    # Your application won't reach here until you exit and the event
    # loop has stopped.
else:
    sys.exit('This is not a module, it should be run directly and not imported')
