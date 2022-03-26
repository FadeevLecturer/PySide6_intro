import sys

from PySide6.QtGui import *
from PySide6.QtWidgets import *

bistate_to_text = {
    False: "Unchecked",
    True: "Checked"
}

tristate_to_text = {
    Qt.CheckState.Unchecked: "Unchecked",
    Qt.CheckState.PartiallyChecked: "Partially Checked",
    Qt.CheckState.Checked: "Checked"
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        main_layout = QVBoxLayout()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        # widgets
        self.common_checkbox = QCheckBox("Common checkbox")
        self.tristate_checkbox = QCheckBox("Tristate checkbox")
        self.tristate_checkbox.setTristate()
        self.label = QLabel("Unchecked and Unchecked")

        # layout
        main_layout.addWidget(self.common_checkbox)
        main_layout.addWidget(self.tristate_checkbox)
        main_layout.addWidget(self.label)

        # connections
        self.common_checkbox.stateChanged.connect(self.update_label)
        self.tristate_checkbox.stateChanged.connect(self.update_label)

    def update_label(self):
        s1 = bistate_to_text[self.common_checkbox.isChecked()]
        s2 = tristate_to_text[self.tristate_checkbox.checkState()]
        self.label.setText(f"{s1} and {s2}")


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()
