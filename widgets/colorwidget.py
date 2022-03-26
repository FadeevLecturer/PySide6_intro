from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget

rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Magenta", "Violet"]


class ColorWidget(QWidget):
    def __init__(self, color, parent=None):
        super().__init__(parent=parent)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
