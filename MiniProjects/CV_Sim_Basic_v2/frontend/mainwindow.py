from PySide6.QtCore import (
    QObject,
    QThread,
    Signal,
    QTimer,
    QElapsedTimer,
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

        self.V = None
        self.p = None
        self.q = None
        self.t = None
        self.connect_signals()

        self.initialize_plots()

        self.play_timer = QTimer(self)
        self.play_timer.timeout.connect(self.update_playback)

        # ~60 FPS
        self.play_timer.setInterval(16)

        self.elapsed_timer = QElapsedTimer()

        # Playback speed multiplier
        self.playback_speed = 1.0

        # Visible window
        self.window_duration = 3.0

        # Gap at right edge
        self.right_margin = 0.20

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
            y=True,
            alpha=0.2
        )

        self.ui.lvPressurePlot.showGrid(
            x=True,
            y=True,
            alpha=0.2
        )

        self.ui.volumePlot.showGrid(
            x=True,
            y=True,
            alpha=0.2
        )

        self.ui.flowPlot.showGrid(
            x=True,
            y=True,
            alpha=0.2
        )

        # ==================================================
        # CREATE CURVES (ONLY ONCE)
        # ==================================================

        self.aorticCurve = self.ui.aorticPressurePlot.plot(
            pen='r'
        )

        self.lvCurve = self.ui.lvPressurePlot.plot(
            pen='y'
        )

        self.lvVolumeCurve = self.ui.volumePlot.plot(
            pen='g',
            name="LV"
        )

        self.aortaVolumeCurve = self.ui.volumePlot.plot(
            pen='c',
            name="Aorta"
        )

        self.veinVolumeCurve = self.ui.volumePlot.plot(
            pen='m',
            name="Veins"
        )

        self.aorticFlowCurve = self.ui.flowPlot.plot(
            pen='w'
        )

        self.mitralFlowCurve = self.ui.flowPlot.plot(
            pen='g'
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

        self.V = V
        self.p = p
        self.q = q
        self.t = t

        self.elapsed_timer.restart()

        self.aorticCurve.setData([], [])
        self.lvCurve.setData([], [])

        self.lvVolumeCurve.setData([], [])
        self.aortaVolumeCurve.setData([], [])
        self.veinVolumeCurve.setData([], [])

        self.aorticFlowCurve.setData([], [])
        self.mitralFlowCurve.setData([], [])

        self.play_timer.start()

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


        
    def update_playback(self):

        # ----------------------------------------
        # Playback time (real elapsed time)
        # ----------------------------------------

        elapsed = self.elapsed_timer.elapsed() / 1000.0

        current_time = elapsed * self.playback_speed

        dt = self.t[1] - self.t[0]

        end = min(
            int(current_time / dt),
            len(self.t)
        )

        # ----------------------------------------
        # Visible window
        # ----------------------------------------

        window_samples = int(
            self.window_duration / dt
        )

        if end <= window_samples:

            # -----------------------------
            # Window still filling
            # -----------------------------

            start = 0

            x_min = 0

            x_max = self.window_duration + self.right_margin

        else:

            # -----------------------------
            # Window full -> scroll
            # -----------------------------

            start = end - window_samples

            x_min = self.t[start]

            x_max = x_min + self.window_duration + self.right_margin

        # ----------------------------------------
        # Update curves
        # ----------------------------------------

        self.aorticCurve.setData(
            self.t[start:end],
            self.p["a"][start:end]
        )

        self.lvCurve.setData(
            self.t[start:end],
            self.p["l"][start:end]
        )

        self.lvVolumeCurve.setData(
            self.t[start:end],
            self.V["l"][start:end]
        )

        self.aortaVolumeCurve.setData(
            self.t[start:end],
            self.V["a"][start:end]
        )

        self.veinVolumeCurve.setData(
            self.t[start:end],
            self.V["v"][start:end]
        )

        self.aorticFlowCurve.setData(
            self.t[start:end],
            self.q["lo"][start:end]
        )

        self.mitralFlowCurve.setData(
            self.t[start:end],
            self.q["li"][start:end]
        )

        # ----------------------------------------
        # Scroll plots
        # ----------------------------------------

        for plot in (
            self.ui.aorticPressurePlot,
            self.ui.lvPressurePlot,
            self.ui.volumePlot,
            self.ui.flowPlot,
        ):
            plot.setXRange(
                x_min,
                x_max,
                padding=0
            )

        # ----------------------------------------
        # Finished
        # ----------------------------------------

        if end >= len(self.t):

            self.play_timer.stop()

            self.update_status(
                self.t
            )

            self.ui.btnRun.setEnabled(True)

            self.log(
                "Simulation completed."
            )

            self.ui.lblStatus.setText(
                "Simulation completed"
            )

            self.ui.lblStatusLeft.setText(
                "Ready"
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