import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout


class MPLLiveGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_plot()

        # widgets
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.navigation_bar = NavigationToolbar2QT(self.canvas, parent=self)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.navigation_bar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.t = 0

    def setup_plot(self):
        self.fig, self.ax = plt.subplots(figsize=(2, 2))
        self.x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(self.x)
        self.line, = self.ax.plot(self.x, y)

    def update_plot(self):
        self.t += 0.1
        y = np.sin(self.x - self.t)
        self.line.set_ydata(y)
        self.canvas.draw()


class MainWindow(QMainWindow):
    def __init__(self, fps=24):
        super().__init__()
        graph = MPLLiveGraph()
        self.setCentralWidget(graph)

        # timer
        self.timer = QTimer()
        self.timer.setInterval(1000 / fps)
        self.timer.timeout.connect(graph.update_plot)
        self.timer.start()


app = QApplication(sys.argv)
main_window = MainWindow(fps=300)
main_window.show()
app.exec()