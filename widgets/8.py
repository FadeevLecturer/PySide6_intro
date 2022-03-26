import sys

from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layout = QFormLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        layout.addRow("Фамилия", QLineEdit())
        layout.addRow("Имя", QLineEdit())
        layout.addRow("Отчество", QLineEdit())
        layout.addRow("Год рождения", QSpinBox())
        layout.addRow("Гражданство РФ", QCheckBox())


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
