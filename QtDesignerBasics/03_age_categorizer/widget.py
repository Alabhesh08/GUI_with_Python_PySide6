from PySide6 import QtCore, QtWidgets
from ui_widget import Ui_age_classifier

class Widget(QtWidgets.QWidget , Ui_age_classifier):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("Age Classifier")

        self.submit_button.clicked.connect(self.classify)

    def classify(self):
        age = self.age_spinbox.value()
        if age < 18:
            print(self.name_line_edit.text(), "is a Kid.")
        elif age < 40:
            print(self.name_line_edit.text(),"is a Young Man.")
        elif age < 70:
            print(self.name_line_edit.text(), "is a Old Man.")
        else:
            print(self.name_line_edit.text(),"is a Senior Citizen.")