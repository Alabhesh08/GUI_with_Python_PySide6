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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(272, 147)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 251, 111))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Full_name_label = QLabel(self.widget)
        self.Full_name_label.setObjectName(u"Full_name_label")

        self.horizontalLayout.addWidget(self.Full_name_label)

        self.Full_name_line_edit = QLineEdit(self.widget)
        self.Full_name_line_edit.setObjectName(u"Full_name_line_edit")

        self.horizontalLayout.addWidget(self.Full_name_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Occupation_label = QLabel(self.widget)
        self.Occupation_label.setObjectName(u"Occupation_label")

        self.horizontalLayout_2.addWidget(self.Occupation_label)

        self.Occupation_line_edit = QLineEdit(self.widget)
        self.Occupation_line_edit.setObjectName(u"Occupation_line_edit")

        self.horizontalLayout_2.addWidget(self.Occupation_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.Submit_button = QPushButton(self.widget)
        self.Submit_button.setObjectName(u"Submit_button")

        self.verticalLayout.addWidget(self.Submit_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Full_name_label.setText(QCoreApplication.translate("Form", u"Full Name: ", None))
        self.Occupation_label.setText(QCoreApplication.translate("Form", u"Occupation : ", None))
        self.Submit_button.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

