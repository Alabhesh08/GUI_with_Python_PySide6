## label, widget and mainwindow. increasing heirarchy. so who gets event and who doesnt is decided by ignore or accept!

import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

## All matter is about accepting and ignoring events. and both are different from recieving events.
# hierarchy: Label -> Widget -> Main Window, so when label accepts, no one else gets the event. 
# when it ignores, its parent that is widget gets the event. if it accepts main window doesnt get event.
# if it ignores, the MainWindow gets the event. 
# accepted → stop propagation
# ignored → continue propagation

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = self.label1("Click Here")
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        
        container = self.widget1()
        container.setLayout(layout)

        self.setCentralWidget(container)
        
    class label1(QLabel):
        def mousePressEvent(self, ev):
            print("Label Clicked!")
            ev.ignore()

    class widget1(QWidget):
        def mousePressEvent(self, event):
            print("Widget Clicked!")
            event.accept()

    def mousePressEvent(self, e):
        print("Main Window Clicked")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
