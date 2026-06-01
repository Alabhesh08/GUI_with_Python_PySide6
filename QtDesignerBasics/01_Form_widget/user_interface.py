from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class UserInterface(QtCore.QObject): # An object wrapping around our ui
    def __init__(self):
        super().__init__()
        self.ui = loader.load('widget.ui', None)
        self.ui.setWindowTitle("User Data")
        self.ui.Submit_button.clicked.connect(self.do_something)

    def do_something(self):
        print(self.ui.Full_name_line_edit.text(), " is a ", self.ui.Occupation_line_edit.text())
    
    def show(self):
        self.ui.show()