import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Submit")

        # self.setFixedSize(QSize(300,400))

        self.setMinimumSize(QSize(100,200))

        self.setMaximumSize(QSize(500,300))

        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()