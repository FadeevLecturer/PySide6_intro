import sys
import os

from PySide6.QtCore import QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class ToggleButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setCheckable(True)
        self.setChecked(True)
        self.setFlat(True)
        self.clicked.connect(self.updateIcon)
        self.icon_on = QIcon(os.path.join("../..", "icons", "on-button.png"))
        self.icon_off = QIcon(os.path.join("../..", "icons", "off-button.png"))
        self.updateIcon()

    def updateIcon(self):
        if self.isChecked():
            self.setIcon(self.icon_on)
        else:
            self.setIcon(self.icon_off)
        self.setIconSize(QSize(40, 30))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        main_layout = QVBoxLayout()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        # top row
        self.button = QPushButton("Button")
        self.label = QLabel("Label")
        self.label.setAlignment(Qt.AlignCenter)
        self.edit = QLineEdit()

        # bottom row
        self.enable_button = ToggleButton("Enable")
        self.show_button = ToggleButton("Show")

        # layout
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.button)
        top_layout.addWidget(self.label)
        top_layout.addWidget(self.edit)
        main_layout.addLayout(top_layout)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.enable_button)
        bottom_layout.addWidget(self.show_button)
        main_layout.addLayout(bottom_layout)

        # connections
        self.enable_button.clicked.connect(self.on_button_enable_click)
        self.show_button.clicked.connect(self.on_button_show_click)

    def on_button_show_click(self):
        for widget in [self.button, self.label, self.edit]:
            widget.setVisible(self.show_button.isChecked())

    def on_button_enable_click(self):
        for widget in [self.button, self.label, self.edit]:
            widget.setEnabled(self.enable_button.isChecked())


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
