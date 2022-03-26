import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *

dark = (119, 149, 86)
light = (235, 236, 208)


class ChessBoard(QImage):
    def __init__(self):
        super().__init__(8, 8, QImage.Format_RGB16)
        for i in range(8):
            for j in range(8):
                color = dark if (i + j) % 2 else light
                self.setPixelColor(i, j, QColor(*color))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel()
        image = ChessBoard()
        pixmap = QPixmap(image)
        pixmap.setDevicePixelRatio(0.025)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
