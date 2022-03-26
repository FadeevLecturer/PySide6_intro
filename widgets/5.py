import sys

from PySide6.QtWidgets import *

from colorwidget import ColorWidget, rainbow_colors


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        for color in rainbow_colors:
            layout.addWidget(ColorWidget(color))


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
