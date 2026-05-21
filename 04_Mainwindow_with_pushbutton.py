import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to custommize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        #Set the central widget of the window.
        self.setCentralWidget(button)
        self.centralWidget.setStyleSheet("QLineEdit { background: red }")
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


