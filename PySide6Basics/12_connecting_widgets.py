import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout)
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("App 1")

        self.input = QLineEdit()
        self.label = QLabel()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        self.setMaximumSize(QSize(300,400))
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()