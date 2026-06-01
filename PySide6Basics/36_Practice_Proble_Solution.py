import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # ---------------- WINDOW ---------------- #
        self.setWindowTitle("Biomedical Signal Annotator")
        self.setMinimumSize(QSize(1000, 700))

        # ---------------- DATA ---------------- #
        self.raw_data = []
        self.filtered_data = []
        self.marker_list = []

        self.gain = 1
        self.threshold = 0.85

        # ---------------- UI ---------------- #
        self.setup_ui()

    # =========================================================
    # UI SETUP
    # =========================================================

    def setup_ui(self):

        main_layout = QVBoxLayout()

        # ---------- TOP AREA ---------- #
        self.load_button = QPushButton("Load CSV")
        self.load_button.clicked.connect(self.load_csv)

        self.filename_label = QLabel("No file loaded")

        # ---------- MIDDLE AREA ---------- #
        middle_layout = QHBoxLayout()

        self.parameters_panel = self.create_parameters_panel()
        self.signal_panel = self.create_signal_panel()

        middle_layout.addLayout(self.parameters_panel)
        middle_layout.addLayout(self.signal_panel)

        # ---------- MARKERS ---------- #
        self.markers_label = QLabel("Markers: None")

        # ---------- MAIN LAYOUT ---------- #
        main_layout.addWidget(self.load_button)
        main_layout.addWidget(self.filename_label)
        main_layout.addLayout(middle_layout)
        main_layout.addWidget(self.markers_label)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

    # =========================================================
    # PANELS
    # =========================================================

    def create_parameters_panel(self):

        parameters_layout = QVBoxLayout()

        # ---------- THRESHOLD ---------- #
        threshold_layout = QHBoxLayout()

        threshold_label = QLabel("Threshold:")

        self.threshold_spinbox = QDoubleSpinBox()
        self.threshold_spinbox.setRange(-10, 10)
        self.threshold_spinbox.setSingleStep(0.01)
        self.threshold_spinbox.setValue(self.threshold)

        self.threshold_spinbox.valueChanged.connect(
            self.update_threshold
        )

        threshold_layout.addWidget(threshold_label)
        threshold_layout.addWidget(self.threshold_spinbox)

        # ---------- GAIN ---------- #
        gain_layout = QHBoxLayout()

        self.gain_label = QLabel(f"Gain: {self.gain}")

        self.gain_slider = QSlider(Qt.Horizontal)
        self.gain_slider.setRange(1, 15)
        self.gain_slider.setValue(self.gain)

        self.gain_slider.valueChanged.connect(
            self.update_gain
        )

        gain_layout.addWidget(self.gain_label)
        gain_layout.addWidget(self.gain_slider)

        # ---------- FINAL ---------- #
        parameters_layout.addLayout(threshold_layout)
        parameters_layout.addSpacing(30)
        parameters_layout.addLayout(gain_layout)
        parameters_layout.addStretch()

        return parameters_layout

    def create_signal_panel(self):

        signal_layout = QVBoxLayout()

        self.signal_title = QLabel("Signal Values")

        self.signal_list = QListWidget()
        self.signal_list.setMaximumHeight(500)

        self.signal_list.itemDoubleClicked.connect(
            self.add_marker
        )

        signal_layout.addWidget(self.signal_title)
        signal_layout.addWidget(self.signal_list)

        return signal_layout

    # =========================================================
    # FILE LOADING
    # =========================================================

    def load_csv(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open CSV File",
            "",
            "CSV Files (*.csv)"
        )

        if not filename:
            return

        try:

            with open(filename, "r") as f:

                self.raw_data = [
                    float(line.strip())
                    for line in f
                ]

            self.filename_label.setText(filename)

            self.process_signal()
            self.update_signal_display()

        except Exception as e:

            self.filename_label.setText(
                f"Error loading file: {e}"
            )

    # =========================================================
    # SIGNAL PROCESSING
    # =========================================================

    def process_signal(self):

        # Apply threshold
        thresholded = [
            value
            for value in self.raw_data
            if value <= self.threshold
        ]

        # Apply gain
        self.filtered_data = [
            value * self.gain
            for value in thresholded
        ]

    # =========================================================
    # DISPLAY
    # =========================================================

    def update_signal_display(self):

        self.signal_list.clear()

        display_data = [
            f"{index} : {value:.4f}"
            for index, value
            in enumerate(self.filtered_data)
        ]

        self.signal_list.addItems(display_data)

    def update_markers_display(self):

        if not self.marker_list:
            self.markers_label.setText("Markers: None")
            return

        marker_text = ", ".join(
            str(marker)
            for marker in self.marker_list
        )

        self.markers_label.setText(
            f"Markers: {marker_text}"
        )

    # =========================================================
    # PARAMETER UPDATES
    # =========================================================

    def update_gain(self, value):

        self.gain = value

        self.gain_label.setText(
            f"Gain: {value}"
        )

        self.process_signal()
        self.update_signal_display()

    def update_threshold(self, value):

        self.threshold = value

        self.process_signal()
        self.update_signal_display()

    # =========================================================
    # ANNOTATION
    # =========================================================

    def add_marker(self, item):

        text = item.text()

        sample_index = text.split(" : ")[0]

        self.marker_list.append(sample_index)

        self.update_markers_display()


# =============================================================
# APPLICATION
# =============================================================

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()