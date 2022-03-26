import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton


class IgnoringButton(QPushButton):
    def mousePressEvent(self, event):
        event.ignore()


class AcceptingButton(QPushButton):
    def mousePressEvent(self, event):
        event.accept()
        print("A mouse button was pressed at the accepting button")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget(parent=self)
        self.setCentralWidget(widget)

        layout = QHBoxLayout()
        layout.addWidget(AcceptingButton("Accept"))
        layout.addWidget(IgnoringButton("Ignore"))
        widget.setLayout(layout)

    def mousePressEvent(self, event):
        print("A mouse button was pressed at the main window")


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
