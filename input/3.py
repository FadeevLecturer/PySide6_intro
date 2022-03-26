import sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MPLGraph(FigureCanvasQTAgg):
    def __init__(self):
        fig, self.ax = plt.subplots(figsize=(2, 2), layout="tight")
        self.ax.set_xticks(np.arange(0, 4 * np.pi + 0.0001, np.pi / 2))
        self.ax.set_xticklabels([
            "0",
            r"$\dfrac{\pi}{2}$",
            r"$\pi$",
            r"$\dfrac{3\pi}{2}$",
            r"$2\pi$",
            r"$\dfrac{5\pi}{2}$",
            r"$3\pi$",
            r"$\dfrac{7\pi}{2}$",
            r"$4\pi$"
        ])
        self.ax.grid()

        self.x = np.linspace(0, 4 * np.pi, 1000)
        self.magnitude = 1.
        self.phase = 0.
        self.line, = self.ax.plot(self.x, self.compute_y())
        self.ax.set_xlim([0, 2 * np.pi])
        self.ax.set_ylim([-1, 1])
        super().__init__(fig)

    def compute_y(self):
        return self.magnitude * np.sin(self.x - self.phase)

    def update_plot(self):
        self.line.set_ydata(self.compute_y())
        self.draw()

    def update_horizontal_range(self, scroll_value):
        left_boundary = scroll_value / 100. * 2 * np.pi
        self.ax.set_xlim([left_boundary, left_boundary + 2 * np.pi])
        self.draw()

    def update_magnitude(self, slider_value):
        self.magnitude = slider_value / 100.
        self.update_plot()

    def update_phase(self, dial_value):
        self.phase = dial_value / 100. * np.pi
        self.update_plot()


class RangeScrollBar(QScrollBar):
    def __init__(self):
        super().__init__(Qt.Horizontal)
        self.setMinimum(0)
        self.setMaximum(100)


class HeightSlider(QSlider):
    def __init__(self):
        super().__init__(Qt.Vertical)
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(100)


class PhaseDial(QDial):
    def __init__(self):
        super().__init__()
        self.setMinimum(0)
        self.setMaximum(100)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 400)
        widget = QWidget()
        layout = QGridLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # widgets
        graph = MPLGraph()
        range_scroll_bar = RangeScrollBar()
        magnitude_slider = HeightSlider()
        phase_dial = PhaseDial()

        # layout
        layout.addWidget(magnitude_slider, 1, 1)
        layout.addWidget(phase_dial, 2, 1)
        layout.addWidget(graph, 1, 2, 2, 2)
        layout.addWidget(range_scroll_bar, 3, 2, 1, 2)

        # connections
        range_scroll_bar.valueChanged.connect(graph.update_horizontal_range)
        magnitude_slider.valueChanged.connect(graph.update_magnitude)
        phase_dial.valueChanged.connect(graph.update_phase)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()