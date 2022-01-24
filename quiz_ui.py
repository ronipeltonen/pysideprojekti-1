# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quiz.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button3 = QPushButton(self.centralwidget)
        self.button3.setObjectName(u"button3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy1)
        self.button3.setFont(font)

        self.gridLayout.addWidget(self.button3, 2, 0, 1, 1)

        self.button4 = QPushButton(self.centralwidget)
        self.button4.setObjectName(u"button4")
        sizePolicy1.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy1)
        self.button4.setFont(font)

        self.gridLayout.addWidget(self.button4, 2, 1, 1, 1)

        self.button1 = QPushButton(self.centralwidget)
        self.button1.setObjectName(u"button1")
        sizePolicy1.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy1)
        self.button1.setFont(font)

        self.gridLayout.addWidget(self.button1, 1, 0, 1, 1)

        self.button2 = QPushButton(self.centralwidget)
        self.button2.setObjectName(u"button2")
        sizePolicy1.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy1)
        self.button2.setFont(font)

        self.gridLayout.addWidget(self.button2, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kysymys", None))
        self.button3.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.button4.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"B", None))
    # retranslateUi

