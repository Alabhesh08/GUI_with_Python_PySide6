import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# QApplication manages the event loop
# QWidget creates a basic empty window

app = QApplication(sys.argv)

window = QMainWindow()
window.show()

app.exec()