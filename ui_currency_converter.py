# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'currency_converter.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(319, 423)
        MainWindow.setStyleSheet(u"QComboBox { \n"
"	border: 1px solid rgb(152, 152, 157);\n"
"	border-radius: 5px;\n"
"	background: transparent;\n"
"	height: 40px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QWidget {\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.exchange_v_layout = QVBoxLayout()
        self.exchange_v_layout.setObjectName(u"exchange_v_layout")
        self.exchange_rate_label = QLabel(self.centralwidget)
        self.exchange_rate_label.setObjectName(u"exchange_rate_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exchange_rate_label.sizePolicy().hasHeightForWidth())
        self.exchange_rate_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Avenir"])
        font.setPointSize(16)
        self.exchange_rate_label.setFont(font)
        self.exchange_rate_label.setStyleSheet(u"color: rgb(152, 152, 157);")
        self.exchange_rate_label.setAlignment(Qt.AlignCenter)

        self.exchange_v_layout.addWidget(self.exchange_rate_label)

        self.exchange_rate = QLabel(self.centralwidget)
        self.exchange_rate.setObjectName(u"exchange_rate")
        sizePolicy.setHeightForWidth(self.exchange_rate.sizePolicy().hasHeightForWidth())
        self.exchange_rate.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Avenir"])
        font1.setPointSize(32)
        font1.setBold(True)
        self.exchange_rate.setFont(font1)
        self.exchange_rate.setAlignment(Qt.AlignCenter)

        self.exchange_v_layout.addWidget(self.exchange_rate)


        self.verticalLayout.addLayout(self.exchange_v_layout)

        self.amount_layout = QVBoxLayout()
        self.amount_layout.setObjectName(u"amount_layout")
        self.amount_label = QLabel(self.centralwidget)
        self.amount_label.setObjectName(u"amount_label")
        sizePolicy.setHeightForWidth(self.amount_label.sizePolicy().hasHeightForWidth())
        self.amount_label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Avenir"])
        font2.setPointSize(12)
        self.amount_label.setFont(font2)

        self.amount_layout.addWidget(self.amount_label)

        self.amount_line_edit = QLineEdit(self.centralwidget)
        self.amount_line_edit.setObjectName(u"amount_line_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.amount_line_edit.sizePolicy().hasHeightForWidth())
        self.amount_line_edit.setSizePolicy(sizePolicy1)
        self.amount_line_edit.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Avenir"])
        font3.setPointSize(20)
        font3.setBold(False)
        self.amount_line_edit.setFont(font3)
        self.amount_line_edit.setStyleSheet(u"border: 1px solid rgb(152, 152, 157);\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"background: transparent;\n"
"height:40px;")

        self.amount_layout.addWidget(self.amount_line_edit)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.amount_layout.addItem(self.verticalSpacer_4)

        self.from_to_layout = QVBoxLayout()
        self.from_to_layout.setObjectName(u"from_to_layout")
        self.from_to_label_layout = QHBoxLayout()
        self.from_to_label_layout.setObjectName(u"from_to_label_layout")
        self.from_label = QLabel(self.centralwidget)
        self.from_label.setObjectName(u"from_label")
        sizePolicy.setHeightForWidth(self.from_label.sizePolicy().hasHeightForWidth())
        self.from_label.setSizePolicy(sizePolicy)
        self.from_label.setFont(font2)

        self.from_to_label_layout.addWidget(self.from_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.from_to_label_layout.addItem(self.horizontalSpacer_2)

        self.to_label = QLabel(self.centralwidget)
        self.to_label.setObjectName(u"to_label")
        sizePolicy.setHeightForWidth(self.to_label.sizePolicy().hasHeightForWidth())
        self.to_label.setSizePolicy(sizePolicy)
        self.to_label.setFont(font2)

        self.from_to_label_layout.addWidget(self.to_label)


        self.from_to_layout.addLayout(self.from_to_label_layout)

        self.combo_box_layout = QHBoxLayout()
        self.combo_box_layout.setObjectName(u"combo_box_layout")
        self.combo_from = QComboBox(self.centralwidget)
        self.combo_from.setObjectName(u"combo_from")
        font4 = QFont()
        font4.setFamilies([u"Avenir"])
        self.combo_from.setFont(font4)
        self.combo_from.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_from.setStyleSheet(u"")
        self.combo_from.setMaxCount(50)

        self.combo_box_layout.addWidget(self.combo_from)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.combo_box_layout.addItem(self.horizontalSpacer)

        self.combo_to = QComboBox(self.centralwidget)
        self.combo_to.setObjectName(u"combo_to")
        self.combo_to.setFont(font4)
        self.combo_to.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_to.setStyleSheet(u"")
        self.combo_to.setMaxCount(50)

        self.combo_box_layout.addWidget(self.combo_to)


        self.from_to_layout.addLayout(self.combo_box_layout)


        self.amount_layout.addLayout(self.from_to_layout)


        self.verticalLayout.addLayout(self.amount_layout)

        self.convert_button = QPushButton(self.centralwidget)
        self.convert_button.setObjectName(u"convert_button")
        font5 = QFont()
        font5.setFamilies([u"Avenir"])
        font5.setPointSize(18)
        font5.setBold(True)
        self.convert_button.setFont(font5)
        self.convert_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.convert_button.setStyleSheet(u"border: none;\n"
"border-radius: 5px;\n"
"background: rgb(10, 132, 255);\n"
"color: white;\n"
"height: 35px;")

        self.verticalLayout.addWidget(self.convert_button)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.exchange_rate_label.setBuddy(self.exchange_rate_label)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.combo_from.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Currency Exchange", None))
        self.exchange_rate_label.setText(QCoreApplication.translate("MainWindow", u"Exchange Rate", None))
        self.exchange_rate.setText(QCoreApplication.translate("MainWindow", u"$27.77", None))
        self.amount_label.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.amount_line_edit.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.from_label.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.to_label.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.convert_button.setText(QCoreApplication.translate("MainWindow", u"CONVERT", None))
    # retranslateUi

