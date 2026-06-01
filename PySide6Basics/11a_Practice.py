# Click Counter

import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Click Counter")
        self.count = 0

        self.button = QPushButton("Click me.")
        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.setWindowTitle("Counting Clicks")
        self.count = self.count + 1

        self.button.setText(f"Clicked {self.count} times {'!'*self.count}")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()