import os.path
import sys

import pandas as pd
from PySide6.QtWidgets import *


path_to_table = os.path.join("..", "data", "planets.csv")


class PandasTable(QTableWidget):
    def __init__(self, df):
        self.df = df
        nrows, ncols = df.shape
        super().__init__(nrows, ncols)

        self.setHorizontalHeaderLabels(self.df.columns)
        self.setVerticalHeaderLabels(self.df.index)

        for i, (label, row) in enumerate(self.df.iterrows()):
            for j, value in enumerate(row):
                self.setItem(i, j, QTableWidgetItem(str(value)))

        self.cellChanged.connect(self.on_cell_changed)

    def on_cell_changed(self, i, j):
        self.df.iloc[i, j] = float(self.item(i, j).text())
        print(self.df.head())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        df = pd.read_csv(path_to_table, index_col="planet")
        table = PandasTable(df)
        self.setCentralWidget(table)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
