import sys
import os

from PySide6.QtGui import *
from PySide6.QtWidgets import *


class ChooseIcon(QGroupBox):
    def __init__(self):
        super().__init__("Window icon and title")

        # icons
        self.python_icon = QIcon(os.path.join("../..", "icons", "python.png"))
        self.qt_icon = QIcon(os.path.join("../..", "icons", "qt.png"))
        self.phys_icon = QIcon(os.path.join("../..", "icons", "phys.png"))

        # buttons
        self.python_button = QRadioButton("Python")
        self.python_button.setIcon(self.python_icon)

        self.qt_button = QRadioButton("Qt")
        self.qt_button.setIcon(self.qt_icon)

        self.phys_button = QRadioButton("Faculty of physics")
        self.phys_button.setIcon(self.phys_icon)

        # ButtonGroup
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.python_button)
        self.button_group.addButton(self.qt_button)
        self.button_group.addButton(self.phys_button)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.python_button)
        layout.addWidget(self.qt_button)
        layout.addWidget(self.phys_button)
        self.setLayout(layout)

        # activating one button
        self.python_button.setChecked(True)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 250, 130)
        self.choose_icon = ChooseIcon()
        self.setCentralWidget(self.choose_icon)
        self.update_bar()
        self.choose_icon.button_group.buttonClicked.connect(self.update_bar)

    def update_bar(self):
        active_button = self.choose_icon.button_group.checkedButton()
        text = active_button.text()
        icon = active_button.icon()
        self.setWindowTitle(text)
        self.setWindowIcon(icon)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
