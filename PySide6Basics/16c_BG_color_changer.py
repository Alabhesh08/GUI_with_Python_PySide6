import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Set color from context menu")
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def contextMenuEvent(self, e):
        context = QMenu(self)

        red = QAction("Red BG", self)
        blue = QAction("Blue BG", self)
        green = QAction("Green BG", self)

        context.addAction(red)
        context.addAction(blue)
        context.addAction(green)

        red.triggered.connect(self.make_red)
        green.triggered.connect(self.make_green)
        blue.triggered.connect(self.make_blue)

        context.exec(e.globalPos())

    def make_red(self):
        self.label.setText("Red")
        self.label.setStyleSheet("background: red")
        
    def make_green(self):
        self.label.setText("Green")
        self.label.setStyleSheet("background: green")
        
    def make_blue(self):
        self.label.setText("Blue")
        self.label.setStyleSheet("background: blue")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()