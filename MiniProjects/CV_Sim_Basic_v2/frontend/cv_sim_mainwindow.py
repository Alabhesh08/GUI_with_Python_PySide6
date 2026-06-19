from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.resize(1600, 900)
        MainWindow.setWindowTitle(
            "Cardiovascular Simulator"
        )

        self.centralwidget = QWidget()
        MainWindow.setCentralWidget(
            self.centralwidget
        )

        # ==================================================
        # MAIN LAYOUT
        # ==================================================

        self.mainLayout = QHBoxLayout(
            self.centralwidget
        )

        # ==================================================
        # LEFT PANEL
        # ==================================================

        self.leftPanel = QVBoxLayout()

        # ----------------------------------
        # Simulation Control
        # ----------------------------------

        self.gbSimulationControl = QGroupBox(
            "Simulation Control"
        )

        self.simControlLayout = QFormLayout()

        self.sbHeartRate = QSpinBox()
        self.sbHeartRate.setRange(20, 250)
        self.sbHeartRate.setValue(60)

        self.sbTimeStep = QDoubleSpinBox()
        self.sbTimeStep.setDecimals(4)
        self.sbTimeStep.setValue(0.001)

        self.simControlLayout.addRow(
            "Heart Rate (bpm)",
            self.sbHeartRate
        )

        self.simControlLayout.addRow(
            "Time Step (s)",
            self.sbTimeStep
        )

        self.gbSimulationControl.setLayout(
            self.simControlLayout
        )

        self.leftPanel.addWidget(
            self.gbSimulationControl
        )

        # ----------------------------------
        # Placeholder boxes
        # ----------------------------------

        self.gbParameters = QGroupBox(
            "Model Parameters"
        )

        self.parametersLayout = QVBoxLayout()

        self.parameterTabs = QTabWidget()

        # ==================================================
        # Resistance Tab
        # ==================================================

        self.tabResistance = QWidget()
        self.resistanceLayout = QFormLayout()

        self.sbRa = QDoubleSpinBox()
        self.sbRa.setValue(1.0)

        self.sbRp = QDoubleSpinBox()
        self.sbRp.setValue(0.08)

        self.sbRli = QDoubleSpinBox()
        self.sbRli.setValue(0.01)

        self.sbRlo = QDoubleSpinBox()
        self.sbRlo.setValue(0.01)

        self.resistanceLayout.addRow(
            "R systemic",
            self.sbRa
        )

        self.resistanceLayout.addRow(
            "R pulmonary",
            self.sbRp
        )

        self.resistanceLayout.addRow(
            "R mitral",
            self.sbRli
        )

        self.resistanceLayout.addRow(
            "R aortic",
            self.sbRlo
        )

        self.tabResistance.setLayout(
            self.resistanceLayout
        )

        # ==================================================
        # Compliance Tab
        # ==================================================

        self.tabCompliance = QWidget()
        self.complianceLayout = QFormLayout()

        self.sbCa = QDoubleSpinBox()
        self.sbCa.setValue(1.6)

        self.sbCv = QDoubleSpinBox()
        self.sbCv.setValue(100)

        self.sbCpa = QDoubleSpinBox()
        self.sbCpa.setValue(4.3)

        self.sbCpv = QDoubleSpinBox()
        self.sbCpv.setValue(8.4)

        self.complianceLayout.addRow(
            "C arterial",
            self.sbCa
        )

        self.complianceLayout.addRow(
            "C venous",
            self.sbCv
        )

        self.complianceLayout.addRow(
            "C pulmonary artery",
            self.sbCpa
        )

        self.complianceLayout.addRow(
            "C pulmonary vein",
            self.sbCpv
        )

        self.tabCompliance.setLayout(
            self.complianceLayout
        )

        # ==================================================
        # Other Tab
        # ==================================================

        self.tabOther = QWidget()

        self.otherLayout = QFormLayout()

        self.sbPitA = QDoubleSpinBox()
        self.sbPitA.setValue(-6)

        self.sbPitB = QDoubleSpinBox()
        self.sbPitB.setValue(-3)

        self.otherLayout.addRow(
            "PIT A",
            self.sbPitA
        )

        self.otherLayout.addRow(
            "PIT B",
            self.sbPitB
        )

        self.tabOther.setLayout(
            self.otherLayout
        )

        # ==================================================

        self.parameterTabs.addTab(
            self.tabResistance,
            "Resistances"
        )

        self.parameterTabs.addTab(
            self.tabCompliance,
            "Compliances"
        )

        self.parameterTabs.addTab(
            self.tabOther,
            "Others"
        )

        self.parametersLayout.addWidget(
            self.parameterTabs
        )

        self.gbParameters.setLayout(
            self.parametersLayout
        )

        self.gbViewOptions = QGroupBox(
            "View Options"
        )

        self.viewOptionsLayout = QVBoxLayout()

        self.chkAorticPressure = QCheckBox(
            "Aortic Pressure"
        )

        self.chkLVPressure = QCheckBox(
            "LV Pressure"
        )

        self.chkRVPressure = QCheckBox(
            "RV Pressure"
        )

        self.chkPulmonaryPressure = QCheckBox(
            "Pulmonary Pressure"
        )

        self.chkVenousPressure = QCheckBox(
            "Venous Pressure"
        )

        self.chkAorticPressure.setChecked(True)
        self.chkLVPressure.setChecked(True)

        self.viewOptionsLayout.addWidget(
            self.chkAorticPressure
        )

        self.viewOptionsLayout.addWidget(
            self.chkLVPressure
        )

        self.viewOptionsLayout.addWidget(
            self.chkRVPressure
        )

        self.viewOptionsLayout.addWidget(
            self.chkPulmonaryPressure
        )

        self.viewOptionsLayout.addWidget(
            self.chkVenousPressure
        )

        self.gbViewOptions.setLayout(
            self.viewOptionsLayout
        )

        self.gbInformation = QGroupBox(
            "Simulation Information"
        )

        self.infoLayout = QFormLayout()

        self.lblModelName = QLabel(
            "Closed Loop CV Model"
        )

        self.lblVersion = QLabel(
            "1.0"
        )


        self.lblStatus = QLabel(
            "Ready"
        )

        self.lblSimBaroreflex = QLabel(
            "Not Run"
        )

        self.lblSimTime = QLabel(
            "-"
        )

        self.lblSimDt = QLabel(
            "-"
        )

        self.infoLayout.addRow(
            "Model",
            self.lblModelName
        )

        self.infoLayout.addRow(
            "Version",
            self.lblVersion
        )


        self.infoLayout.addRow(
            "Status",
            self.lblStatus
        )
        
        self.infoLayout.addRow(
            "Baroreflex",
            self.lblSimBaroreflex
        )

        self.infoLayout.addRow(
            "Simulation Time",
            self.lblSimTime
        )

        self.infoLayout.addRow(
            "dt",
            self.lblSimDt
        )

        self.gbInformation.setLayout(
            self.infoLayout
        )

        self.leftPanel.addWidget(
            self.gbParameters
        )

        self.leftPanel.addWidget(
            self.gbViewOptions
        )

        self.leftPanel.addWidget(
            self.gbInformation
        )

        self.leftPanel.addStretch()

        # ==================================================
        # RIGHT PANEL
        # ==================================================

        self.rightPanel = QVBoxLayout()

        # ----------------------------------
        # TOP CONTROLS
        # ----------------------------------

        self.gbTopControls = QGroupBox()

        self.topControlsLayout = QHBoxLayout()

        self.sbSimulationTime = QSpinBox()
        self.sbSimulationTime.setRange(
            1,
            3600
        )
        self.sbSimulationTime.setValue(
            120
        )

        self.sbGlobalDT = QDoubleSpinBox()
        self.sbGlobalDT.setDecimals(
            4
        )
        self.sbGlobalDT.setValue(
            0.001
        )

        self.chkBaroreflex = QCheckBox(
            "Baroreflex"
        )

        self.btnRun = QPushButton(
            "Run"
        )

        self.btnPause = QPushButton(
            "Pause"
        )

        self.btnReset = QPushButton(
            "Reset"
        )

        self.btnSave = QPushButton(
            "Save Results"
        )

        self.topControlsLayout.addWidget(
            QLabel("Simulation Time (s)")
        )

        self.topControlsLayout.addWidget(
            self.sbSimulationTime
        )

        self.topControlsLayout.addSpacing(
            20
        )

        self.topControlsLayout.addWidget(
            QLabel("Time Step (s)")
        )

        self.topControlsLayout.addWidget(
            self.sbGlobalDT
        )

        self.topControlsLayout.addSpacing(
            20
        )

        self.topControlsLayout.addWidget(
            self.chkBaroreflex
        )

        self.topControlsLayout.addStretch()

        self.topControlsLayout.addWidget(
            self.btnRun
        )

        self.topControlsLayout.addWidget(
            self.btnPause
        )

        self.topControlsLayout.addWidget(
            self.btnReset
        )

        self.topControlsLayout.addWidget(
            self.btnSave
        )

        self.gbTopControls.setLayout(
            self.topControlsLayout
        )

        self.rightPanel.addWidget(
            self.gbTopControls
        )

        # ==================================================
        # PLOTS
        # ==================================================

        self.gbPlots = QGroupBox(
            "Plots"
        )

        self.plotGrid = QGridLayout()

        self.aorticPressurePlot = PlotWidget()
        self.lvPressurePlot = PlotWidget()
        self.volumePlot = PlotWidget()
        self.flowPlot = PlotWidget()

        self.plotGrid.addWidget(
            self.aorticPressurePlot,
            0,
            0
        )

        self.plotGrid.addWidget(
            self.lvPressurePlot,
            0,
            1
        )

        self.plotGrid.addWidget(
            self.volumePlot,
            1,
            0
        )

        self.plotGrid.addWidget(
            self.flowPlot,
            1,
            1
        )

        self.gbPlots.setLayout(
            self.plotGrid
        )

        self.rightPanel.addWidget(
            self.gbPlots,
            stretch=1
        )

        self.gbLog = QGroupBox(
            "Messages / Log"
        )

        self.logLayout = QVBoxLayout()

        self.txtLog = QTextEdit()
        self.txtLog.setReadOnly(True)

        self.btnClearLog = QPushButton(
            "Clear Log"
        )

        self.logLayout.addWidget(
            self.txtLog
        )

        self.logLayout.addWidget(
            self.btnClearLog
        )

        self.gbLog.setLayout(
            self.logLayout
        )

        self.rightPanel.addWidget(
            self.gbLog
        )

        self.statusFrame = QFrame()

        self.statusFrame.setFrameShape(
            QFrame.StyledPanel
        )

        self.statusLayout = QHBoxLayout(
            self.statusFrame
        )

        self.lblStatusLeft = QLabel(
            "Ready"
        )

        self.lblSimulationTime = QLabel(
            "Simulation Time: 120 s"
        )

        self.lblDt = QLabel(
            "dt = 0.001 s"
        )

        self.lblPoints = QLabel(
            "Points: 120001"
        )

        self.statusLayout.addWidget(
            self.lblStatusLeft
        )

        self.statusLayout.addStretch()

        self.statusLayout.addWidget(
            self.lblSimulationTime
        )

        self.statusLayout.addWidget(
            self.lblDt
        )

        self.statusLayout.addWidget(
            self.lblPoints
        )

        self.rightPanel.addWidget(
            self.statusFrame
        )
        # ==================================================
        # MAIN SPLIT
        # ==================================================

        self.mainLayout.addLayout(
            self.leftPanel,
            1
        )

        self.mainLayout.addLayout(
            self.rightPanel,
            4
        )