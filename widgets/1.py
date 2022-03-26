import sys
from functools import partial

from PySide6.QtGui import Qt
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        main_layout = QVBoxLayout()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        # top row
        button = QPushButton("Button")
        label = QLabel("Label")
        label.setAlignment(Qt.AlignCenter)
        edit = QLineEdit()

        # bottom row
        enable_button = QPushButton("Enable")
        disable_button = QPushButton("Disable")
        show_button = QPushButton("Show")
        hide_button = QPushButton("Hide")

        # layout

        top_layout = QHBoxLayout()
        top_layout.addWidget(button)
        top_layout.addWidget(label)
        top_layout.addWidget(edit)
        main_layout.addLayout(top_layout)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(enable_button)
        bottom_layout.addWidget(disable_button)
        bottom_layout.addWidget(show_button)
        bottom_layout.addWidget(hide_button)
        main_layout.addLayout(bottom_layout)

        # connections
        for widget in [button, label, edit]:
            enable_button.clicked.connect(partial(widget.setEnabled, True))
            disable_button.clicked.connect(partial(widget.setDisabled, True))
            show_button.clicked.connect(widget.show)
            hide_button.clicked.connect(widget.hide)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
