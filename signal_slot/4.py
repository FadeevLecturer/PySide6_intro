import sys

from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # widgets
        source = QLineEdit()
        destination = QLineEdit()
        copy_paste_button = QPushButton("Copy and paste")
        copy_paste_button.clicked.connect(lambda: destination.setText(source.text()))

        # layout
        layout = QHBoxLayout()
        layout.addWidget(source)
        layout.addWidget(copy_paste_button)
        layout.addWidget(destination)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
