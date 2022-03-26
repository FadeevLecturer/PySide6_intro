import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()