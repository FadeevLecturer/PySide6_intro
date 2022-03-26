import sys

from PySide6.QtWidgets import *


class ChangeTitleQuestion(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setText('Change the window title to "Hello, World!" string?')
        self.setIcon(QMessageBox.Question)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setMinimumWidth(300)

        # buttons
        push_button = QPushButton("Show question")
        push_button.clicked.connect(self.show_question)
        layout.addWidget(push_button)

    def show_question(self):
        message_box = ChangeTitleQuestion(parent=self)

        ret = message_box.exec()
        if ret == QMessageBox.Yes:
            self.setWindowTitle("Hello, World!")


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
