# A program to store mouse click coordinates and clear them.

import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QMenu
from PySide6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.toggle_flag = True

        self.setWindowTitle(f"Store Coordinates: {str(self.toggle_flag)}")

        self.label = QLabel("No Points Stored yet!")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.coord = []
        self.setCentralWidget(self.label)

        self.dlt_pt = QAction("Delete Last Point", self)
        self.dlt_pt.triggered.connect(self.dlt_last_pt)

        self.clr = QAction("Clear All", self)
        self.clr.triggered.connect(self.mouseDoubleClickEvent)

        self.track = QAction("Toggle Tracking", self)
        self.track.triggered.connect(self.toggle_tracking)

    def toggle_tracking(self):
        self.toggle_flag = not self.toggle_flag
        self.setWindowTitle(f"Store Coordinates: {str(self.toggle_flag)}")

    def dlt_last_pt(self):
        if self.toggle_flag :
            self.coord.pop()
            Coordinates = "\n".join(str(row) for row in self.coord)
            self.label.setText(Coordinates)
        
    def mousePressEvent(self, event): 
        if self.toggle_flag & (event.button() == Qt.MouseButton.LeftButton):
            self.coord.append(event.position().toTuple())
            # print(self.coord)
            Coordinates = "\n".join(str(row) for row in self.coord)
            self.label.setText(Coordinates)
    
    def mouseDoubleClickEvent(self, event):
        if self.toggle_flag:
            self.coord = []
            # print('empty list')
            self.label.setText("Points Deleted")
    
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(self.dlt_pt)
        context.addAction(self.clr)
        context.addAction(self.track)
        context.exec(e.globalPos())

    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
