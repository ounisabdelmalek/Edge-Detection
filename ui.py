# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledQvpwUT.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QFontMetrics)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)



        
        MainWindow.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"    background-color: #f8f9fa;\n"
"    font-family: \"Poppins\", sans-serif;\n"
"    color: #333;\n"
"}\n"
"\n"
"#frame{\n"
"	padding:4;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#4CAF50;    \n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"\n"
"\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#save{\n"
"    background-color: #4CAF50;\n"
"    border-radius: 12px;\n"
"    padding: 12px;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"#run{\n"
"padding:10;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3e8e41;\n"
"}\n"
"\n"
"\n"
"QComboBox{\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 8px;\n"
    "  width: 400px;\n"
    
"    padding: 6px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"#centralwidget{\n"
"  border-radius: 15px;\n"
"\n"
"  width: 500;\n"
"  right: 25;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color:#f8f9"
                        "fa;\n"
"    font-size: 16px;\n"
"    color: #777;\n"
"    border: 2px dashed #ccc;\n"
"    border-radius: 12px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"\n"
"#widget{\n"
"margin:0;\n"
"}\n"
"\n"
"#filters{\n"
"color: black;\n"
"font-size :50;\n"
"padding-left: 5 dp;\n"
"}\n"
"\n"
"#filters:hover{\n"
"color:red;\n"
"}\n"
"#filters::tab{\n"
"color:blue;\n"
"}\n"
"\n"
"\n"
"\n"
"#image:hover{\n"
"color: blue;\n"
"font-size: 20px;\n"
"font-size: 30px;\n"
"}\n"
"#save:hover {\n"
"    background-color: #43a047;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image = ClickableLable(self.centralwidget)
        self.image.setObjectName(u"image")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        
        self.image.setSizePolicy(sizePolicy)
        self.image.setScaledContents(False)
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.image)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.filters = QComboBox(self.frame)
        self.filters.addItem("")
        self.filters.addItem("")
        self.filters.addItem("")
        self.filters.addItem("")
        self.filters.addItem("")
        self.filters.addItem("")
        self.filters.setObjectName(u"filters")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.filters.sizePolicy().hasWidthForHeight())
        self.filters.setSizePolicy(sizePolicy3)
        self.filters.setMaximumSize(QSize(95, 16777215))
        self.filters.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)



        self.verticalLayout.addWidget(self.filters, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.run = QPushButton(self.frame)
        self.run.setObjectName(u"run")
        self.run.setMaximumSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.run, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.filtered_image = QLabel(self.widget_2)
        self.filtered_image.setObjectName(u"filtered_image")
        sizePolicy.setHeightForWidth(self.filtered_image.sizePolicy().hasHeightForWidth())
        self.filtered_image.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.filtered_image)

        self.save = QPushButton(self.widget_2)
        self.save.setObjectName(u"save")

        self.verticalLayout_2.addWidget(self.save)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"Click to add an image", None))
        self.filters.setPlaceholderText("")
        self.run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.filtered_image.setText("")
        self.save.setText(QCoreApplication.translate("MainWindow", u"Save", None))



class ClickableLable(QLabel):
    click =Signal()
    def mousePressEvent(self, ev):
        self.click.emit()
        return super().mousePressEvent(ev)
