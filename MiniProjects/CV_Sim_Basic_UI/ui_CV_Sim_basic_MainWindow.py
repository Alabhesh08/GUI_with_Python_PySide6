# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CV_Sim_basic_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1154, 861)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 710, 1131, 91))
        font = QFont()
        font.setFamilies([u"Sitka Heading"])
        font.setBold(True)
        self.groupBox.setFont(font)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 1111, 49))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Different_Metric_label = QLabel(self.layoutWidget)
        self.Different_Metric_label.setObjectName(u"Different_Metric_label")

        self.verticalLayout_5.addWidget(self.Different_Metric_label)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 11, 1131, 691))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.parameter_label = QLabel(self.widget)
        self.parameter_label.setObjectName(u"parameter_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameter_label.sizePolicy().hasHeightForWidth())
        self.parameter_label.setSizePolicy(sizePolicy)
        self.parameter_label.setMinimumSize(QSize(100, 50))
        font1 = QFont()
        font1.setFamilies([u"Sitka Small"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.parameter_label.setFont(font1)

        self.verticalLayout.addWidget(self.parameter_label)

        self.hr_label = QLabel(self.widget)
        self.hr_label.setObjectName(u"hr_label")
        sizePolicy.setHeightForWidth(self.hr_label.sizePolicy().hasHeightForWidth())
        self.hr_label.setSizePolicy(sizePolicy)
        self.hr_label.setMinimumSize(QSize(100, 0))
        font2 = QFont()
        font2.setFamilies([u"Sitka Heading"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.hr_label.setFont(font2)

        self.verticalLayout.addWidget(self.hr_label)

        self.resistance_label = QLabel(self.widget)
        self.resistance_label.setObjectName(u"resistance_label")
        sizePolicy.setHeightForWidth(self.resistance_label.sizePolicy().hasHeightForWidth())
        self.resistance_label.setSizePolicy(sizePolicy)
        self.resistance_label.setMinimumSize(QSize(100, 0))
        self.resistance_label.setFont(font2)

        self.verticalLayout.addWidget(self.resistance_label)

        self.compliance_label = QLabel(self.widget)
        self.compliance_label.setObjectName(u"compliance_label")
        sizePolicy.setHeightForWidth(self.compliance_label.sizePolicy().hasHeightForWidth())
        self.compliance_label.setSizePolicy(sizePolicy)
        self.compliance_label.setMinimumSize(QSize(100, 0))
        self.compliance_label.setFont(font2)

        self.verticalLayout.addWidget(self.compliance_label)

        self.contractility_label = QLabel(self.widget)
        self.contractility_label.setObjectName(u"contractility_label")
        sizePolicy.setHeightForWidth(self.contractility_label.sizePolicy().hasHeightForWidth())
        self.contractility_label.setSizePolicy(sizePolicy)
        self.contractility_label.setMinimumSize(QSize(100, 0))
        self.contractility_label.setFont(font2)

        self.verticalLayout.addWidget(self.contractility_label)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.start_button = QPushButton(self.widget)
        self.start_button.setObjectName(u"start_button")
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QSize(200, 0))
        self.start_button.setMaximumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.start_button, 0, 0, 1, 1)

        self.pause_button = QPushButton(self.widget)
        self.pause_button.setObjectName(u"pause_button")
        sizePolicy.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.pause_button.setSizePolicy(sizePolicy)
        self.pause_button.setMinimumSize(QSize(200, 0))
        self.pause_button.setMaximumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.pause_button, 1, 0, 1, 1)

        self.reset_button = QPushButton(self.widget)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setMinimumSize(QSize(200, 0))
        self.reset_button.setMaximumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.reset_button, 2, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.realtime_plots_label = QLabel(self.widget)
        self.realtime_plots_label.setObjectName(u"realtime_plots_label")
        sizePolicy.setHeightForWidth(self.realtime_plots_label.sizePolicy().hasHeightForWidth())
        self.realtime_plots_label.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.realtime_plots_label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.PT_plot_widget = PlotWidget(self.widget)
        self.PT_plot_widget.setObjectName(u"PT_plot_widget")

        self.verticalLayout_2.addWidget(self.PT_plot_widget)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.FT_plot_widget = PlotWidget(self.widget)
        self.FT_plot_widget.setObjectName(u"FT_plot_widget")

        self.verticalLayout_6.addWidget(self.FT_plot_widget)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.PV_plot_widget = PlotWidget(self.widget)
        self.PV_plot_widget.setObjectName(u"PV_plot_widget")

        self.verticalLayout_7.addWidget(self.PV_plot_widget)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1154, 25))
        self.menuDashboard = QMenu(self.menubar)
        self.menuDashboard.setObjectName(u"menuDashboard")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDashboard.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Metrics Panel", None))
        self.Different_Metric_label.setText(QCoreApplication.translate("MainWindow", u"HR       |       CO       |       MAP       |       SV       |       EF       |       LV Pressure       |       Aortic Pressure    ", None))
        self.parameter_label.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.hr_label.setText(QCoreApplication.translate("MainWindow", u"HR :", None))
        self.resistance_label.setText(QCoreApplication.translate("MainWindow", u"Resistance :", None))
        self.compliance_label.setText(QCoreApplication.translate("MainWindow", u"Compliance :", None))
        self.contractility_label.setText(QCoreApplication.translate("MainWindow", u"Contractility :", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pause_button.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.realtime_plots_label.setText(QCoreApplication.translate("MainWindow", u"Real-time Plots", None))
        self.menuDashboard.setTitle(QCoreApplication.translate("MainWindow", u"Dashboard", None))
    # retranslateUi

