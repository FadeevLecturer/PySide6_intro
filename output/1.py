import sys
import os

from PySide6.QtWidgets import *
from PySide6.QtGui import *


path_to_the_image = os.path.join("..", "images", "msu.jpg")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel()
        pixmap = QPixmap(path_to_the_image)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
