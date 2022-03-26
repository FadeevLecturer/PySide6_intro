import sys

from PySide6.QtWidgets import *

from colorwidget import ColorWidget, rainbow_colors


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.setMovable(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.tabs.removeTab)

        for color in rainbow_colors:
            self.tabs.addTab(ColorWidget(color), color)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
