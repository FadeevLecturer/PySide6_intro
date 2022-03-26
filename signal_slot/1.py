import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


def on_button_click():
    print("Button was pressed")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("Press me!", parent=self)
        button.clicked.connect(on_button_click)
        self.setCentralWidget(button)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
