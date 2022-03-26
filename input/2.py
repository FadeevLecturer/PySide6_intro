import sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MPLGraph(FigureCanvasQTAgg):
    def __init__(self):
        fig, ax = plt.subplots(figsize=(2, 2))
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        self.x = np.linspace(0, 2 * np.pi, 1000)
        self.line, = ax.plot(self.x, self.x)
        super().__init__(fig)

    def update_power(self, power):
        y = self.x ** power
        self.line.set_ydata(y)
        self.draw()

    def update_linewidth(self, width):
        self.line.set_linewidth(width)
        self.draw()

    def update_color(self, color):
        self.line.set_color(color)
        self.draw()


class PowerSpinBox(QSpinBox):
    def __init__(self):
        super().__init__()
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(1)
        self.setPrefix("Power: ")


class RainbowColorSpinBox(QSpinBox):
    colors = ["red",
              "orange",
              "yellow",
              "green",
              "blue",
              "magenta",
              "violet"]

    def __init__(self):
        super().__init__()
        self.setMinimum(0)
        self.setMaximum(6)

    def textFromValue(self, val):
        return self.colors[val]


class LineWidthSpinBox(QDoubleSpinBox):
    def __init__(self):
        super().__init__()
        self.setMinimum(0.1)
        self.setMaximum(10)
        self.setSingleStep(0.1)
        self.setValue(1.)
        self.setSuffix(" px")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 400)
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # widgets
        graph = MPLGraph()

        linewidth_sb = LineWidthSpinBox()
        linewidth_label = QLabel("Line width")
        linewidth_label.setAlignment(Qt.AlignRight)

        power_sb = PowerSpinBox()
        power_label = QLabel("Power")
        power_label.setAlignment(Qt.AlignRight)

        color_sb = RainbowColorSpinBox()
        color_label = QLabel("Color")
        color_label.setAlignment(Qt.AlignRight)


        # layout
        layout.addWidget(graph)

        bottom_row = QHBoxLayout()
        bottom_row.addWidget(linewidth_label)
        bottom_row.addWidget(linewidth_sb)
        bottom_row.addWidget(power_label)
        bottom_row.addWidget(power_sb)
        bottom_row.addWidget(color_label)
        bottom_row.addWidget(color_sb)
        layout.addLayout(bottom_row)

        # connections
        linewidth_sb.valueChanged.connect(graph.update_linewidth)
        power_sb.valueChanged.connect(graph.update_power)
        color_sb.textChanged.connect(graph.update_color)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()