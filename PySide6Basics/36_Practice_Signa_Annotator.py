# Simple signal Annotator simulation


# +------------------------------------------------+
# | Load CSV                                       |
# +------------------+-----------------------------+
# |                  |                             |
# | Signal Values    |     Parameters Panel        |
# |                  |                             |
# | 0 : 0.12         | Threshold [0.5]             |
# | 1 : 0.15         | Gain      [slider]          |
# | 2 : 0.18         | Normalize [x]               |
# |                  |                             |
# +------------------+-----------------------------+
# | Markers: 34, 89, 120                           |
# +------------------------------------------------+


import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QColor, QPalette
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
    QSlider,
    QLayout,
    QListWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(1000,700))
        self.data = []
        self.set_gain = 1

        Main_layout = QVBoxLayout()

        sub_layout = QHBoxLayout()
        self.signal = QLabel("Signal Values: ")
        self.signal.setFixedSize(QSize(500,30))
        # self.signal.setStyleSheet('background:red')

        self.signal_list = QListWidget()
        self.signal_list.setStyleSheet("QListWidget::item { height: 25px; }")
        self.signal_list.setMaximumHeight(450)
        self.signal_list.currentTextChanged.connect(self.annotate)
        

        parameters = QVBoxLayout()

        threshold = QHBoxLayout()
        threshold_label = QLabel("Threshold (upper limit):")
        # threshold_label.setStyleSheet('background:red')
        threshold_label.setMaximumSize(QSize(150,30))
        get_threshold = QDoubleSpinBox()
        get_threshold.setMaximumSize(QSize(150,30))
        get_threshold.setValue(0.85)
        get_threshold.setSingleStep(0.01)
        get_threshold.setRange(-1,1)
        get_threshold.valueChanged.connect(self.thresholdChanged)
        self.threshold_value = get_threshold.value()
        threshold.addWidget(threshold_label)
        threshold.addWidget(get_threshold)

        gain = QHBoxLayout()
        self.gain_label = QLabel("Gain : 1")
        # self.gain_label.setStyleSheet('background:red')
        self.gain_label.setMaximumSize(QSize(100,30))
        gain.addWidget(self.gain_label)
        gain_slider = QSlider(Qt.Orientation.Horizontal)
        gain_slider.setSliderPosition(1)
        gain_slider.setRange(-5,15)
        gain_slider.setValue(0)
        gain_slider.setMaximumSize(QSize(250,30))
        # gain_slider.setStyleSheet('background:red')
        gain_slider.valueChanged.connect(self.gain_value)
        gain.addWidget(gain_slider)


        parameters.addLayout(threshold)
        parameters.addLayout(gain)

        sub_layout2 = QVBoxLayout()
        sub_layout2.addWidget(self.signal)
        sub_layout2.addWidget(self.signal_list)

        sub_layout.addLayout(parameters)
        sub_layout.addLayout(sub_layout2)
        
        self.csv_filename = QLabel("")
        self.csv_filename.setFixedSize(QSize(800,30))
        csv_loader = QPushButton("Load CSV")
        csv_loader.clicked.connect(self.load_csv)

        self.markers = QLabel("Markers: ")
        self.marker_list = []

        Main_layout.setContentsMargins(10,10,10,10)

        Main_layout.addWidget(csv_loader)
        Main_layout.addWidget(self.csv_filename)
        Main_layout.addLayout(sub_layout)
        Main_layout.addWidget(self.markers)

        widget = QWidget()
        widget.setLayout(Main_layout)

        self.setCentralWidget(widget)

        

    def load_csv(self):
        self.signal_value = ""
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open CSV File",
            "",
            "CSV Files (*.csv)"
            )
        if filename :
            with open(filename, 'r') as f:
                self.data = [line.strip() for line in f]
                f.close()
                self.csv_filename.setText(filename)
                self.print_signal()
                # print(type(self.data))

    def print_signal(self):
        self.signal_list.clear()

        redata = [float(i) for i in self.data]
        print(redata, type(redata[5]))

        # Rebuild the list with only values <= threshold_value
        redata = [x for x in redata if x <= self.threshold_value]

        data1 = [str(i+1) + " : " + str(redata[i]*(self.set_gain)) for i in range(len(redata))]
        self.signal_list.addItems(data1)

    def gain_value(self,value):
        self.gain_label.setText("Gain : "+ str(value))
        self.set_gain = value
        self.print_signal()

    def annotate(self, text):
        self.marker_list.append(text.split(' : ')[1])
        self.markers.setText("Markers: \n" + ", ".join(self.marker_list))
    
    def thresholdChanged(self, value):
        self.threshold_value = value
        self.print_signal()

                

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()