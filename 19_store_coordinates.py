# A program to store mouse click coordinates and clear them.

import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Store Coordinates")
        self.label = QLabel("No Points Stored yet!")
        
        self.coord = []

    def mousePressEvent(self, event):
        self.coord.append( str(event.pos()).removeprefix("PySide6.QtCore.QPoint"))
        print(int(str(event.pos()).removeprefix("PySide6.QtCore.QPoint")))
        print(self.coord)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
