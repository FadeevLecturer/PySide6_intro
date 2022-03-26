import sys

from PySide6.QtWidgets import *

from colorwidget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layout = QGridLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        layout.addWidget(ColorWidget("Red"), 1, 1)
        layout.addWidget(ColorWidget("Green"), 2, 4)
        layout.addWidget(ColorWidget("Blue"), 3, 1, 1, 2)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
