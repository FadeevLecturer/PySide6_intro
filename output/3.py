import sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

from PySide6.QtWidgets import *


def plot():
    fig, ax = plt.subplots(figsize=(2, 2))
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    ax.plot(x, y)
    return fig


class MPLGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.fig = plot()

        # widgets
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.navigation_bar = NavigationToolbar2QT(self.canvas, parent=self)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.navigation_bar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        graph = MPLGraph()
        graph.setLayout(layout)
        self.setCentralWidget(graph)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()