# A transparent overlay above the large label and main window at back. handle the events.

import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = self.QLabel("Label")
        self.label.setStyleSheet("background:red")
        self.widget = self.over1(self.label)

        self.widget.setGeometry(self.label.rect())

        self.setCentralWidget(self.label)
        
    class over1(QWidget):
        
        A = ''

        def mousePressEvent(self, event):
            print('over click!')
            if self.A == 'N':
                event.ignore()
            else:
                event.accept()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.widget.A = 'N'
            # print("Key Space")

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.widget.A = ''
        # print("Key Released")

    class QLabel(QLabel):
        def mousePressEvent(self, ev):
            print('label click!')
            ev.accept()

    def mousePressEvent(self, event):
        print('mainwindow click!')
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()