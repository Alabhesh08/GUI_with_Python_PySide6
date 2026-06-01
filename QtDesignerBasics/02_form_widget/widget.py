from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Form

class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('User Data')

        self.Submit_button.clicked.connect(self.do_something)
        
    def do_something(self):
        print(self.Full_name_line_edit.text() , ' is a ', self.Occupation_line_edit.text())