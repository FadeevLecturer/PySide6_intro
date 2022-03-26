import sys

from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # buttons
        check_box = QCheckBox("Check box")
        push_button = QPushButton("Push button")
        layout.addWidget(check_box)
        layout.addWidget(push_button)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
