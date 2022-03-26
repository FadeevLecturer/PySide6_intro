import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QIcon, Qt


path_to_the_icon = os.path.join("..", "icons", "phys.png")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("My Qt Application")
        self.setWindowIcon(QIcon(path_to_the_icon))

        self.label = QLabel("Hello, World!",  parent=self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
