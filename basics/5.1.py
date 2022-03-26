import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout
from PySide6.QtGui import QIcon, Qt, QPixmap


path_to_the_icon = os.path.join("..", "icons", "phys.png")
path_to_py_logo = os.path.join("..", "icons", "python.png")
path_to_qt_logo = os.path.join("..", "icons", "qt.png")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("My Qt Application")
        self.setWindowIcon(QIcon(path_to_the_icon))

        widget = QWidget(parent=self)
        self.setCentralWidget(widget)

        python_logo = QPixmap(path_to_py_logo)
        python_logo_label = QLabel()
        python_logo_label.setPixmap(python_logo)

        qt_logo = QPixmap(path_to_qt_logo)
        qt_logo_label = QLabel()
        qt_logo_label.setPixmap(qt_logo)

        layout = QHBoxLayout()
        layout.addWidget(python_logo_label, alignment=Qt.AlignCenter)
        layout.addWidget(qt_logo_label, alignment=Qt.AlignCenter)
        widget.setLayout(layout)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
