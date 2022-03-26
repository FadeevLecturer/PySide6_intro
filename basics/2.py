import sys

from PySide6.QtWidgets import QApplication, QMainWindow


app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.show()
app.exec()
print("Application is closed!")