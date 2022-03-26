import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from PySide6.QtWidgets import *


class MPLGraph(FigureCanvasQTAgg):
    def __init__(self):
        self.fig = plt.figure(figsize=(2, 2), layout="tight")
        self.ax = None
        super().__init__(self.fig)
        self.style = "default"
        self.title = ""
        self.noise_scale = 0.1
        self.plot()

    def plot(self):
        with plt.style.context(self.style):
            if self.ax:
                self.fig.delaxes(self.ax)
            self.ax = self.fig.add_subplot(111)
            x = np.linspace(0, 1)
            noise = np.random.normal(0, self.noise_scale, size=(len(x),))
            y = x + noise
            self.ax.plot(x, y)
            self.ax.set_title(self.title)
            self.ax.set_xlabel("t")
            self.ax.set_ylabel("signal")
            self.draw()

    def set_style(self, style):
        self.style = style
        self.plot()

    def set_title(self, title):
        self.title = title
        self.plot()

    def set_noise_scale(self, scale):
        self.noise_scale = scale
        self.plot()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 400)
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # widgets
        self.graph = MPLGraph()
        set_title_button = QPushButton("Set title")
        set_style_button = QPushButton("Choose style")
        set_noise_scale_button = QPushButton("Set noice scale")

        # layout
        layout.addWidget(self.graph)

        bottom_row = QHBoxLayout()
        bottom_row.addWidget(set_title_button)
        bottom_row.addWidget(set_style_button)
        bottom_row.addWidget(set_noise_scale_button)
        layout.addLayout(bottom_row)

        # connections
        set_title_button.clicked.connect(self.on_set_title_button_click)
        set_style_button.clicked.connect(self.on_set_style_button_clicked)
        set_noise_scale_button.clicked.connect(
            self.on_set_noise_scale_button_click
        )

    def on_set_title_button_click(self):
        title, ok = QInputDialog.getText(
            self,
            "Choose title",
            "Choose the title for the figure",
        )
        if ok:
            self.graph.set_title(title)

    def on_set_style_button_clicked(self):
        style_list = ['default'] + plt.style.available
        style, ok = QInputDialog.getItem(
            self,
            "Choose style",
            "Pick a style",
            style_list
        )
        self.graph.set_style(style)

    def on_set_noise_scale_button_click(self):
        scale, ok = QInputDialog.getDouble(
            self,
            "Choose noise scale",
            "Type in standard deviation of noise to be applied",
            0.1,
            0,
            0.2,
            decimals=2,
            step=0.01
        )
        if ok:
            self.graph.set_noise_scale(scale)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()