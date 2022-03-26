import os.path
import sys

from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # buttons
        self.label = QLabel("An image will be displayed here")
        push_button = QPushButton("Choose Image")
        layout.addWidget(self.label)
        layout.addWidget(push_button)

        # connections
        push_button.clicked.connect(self.choose_image)

    def choose_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            caption="Pick an image",
            dir=os.path.join("..", "images"),
            filter="Images (*.png *.xpm *.jpg)"
        )
        if path:
            self.label.setPixmap(QPixmap(path))


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
