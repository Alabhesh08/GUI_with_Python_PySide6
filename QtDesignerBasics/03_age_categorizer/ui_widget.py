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
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_age_classifier(object):
    def setupUi(self, age_classifier):
        if not age_classifier.objectName():
            age_classifier.setObjectName(u"age_classifier")
        age_classifier.resize(288, 160)
        self.widget = QWidget(age_classifier)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 16, 261, 131))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_label = QLabel(self.widget)
        self.name_label.setObjectName(u"name_label")

        self.horizontalLayout.addWidget(self.name_label)

        self.name_line_edit = QLineEdit(self.widget)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.horizontalLayout.addWidget(self.name_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.age_label = QLabel(self.widget)
        self.age_label.setObjectName(u"age_label")

        self.horizontalLayout_2.addWidget(self.age_label)

        self.age_spinbox = QSpinBox(self.widget)
        self.age_spinbox.setObjectName(u"age_spinbox")

        self.horizontalLayout_2.addWidget(self.age_spinbox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.submit_button = QPushButton(self.widget)
        self.submit_button.setObjectName(u"submit_button")

        self.verticalLayout.addWidget(self.submit_button)


        self.retranslateUi(age_classifier)

        QMetaObject.connectSlotsByName(age_classifier)
    # setupUi

    def retranslateUi(self, age_classifier):
        age_classifier.setWindowTitle(QCoreApplication.translate("age_classifier", u"Form", None))
        self.name_label.setText(QCoreApplication.translate("age_classifier", u"Name : ", None))
        self.age_label.setText(QCoreApplication.translate("age_classifier", u"Age : ", None))
        self.submit_button.setText(QCoreApplication.translate("age_classifier", u"Submit", None))
    # retranslateUi

