import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import *


class CountingLabel(QLabel):
    def __init__(self, text):
        super().__init__(f"{text}\n{0:3d}")

        self.text = text
        self.setAlignment(Qt.AlignCenter)
        self.counter = 0

    def increment(self):
        self.counter += 1
        self.setText(f"{self.text}\n{self.counter:3d}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # top row
        left_label = CountingLabel("Left")
        right_label = CountingLabel("Right")

        # bottom row
        left_button = QPushButton("Increment left")
        middle_button = QPushButton("Increment both")
        right_button = QPushButton("Increment right")

        # layout
        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        top_layout.addWidget(left_label)
        top_layout.addWidget(right_label)
        main_layout.addLayout(top_layout)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(left_button)
        bottom_layout.addWidget(middle_button)
        bottom_layout.addWidget(right_button)
        main_layout.addLayout(bottom_layout)

        # connections
        left_button.clicked.connect(left_label.increment)
        middle_button.clicked.connect(left_label.increment)
        middle_button.clicked.connect(right_label.increment)
        right_button.clicked.connect(right_label.increment)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
