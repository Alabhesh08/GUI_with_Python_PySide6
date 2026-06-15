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
        MainWindow.resize(1153, 1095)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 920, 1131, 91))
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

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 11, 1131, 895))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.realtime_plots_label = QLabel(self.layoutWidget1)
        self.realtime_plots_label.setObjectName(u"realtime_plots_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realtime_plots_label.sizePolicy().hasHeightForWidth())
        self.realtime_plots_label.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.realtime_plots_label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.PT_plot_widget = PlotWidget(self.layoutWidget1)
        self.PT_plot_widget.setObjectName(u"PT_plot_widget")

        self.verticalLayout_2.addWidget(self.PT_plot_widget)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.FT_plot_widget = PlotWidget(self.layoutWidget1)
        self.FT_plot_widget.setObjectName(u"FT_plot_widget")

        self.verticalLayout_6.addWidget(self.FT_plot_widget)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.PV_plot_widget = PlotWidget(self.layoutWidget1)
        self.PV_plot_widget.setObjectName(u"PV_plot_widget")

        self.verticalLayout_7.addWidget(self.PV_plot_widget)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.groupBox_5 = QGroupBox(self.layoutWidget1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 600))
        self.groupBox_5.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.groupBox_5.setFont(font1)
        self.groupBox_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBox_5.setStyleSheet(u"")
        self.groupBox_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget2 = QWidget(self.groupBox_5)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(40, 80, 121, 431))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.layoutWidget2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(50, 50))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.groupBox_2.setStyleSheet(u"")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 101, 91))
        font3 = QFont()
        font3.setFamilies([u"Adobe Fan Heiti Std"])
        font3.setPointSize(36)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.layoutWidget2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(100, 100))
        self.groupBox_4.setFont(font2)
        self.groupBox_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 30, 101, 91))
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.layoutWidget2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(100, 100))
        self.groupBox_3.setFont(font2)
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 101, 91))
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.groupBox_5)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.reset_button = QPushButton(self.layoutWidget1)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setMinimumSize(QSize(200, 0))
        self.reset_button.setMaximumSize(QSize(150, 40))
        font4 = QFont()
        font4.setFamilies([u"Sitka Heading"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.reset_button.setFont(font4)
        self.reset_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.reset_button, 2, 0, 1, 1)

        self.pause_button = QPushButton(self.layoutWidget1)
        self.pause_button.setObjectName(u"pause_button")
        sizePolicy.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.pause_button.setSizePolicy(sizePolicy)
        self.pause_button.setMinimumSize(QSize(200, 0))
        self.pause_button.setMaximumSize(QSize(150, 40))
        self.pause_button.setFont(font4)
        self.pause_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pause_button, 1, 0, 1, 1)

        self.start_button = QPushButton(self.layoutWidget1)
        self.start_button.setObjectName(u"start_button")
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QSize(200, 0))
        self.start_button.setMaximumSize(QSize(150, 40))
        self.start_button.setFont(font4)
        self.start_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.start_button, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1153, 25))
        self.menuDashboard = QMenu(self.menubar)
        self.menuDashboard.setObjectName(u"menuDashboard")
        self.menuInterventions = QMenu(self.menubar)
        self.menuInterventions.setObjectName(u"menuInterventions")
        self.menuInstructor = QMenu(self.menubar)
        self.menuInstructor.setObjectName(u"menuInstructor")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDashboard.menuAction())
        self.menubar.addAction(self.menuInterventions.menuAction())
        self.menubar.addAction(self.menuInstructor.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Metrics Panel", None))
        self.Different_Metric_label.setText(QCoreApplication.translate("MainWindow", u"HR       |       CO       |       MAP       |       SV       |       EF       |       LV Pressure       |       Aortic Pressure    ", None))
        self.realtime_plots_label.setText(QCoreApplication.translate("MainWindow", u"Real-time Plots", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"SVV", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"SV", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"CO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pause_button.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menuDashboard.setTitle(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.menuInterventions.setTitle(QCoreApplication.translate("MainWindow", u"Interventions", None))
        self.menuInstructor.setTitle(QCoreApplication.translate("MainWindow", u"Instructor", None))
    # retranslateUi

