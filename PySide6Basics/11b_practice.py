# Toggle Window

import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

a = {True: "ON" , False: "OFF"}

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mode")
        self.button = QPushButton("Press button")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.toggle)

        self.setCentralWidget(self.button)
    def toggle(self, checked):
        self.setWindowTitle(f"Mode: {a[checked]}")

app = QApplication(sys.argv)

window = Mainwindow()
window.show()

app.exec()