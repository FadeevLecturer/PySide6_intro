import sys

from PySide6.QtWidgets import *

from colorwidget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = ColorWidget("Blue")
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
