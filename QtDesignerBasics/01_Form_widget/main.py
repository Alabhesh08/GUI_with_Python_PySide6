import sys
from PySide6.QtWidgets import QApplication
from user_interface import UserInterface

app = QApplication(sys.argv)

window = UserInterface()
window.show()

app.exec()