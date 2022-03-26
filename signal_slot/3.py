import sys

from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # widgets
        line_edit = QLineEdit()
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(line_edit.clear)

        # layout
        layout = QHBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(clear_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
