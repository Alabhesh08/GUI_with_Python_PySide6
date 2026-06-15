import sys

from PySide6.QtCore import Qt
from qt_material import apply_stylesheet
from PySide6.QtWidgets import QApplication
from CV_Sim_basic_MainWindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

apply_stylesheet(app, theme="dark_medical.xml")
app.exec()