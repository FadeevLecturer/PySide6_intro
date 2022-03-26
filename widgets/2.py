import sys

from PySide6.QtWidgets import *

from colorwidget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300)

        red = ColorWidget("Red", parent=self)
        red.setGeometry(0, 0, 100, 100)

        green = ColorWidget("Green", parent=self)
        green.setGeometry(100, 100, 100, 100)

        blue = ColorWidget("Blue", parent=self)
        blue.setGeometry(200, 200, 100, 100)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
