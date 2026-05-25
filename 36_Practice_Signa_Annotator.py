# Simple signal Annotator simulation

import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog,
    QDoubleSpinBox,
    QSlider
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(1100,800))

        Main_layout = QVBoxLayout()

        sub_layout = QHBoxLayout()
        self.signal = QLabel("Signal Values: ")
        sub_layout.addWidget(self.signal)

        parameters = QVBoxLayout()

        threshold = QHBoxLayout()
        threshold_label = QLabel("Threshold :")
        get_threshold = QDoubleSpinBox()
        threshold.addWidget(threshold_label)
        threshold.addWidget(get_threshold)

        gain = QHBoxLayout()
        gain_label = QLabel("Gain :")
        gain_slider = QSlider(Qt.Orientation.Horizontal)
        # gain_slider.setSliderPosition(1)
        gain_slider.setRange(-5,5)
        gain_slider.setValue(1)


        parameters.addLayout(threshold)

        sub_layout.addLayout(parameters)
        
        self.csv_filename = QLabel("")
        self.csv_filename.setFixedSize(QSize(800,30))
        csv_loader = QPushButton("Load CSV")
        csv_loader.clicked.connect(self.load_csv)

        markers = QLabel("Markers: ")

        Main_layout.setContentsMargins(10,10,10,10)

        Main_layout.addWidget(csv_loader)
        Main_layout.addWidget(self.csv_filename)
        Main_layout.addLayout(sub_layout)
        Main_layout.addWidget(markers)

        widget = QWidget()
        widget.setLayout(Main_layout)

        self.setCentralWidget(widget)

    def load_csv(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open CSV File",
            "",
            "CSV Files (*.csv)"
            )
        if filename :
            with open(filename, 'r') as f:
                data = f.readlines()
                f.close()
                self.csv_filename.setText(filename)
                signal_value = ""
                for i in range(len(data)):
                    signal_value = signal_value + str(i) + " : " + data[i]
                    self.signal.setText("Signal values:\n"+ signal_value)


                

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()