import sys

from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def mousePressEvent(self, event):
        button_name = event.button().name.decode()
        pos = event.position()
        x, y = pos.x(), pos.y()
        print(f"{button_name:12} mouse button was pressed at x={int(x):3d} and y={int(y):3d}")


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
