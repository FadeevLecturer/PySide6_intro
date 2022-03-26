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
        push_button = QPushButton("Show message")
        push_button.clicked.connect(self.show_message)
        layout.addWidget(push_button)

    def show_message(self):
        QMessageBox.information(
            self,
            "My first dialog",
            "Hello, World!"
        )

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
