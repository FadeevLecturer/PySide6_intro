import os.path
import sys

import pandas as pd
from PySide6.QtCore import *
from PySide6.QtWidgets import *

path_to_table = os.path.join("..", "data", "planets.csv")


class PandasModel(QAbstractTableModel):
    def __init__(self, df, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.df = df

    def rowCount(self, parent=None):
        return len(self.df)

    def columnCount(self, parent=None):
        return self.df.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                r, c = index.row(), index.column()
                return str(self.df.iat[r, c])
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid():
            if role == Qt.EditRole:
                r, c = index.row(), index.column()
                self.df.iat[r, c] = float(value)
                self.dataChanged.emit(index, index, value)
                return True
        return False

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, i, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.df.columns[i]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self.df.index[i]
        return None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        df = pd.read_csv(path_to_table, index_col="planet")
        self.table_model = PandasModel(df)
        self.table_model.dataChanged.connect(self.print_data)
        table_view = QTableView()
        table_view.setModel(self.table_model)

        self.setCentralWidget(table_view)

    def print_data(self):
        print(self.table_model.df.head())


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()