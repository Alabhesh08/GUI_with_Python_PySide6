from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from ui_CV_Sim_basic_MainWindow import Ui_MainWindow
import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import QTimer

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        
        self.setupUi(self)
        self.setWindowTitle("Basic Simulator Layout")

        # start simulating 3 graphs
        # Example x-axis
        self.x = np.linspace(0, 10, 500)

        # Create curves
        self.pt_curve = self.PT_plot_widget.plot(
            pen=pg.mkPen('#00E5FF', width=2)
        )

        self.ft_curve = self.FT_plot_widget.plot(
            pen=pg.mkPen('#22C55E', width=2)
        )

        self.pv_curve = self.PV_plot_widget.plot(
            pen=pg.mkPen('#F59E0B', width=2)
        )

        # Titles
        self.PT_plot_widget.setTitle("Pressure vs Time")
        self.FT_plot_widget.setTitle("Flow vs Time")
        self.PV_plot_widget.setTitle("Pressure-Volume Loop")

        # Grid
        for plot in [
            self.PT_plot_widget,
            self.FT_plot_widget,
            self.PV_plot_widget
        ]:
            plot.showGrid(x=True, y=True, alpha=0.3)

        self.t = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plots)
        self.timer.start(50)

    def update_plots(self):

        self.t += 0.1

        pressure = 120 + 20*np.sin(self.x + self.t)

        flow = 5*np.sin(
            2*(self.x + self.t)
        )

        volume = 120 + 40*np.sin(self.x + self.t)

        # Pressure-Time
        self.pt_curve.setData(
            self.x,
            pressure
        )

        # Flow-Time
        self.ft_curve.setData(
            self.x,
            flow
        )

        # Pressure-Volume Loop
        self.pv_curve.setData(
            volume,
            pressure
        )
        
