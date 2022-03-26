import sys

from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        main_layout = QVBoxLayout()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        # edit
        self.edit = QLineEdit()
        self.edit.setClearButtonEnabled(True)

        # buttons row
        clear_button = QPushButton("Clear")
        copy_button = QPushButton("Copy")
        paste_button = QPushButton("Paste")
        select_button = QPushButton("Select all")

        # labels
        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignLeft)

        # checkboxes
        self.is_password = QCheckBox("password")
        self.numbers_only = QCheckBox("numbers only")

        # layout
        main_layout.addWidget(self.edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(clear_button)
        button_layout.addWidget(copy_button)
        button_layout.addWidget(paste_button)
        button_layout.addWidget(select_button)
        main_layout.addLayout(button_layout)

        main_layout.addWidget(self.label)

        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(self.is_password)
        checkbox_layout.addWidget(self.numbers_only)
        main_layout.addLayout(checkbox_layout)

        # connections
        clear_button.clicked.connect(self.edit.clear)
        copy_button.clicked.connect(self.edit.copy)
        paste_button.clicked.connect(self.edit.paste)
        select_button.clicked.connect(self.edit.selectAll)
        self.edit.editingFinished.connect(self.sync)
        self.is_password.stateChanged.connect(self.update_echo_mode)
        self.numbers_only.stateChanged.connect(self.update_validator)

    def sync(self):
        self.label.setText(self.edit.text())

    def update_echo_mode(self):
        mode = QLineEdit.Password if self.is_password.isChecked() else QLineEdit.Normal
        self.edit.setEchoMode(mode)

    def update_validator(self):
        validator = QIntValidator() if self.numbers_only.isChecked() else None
        validator.setBottom(0)
        self.edit.setValidator(validator)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
