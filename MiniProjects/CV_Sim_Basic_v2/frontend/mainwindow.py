from PySide6.QtCore import (
    QObject,
    QThread,
    Signal,
)

from PySide6.QtWidgets import (
    QMainWindow,
)
from cv_sim_mainwindow import Ui_MainWindow
from backend.cardiovascular_simulator import CardiovascularSimulator

class SimulationWorker(QObject):

    finished = Signal(
        object,
        object,
        object,
        object,
    )

    log = Signal(str)

    def __init__(
        self,
        simulator,
    ):
        super().__init__()

        self.simulator = simulator

    def run(self):

        self.log.emit(
            "Simulation started..."
        )

        V, p, q, t = (
            self.simulator.run()
        )

        self.finished.emit(
            V,
            p,
            q,
            t,
        )


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.simulator = None
        self.thread = None
        self.worker = None

        self.connect_signals()

        self.initialize_plots()

    # ==================================================
    # SIGNALS
    # ==================================================

    def connect_signals(self):

        self.ui.btnRun.clicked.connect(
            self.run_simulation
        )

        self.ui.btnReset.clicked.connect(
            self.reset_simulation
        )

        self.ui.btnClearLog.clicked.connect(
            self.ui.txtLog.clear
        )

    # ==================================================
    # PLOTS
    # ==================================================

    def initialize_plots(self):

        self.ui.aorticPressurePlot.setTitle(
            "Aortic Pressure"
        )

        self.ui.lvPressurePlot.setTitle(
            "LV Pressure"
        )

        self.ui.volumePlot.setTitle(
            "Volumes"
        )

        self.ui.flowPlot.setTitle(
            "Flows"
        )

        self.ui.aorticPressurePlot.showGrid(
            x=True,
            y=True
        )

        self.ui.lvPressurePlot.showGrid(
            x=True,
            y=True
        )

        self.ui.volumePlot.showGrid(
            x=True,
            y=True
        )

        self.ui.flowPlot.showGrid(
            x=True,
            y=True
        )

    # ==================================================
    # LOGGING
    # ==================================================

    def log(self, text):

        self.ui.txtLog.append(text)

    # ==================================================
    # RUN
    # ==================================================

    def run_simulation(self):

        self.ui.btnRun.setEnabled(
            False
        )

        self.ui.lblStatus.setText(
            "Running simulation..."
        )

        self.ui.lblStatusLeft.setText(
            "Running..."
        )
    
        self.simulator = (
            CardiovascularSimulator(
                use_baroreflex=
                self.ui.chkBaroreflex.isChecked(),

                simulation_time=
                self.ui.sbSimulationTime.value(),

                dt=
                self.ui.sbGlobalDT.value(),
            )
        )

        self.thread = QThread()

        self.worker = (
            SimulationWorker(
                self.simulator
            )
        )

        self.worker.moveToThread(
            self.thread
        )

        self.thread.started.connect(
            self.worker.run
        )

        self.worker.finished.connect(
            self.simulation_finished
        )

        self.worker.log.connect(
            self.log
        )

        self.worker.finished.connect(
            self.thread.quit
        )

        self.worker.finished.connect(
            self.worker.deleteLater
        )

        self.thread.finished.connect(
            self.thread.deleteLater
        )

        self.thread.start()

    def simulation_finished(
        self,
        V,
        p,
        q,
        t,
    ):

        self.update_plots(
            V,
            p,
            q,
            t,
        )

        self.update_status(
            t
        )

        self.ui.lblSimBaroreflex.setText(
            "Enabled"
            if self.ui.chkBaroreflex.isChecked()
            else "Disabled"
        )

        self.ui.lblSimTime.setText(
            str(
                self.ui.sbSimulationTime.value()
            ) + " s"
        )

        self.ui.lblSimDt.setText(
            str(
                self.ui.sbGlobalDT.value()
            )
        )

        self.log(
            "Simulation completed."
        )

        self.ui.lblStatus.setText(
            "Simulation completed"
        )

        self.ui.lblStatusLeft.setText(
            "Ready"
        )

        self.ui.btnRun.setEnabled(
            True
        )
    # ==================================================
    # PLOTS UPDATE
    # ==================================================

    def update_plots(
        self,
        V,
        p,
        q,
        t
    ):

        self.ui.aorticPressurePlot.clear()
        self.ui.lvPressurePlot.clear()
        self.ui.volumePlot.clear()
        self.ui.flowPlot.clear()

        # --------------------------------------
        # Aortic Pressure
        # --------------------------------------

        self.ui.aorticPressurePlot.plot(
            t,
            p["a"],
            name="p.a"
        )

        # --------------------------------------
        # LV Pressure
        # --------------------------------------

        self.ui.lvPressurePlot.plot(
            t,
            p["l"],
            name="p.l"
        )

        # --------------------------------------
        # Volumes
        # --------------------------------------

        self.ui.volumePlot.plot(
            t,
            V["l"],
            name="LV"
        )

        self.ui.volumePlot.plot(
            t,
            V["a"],
            name="Aorta"
        )

        self.ui.volumePlot.plot(
            t,
            V["v"],
            name="Veins"
        )

        # --------------------------------------
        # Flows
        # --------------------------------------

        self.ui.flowPlot.plot(
            t,
            q["lo"],
            name="Aortic Valve"
        )

        self.ui.flowPlot.plot(
            t,
            q["li"],
            name="Mitral Valve"
        )

    # ==================================================
    # STATUS
    # ==================================================

    def update_status(
        self,
        t
    ):

        self.ui.lblStatus.setText(
            "Completed"
        )

        self.ui.lblStatusLeft.setText(
            "Ready"
        )

        self.ui.lblSimulationTime.setText(
            f"Simulation Time: {t[-1]:.0f} s"
        )

        self.ui.lblPoints.setText(
            f"Points: {len(t)}"
        )

    # ==================================================
    # RESET
    # ==================================================

    def reset_simulation(self):

        self.ui.aorticPressurePlot.clear()
        self.ui.lvPressurePlot.clear()
        self.ui.volumePlot.clear()
        self.ui.flowPlot.clear()

        self.ui.txtLog.clear()

        self.ui.lblStatus.setText(
            "Ready"
        )

        self.log(
            "Simulation reset."
        )