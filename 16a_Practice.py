# Output number of characters, Even-Odd and Upper case of input text


import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget

eo = {0:"EVEN", 1:"ODD"}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.input = QLineEdit()

        self.char_count = QLabel("Length of your text is: 0")
        self.even_odd = QLabel("Character count EVEN/ODD??")
        self.u_case = QLabel("Upper Case: ")

        self.input.textChanged.connect(self.input_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.char_count)
        layout.addWidget(self.even_odd)
        layout.addWidget(self.u_case)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def input_changed(self, text):
        self.char_count.setText(f"Length of your text is: {len(text)}")
        self.even_odd.setText(f"Character count is {eo[len(text)%2]}")
        self.u_case.setText(f"Upper Case: {text.upper()}")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()