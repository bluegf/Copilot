''' Program to run when the Copilot key is pressed. '''

'''
Copyright (c)2026 Damion James Edwards & BlueGF.
See LICENCE.txt for details (MIT No Attribution).

TODO Icon not working, convert from png to ico
TODO test on windows
'''

try:  # Shows my icon in Windows Explorer & Taskbar:
    from ctypes import windll  # Only exists on Windows hence using try/except
except ImportError:  # When not on windows - how will this work with generating executable with PyInstaller or similar?
    pass
else:
    myappid = 'com.bluegf.copilot'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QScreen
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

        icon = QIcon('copilot_icon.png')
        self.setWindowIcon(icon)
        self.setWindowTitle('Copilot')
        # self.setWindowTitle(' ')
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
