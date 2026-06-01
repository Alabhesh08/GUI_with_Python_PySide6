# Mouse Tracker

import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMouseTracking(True)
        self.coordinates = QLabel("Cursor Coordinates: ")
        self.setCentralWidget(self.coordinates)
        self.coordinates.setAlignment(Qt.AlignCenter)
        self.coordinates.setMouseTracking(True)



    def mouseMoveEvent(self, event):
        self.coordinates.setText(f"Cursor Coordinates: ({int(event.position().x())}, {int(event.position().y())})\n{"Top" if int(event.position().y()) < self.height()/2 else "Bottom"} {"Left Half" if int(event.position().x()) < self.width()/2 else "Right Half"}")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()