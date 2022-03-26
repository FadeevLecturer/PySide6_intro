import sys

from PySide6.QtWidgets import *

from colorwidget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        red = ColorWidget("Red")
        red.setMinimumWidth(100)
        red.setMaximumWidth(200)
        violet = ColorWidget("Violet")
        violet.setMinimumWidth(100)
        violet.setMaximumWidth(200)

        layout.addWidget(red, stretch=1)
        layout.addStretch(2)
        layout.addWidget(violet, stretch=1)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
