import PySide6
from qt_material import apply_stylesheet

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

apply_stylesheet(app, theme="dark_teal.xml")

sys.exit(app.exec())