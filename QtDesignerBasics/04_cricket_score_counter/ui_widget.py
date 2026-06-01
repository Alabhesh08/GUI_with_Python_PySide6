# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_cricket_run_counter(object):
    def setupUi(self, cricket_run_counter):
        if not cricket_run_counter.objectName():
            cricket_run_counter.setObjectName(u"cricket_run_counter")
        cricket_run_counter.resize(323, 511)
        self.widget = QWidget(cricket_run_counter)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 304, 481))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.runs_label = QLabel(self.widget)
        self.runs_label.setObjectName(u"runs_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runs_label.sizePolicy().hasHeightForWidth())
        self.runs_label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.runs_label)

        self.overs_label = QLabel(self.widget)
        self.overs_label.setObjectName(u"overs_label")
        sizePolicy.setHeightForWidth(self.overs_label.sizePolicy().hasHeightForWidth())
        self.overs_label.setSizePolicy(sizePolicy)
        self.overs_label.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.overs_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.crr_label = QLabel(self.widget)
        self.crr_label.setObjectName(u"crr_label")
        sizePolicy.setHeightForWidth(self.crr_label.sizePolicy().hasHeightForWidth())
        self.crr_label.setSizePolicy(sizePolicy)
        self.crr_label.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.crr_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.run1_button = QPushButton(self.widget)
        self.run1_button.setObjectName(u"run1_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.run1_button.sizePolicy().hasHeightForWidth())
        self.run1_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.run1_button)

        self.run4_button = QPushButton(self.widget)
        self.run4_button.setObjectName(u"run4_button")
        sizePolicy1.setHeightForWidth(self.run4_button.sizePolicy().hasHeightForWidth())
        self.run4_button.setSizePolicy(sizePolicy1)
        self.run4_button.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.run4_button)

        self.run6_button = QPushButton(self.widget)
        self.run6_button.setObjectName(u"run6_button")
        sizePolicy1.setHeightForWidth(self.run6_button.sizePolicy().hasHeightForWidth())
        self.run6_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.run6_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.wicket_button = QPushButton(self.widget)
        self.wicket_button.setObjectName(u"wicket_button")
        sizePolicy1.setHeightForWidth(self.wicket_button.sizePolicy().hasHeightForWidth())
        self.wicket_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.wicket_button)

        self.ball_button = QPushButton(self.widget)
        self.ball_button.setObjectName(u"ball_button")
        sizePolicy1.setHeightForWidth(self.ball_button.sizePolicy().hasHeightForWidth())
        self.ball_button.setSizePolicy(sizePolicy1)
        self.ball_button.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_3.addWidget(self.ball_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.reset_button = QPushButton(self.widget)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy2)
        self.reset_button.setMinimumSize(QSize(300, 40))

        self.verticalLayout_3.addWidget(self.reset_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(cricket_run_counter)

        QMetaObject.connectSlotsByName(cricket_run_counter)
    # setupUi

    def retranslateUi(self, cricket_run_counter):
        cricket_run_counter.setWindowTitle(QCoreApplication.translate("cricket_run_counter", u"Form", None))
        self.runs_label.setText(QCoreApplication.translate("cricket_run_counter", u"Runs : 0", None))
        self.overs_label.setText(QCoreApplication.translate("cricket_run_counter", u"Overs : 0", None))
        self.crr_label.setText(QCoreApplication.translate("cricket_run_counter", u"Current Run Rate (CRR) : 0.0", None))
        self.run1_button.setText(QCoreApplication.translate("cricket_run_counter", u"1 Run", None))
        self.run4_button.setText(QCoreApplication.translate("cricket_run_counter", u"4 Runs", None))
        self.run6_button.setText(QCoreApplication.translate("cricket_run_counter", u"6 Runs", None))
        self.wicket_button.setText(QCoreApplication.translate("cricket_run_counter", u"Wicket!", None))
        self.ball_button.setText(QCoreApplication.translate("cricket_run_counter", u"Ball", None))
        self.reset_button.setText(QCoreApplication.translate("cricket_run_counter", u"Reset", None))
    # retranslateUi

