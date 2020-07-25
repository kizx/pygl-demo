# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from flines import FLines
from solor import Solor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(749, 575)
        self.open = QAction(MainWindow)
        self.open.setObjectName(u"open")
        self.about = QAction(MainWindow)
        self.about.setObjectName(u"about")
        self.description = QAction(MainWindow)
        self.description.setObjectName(u"description")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.flines_num = QSlider(self.groupBox_2)
        self.flines_num.setObjectName(u"flines_num")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.flines_num.sizePolicy().hasHeightForWidth())
        self.flines_num.setSizePolicy(sizePolicy1)
        self.flines_num.setMinimum(3)
        self.flines_num.setMaximum(20)
        self.flines_num.setPageStep(1)
        self.flines_num.setValue(3)
        self.flines_num.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.flines_num)

        self.spinBox_3 = QSpinBox(self.groupBox_2)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimum(3)
        self.spinBox_3.setMaximum(20)
        self.spinBox_3.setValue(3)

        self.horizontalLayout_4.addWidget(self.spinBox_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.diameter = QSlider(self.groupBox_2)
        self.diameter.setObjectName(u"diameter")
        self.diameter.setMinimum(10)
        self.diameter.setMaximum(200)
        self.diameter.setValue(100)
        self.diameter.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.diameter)

        self.spinBox_5 = QSpinBox(self.groupBox_2)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMinimum(10)
        self.spinBox_5.setMaximum(200)
        self.spinBox_5.setValue(100)

        self.horizontalLayout_6.addWidget(self.spinBox_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.line_width = QSlider(self.groupBox_2)
        self.line_width.setObjectName(u"line_width")
        self.line_width.setMinimum(1)
        self.line_width.setMaximum(6)
        self.line_width.setPageStep(1)
        self.line_width.setValue(2)
        self.line_width.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.line_width)

        self.spinBox_11 = QSpinBox(self.groupBox_2)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setMinimum(1)
        self.spinBox_11.setMaximum(6)
        self.spinBox_11.setValue(2)

        self.horizontalLayout_13.addWidget(self.spinBox_11)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.rgb_r = QSlider(self.groupBox)
        self.rgb_r.setObjectName(u"rgb_r")
        self.rgb_r.setMinimum(0)
        self.rgb_r.setMaximum(255)
        self.rgb_r.setValue(255)
        self.rgb_r.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.rgb_r)

        self.spinBox_6 = QSpinBox(self.groupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMinimum(0)
        self.spinBox_6.setMaximum(255)
        self.spinBox_6.setValue(255)

        self.horizontalLayout_7.addWidget(self.spinBox_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.rgb_g = QSlider(self.groupBox)
        self.rgb_g.setObjectName(u"rgb_g")
        self.rgb_g.setMinimum(0)
        self.rgb_g.setMaximum(255)
        self.rgb_g.setValue(255)
        self.rgb_g.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.rgb_g)

        self.spinBox_7 = QSpinBox(self.groupBox)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMinimum(0)
        self.spinBox_7.setMaximum(255)
        self.spinBox_7.setValue(255)

        self.horizontalLayout_8.addWidget(self.spinBox_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.rgb_b = QSlider(self.groupBox)
        self.rgb_b.setObjectName(u"rgb_b")
        self.rgb_b.setMinimum(0)
        self.rgb_b.setMaximum(255)
        self.rgb_b.setValue(0)
        self.rgb_b.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.rgb_b)

        self.spinBox_8 = QSpinBox(self.groupBox)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMinimum(0)
        self.spinBox_8.setMaximum(255)
        self.spinBox_8.setValue(0)

        self.horizontalLayout_9.addWidget(self.spinBox_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.x_rot = QSlider(self.groupBox_3)
        self.x_rot.setObjectName(u"x_rot")
        self.x_rot.setMinimum(0)
        self.x_rot.setMaximum(360)
        self.x_rot.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.x_rot)

        self.spinBox_9 = QSpinBox(self.groupBox_3)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMinimum(0)
        self.spinBox_9.setMaximum(360)

        self.horizontalLayout.addWidget(self.spinBox_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.y_rot = QSlider(self.groupBox_3)
        self.y_rot.setObjectName(u"y_rot")
        self.y_rot.setMinimum(0)
        self.y_rot.setMaximum(360)
        self.y_rot.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.y_rot)

        self.spinBox_10 = QSpinBox(self.groupBox_3)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setMinimum(0)
        self.spinBox_10.setMaximum(360)

        self.horizontalLayout_10.addWidget(self.spinBox_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.z_rot = QSlider(self.groupBox_3)
        self.z_rot.setObjectName(u"z_rot")
        self.z_rot.setMinimum(0)
        self.z_rot.setMaximum(360)
        self.z_rot.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.z_rot)

        self.spinBox_12 = QSpinBox(self.groupBox_3)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setMaximum(360)

        self.horizontalLayout_14.addWidget(self.spinBox_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.check_coor = QCheckBox(self.groupBox_3)
        self.check_coor.setObjectName(u"check_coor")
        self.check_coor.setChecked(True)

        self.verticalLayout_3.addWidget(self.check_coor)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_12.addWidget(self.groupBox_2)

        self.flines = FLines(self.tab_2)
        self.flines.setObjectName(u"flines")

        self.horizontalLayout_12.addWidget(self.flines)

        self.horizontalLayout_12.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.groupBox_5 = QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.entity = QRadioButton(self.groupBox_5)
        self.model = QButtonGroup(MainWindow)
        self.model.setObjectName(u"model")
        self.model.addButton(self.entity)
        self.entity.setObjectName(u"entity")
        self.entity.setChecked(True)

        self.horizontalLayout_2.addWidget(self.entity)

        self.wire = QRadioButton(self.groupBox_5)
        self.model.addButton(self.wire)
        self.wire.setObjectName(u"wire")

        self.horizontalLayout_2.addWidget(self.wire)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.perspective = QRadioButton(self.groupBox_5)
        self.projection = QButtonGroup(MainWindow)
        self.projection.setObjectName(u"projection")
        self.projection.addButton(self.perspective)
        self.perspective.setObjectName(u"perspective")
        self.perspective.setChecked(True)

        self.horizontalLayout_17.addWidget(self.perspective)

        self.ortho = QRadioButton(self.groupBox_5)
        self.projection.addButton(self.ortho)
        self.ortho.setObjectName(u"ortho")

        self.horizontalLayout_17.addWidget(self.ortho)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.fovy = QSlider(self.groupBox_5)
        self.fovy.setObjectName(u"fovy")
        self.fovy.setMinimum(30)
        self.fovy.setMaximum(120)
        self.fovy.setValue(60)
        self.fovy.setOrientation(Qt.Horizontal)

        self.horizontalLayout_18.addWidget(self.fovy)

        self.spinBox_13 = QSpinBox(self.groupBox_5)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setMinimum(30)
        self.spinBox_13.setMaximum(120)
        self.spinBox_13.setValue(60)

        self.horizontalLayout_18.addWidget(self.spinBox_13)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.groupBox_4 = QGroupBox(self.groupBox_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.earth = QCheckBox(self.groupBox_4)
        self.showplanet = QButtonGroup(MainWindow)
        self.showplanet.setObjectName(u"showplanet")
        self.showplanet.setExclusive(False)
        self.showplanet.addButton(self.earth)
        self.earth.setObjectName(u"earth")
        self.earth.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.earth)

        self.moon = QCheckBox(self.groupBox_4)
        self.showplanet.addButton(self.moon)
        self.moon.setObjectName(u"moon")
        self.moon.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.moon)

        self.sun = QCheckBox(self.groupBox_4)
        self.showplanet.addButton(self.sun)
        self.sun.setObjectName(u"sun")
        self.sun.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.sun)

        self.shui = QCheckBox(self.groupBox_4)
        self.showplanet.addButton(self.shui)
        self.shui.setObjectName(u"shui")
        self.shui.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.shui)

        self.jin = QCheckBox(self.groupBox_4)
        self.showplanet.addButton(self.jin)
        self.jin.setObjectName(u"jin")
        self.jin.setChecked(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.jin)

        self.huo = QCheckBox(self.groupBox_4)
        self.showplanet.addButton(self.huo)
        self.huo.setObjectName(u"huo")
        self.huo.setChecked(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.huo)

        self.mu = QCheckBox(self.groupBox_4)
        self.showplanet.addButton(self.mu)
        self.mu.setObjectName(u"mu")
        self.mu.setChecked(True)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.mu)

        self.tu = QCheckBox(self.groupBox_4)
        self.showplanet.addButton(self.tu)
        self.tu.setObjectName(u"tu")
        self.tu.setChecked(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.tu)

        self.tian = QCheckBox(self.groupBox_4)
        self.showplanet.addButton(self.tian)
        self.tian.setObjectName(u"tian")
        self.tian.setChecked(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.tian)

        self.hai = QCheckBox(self.groupBox_4)
        self.showplanet.addButton(self.hai)
        self.hai.setObjectName(u"hai")
        self.hai.setChecked(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.hai)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout_6.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.x_slolar = QSlider(self.groupBox_6)
        self.x_slolar.setObjectName(u"x_slolar")
        self.x_slolar.setMaximum(360)
        self.x_slolar.setValue(270)
        self.x_slolar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.x_slolar)

        self.spinBox = QSpinBox(self.groupBox_6)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(360)
        self.spinBox.setValue(270)

        self.horizontalLayout_3.addWidget(self.spinBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.groupBox_6)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.y_slolar = QSlider(self.groupBox_6)
        self.y_slolar.setObjectName(u"y_slolar")
        self.y_slolar.setMaximum(360)
        self.y_slolar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.y_slolar)

        self.spinBox_2 = QSpinBox(self.groupBox_6)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(360)

        self.horizontalLayout_5.addWidget(self.spinBox_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.z_slolar = QSlider(self.groupBox_6)
        self.z_slolar.setObjectName(u"z_slolar")
        self.z_slolar.setMaximum(360)
        self.z_slolar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.z_slolar)

        self.spinBox_4 = QSpinBox(self.groupBox_6)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(360)

        self.horizontalLayout_11.addWidget(self.spinBox_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)


        self.verticalLayout_6.addWidget(self.groupBox_6)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.showtrack = QCheckBox(self.groupBox_5)
        self.showtrack.setObjectName(u"showtrack")
        self.showtrack.setChecked(True)

        self.horizontalLayout_16.addWidget(self.showtrack)

        self.colortrack = QCheckBox(self.groupBox_5)
        self.colortrack.setObjectName(u"colortrack")

        self.horizontalLayout_16.addWidget(self.colortrack)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.flag = QCheckBox(self.groupBox_5)
        self.flag.setObjectName(u"flag")
        self.flag.setChecked(True)

        self.verticalLayout_6.addWidget(self.flag)

        self.stop = QPushButton(self.groupBox_5)
        self.stop.setObjectName(u"stop")

        self.verticalLayout_6.addWidget(self.stop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addWidget(self.groupBox_5)

        self.solar = Solor(self.tab_3)
        self.solar.setObjectName(u"solar")

        self.horizontalLayout_15.addWidget(self.solar)

        self.horizontalLayout_15.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 749, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.open)
        self.menu_2.addAction(self.description)
        self.menu_2.addAction(self.about)

        self.retranslateUi(MainWindow)
        self.diameter.valueChanged.connect(self.spinBox_5.setValue)
        self.spinBox_10.valueChanged.connect(self.y_rot.setValue)
        self.y_rot.valueChanged.connect(self.spinBox_10.setValue)
        self.spinBox_12.valueChanged.connect(self.z_rot.setValue)
        self.spinBox_5.valueChanged.connect(self.diameter.setValue)
        self.line_width.valueChanged.connect(self.spinBox_11.setValue)
        self.spinBox_3.valueChanged.connect(self.flines_num.setValue)
        self.rgb_b.valueChanged.connect(self.spinBox_8.setValue)
        self.rgb_r.valueChanged.connect(self.spinBox_6.setValue)
        self.spinBox_9.valueChanged.connect(self.x_rot.setValue)
        self.rgb_g.valueChanged.connect(self.spinBox_7.setValue)
        self.flines_num.valueChanged.connect(self.spinBox_3.setValue)
        self.spinBox_7.valueChanged.connect(self.rgb_g.setValue)
        self.spinBox_8.valueChanged.connect(self.rgb_b.setValue)
        self.z_rot.valueChanged.connect(self.spinBox_12.setValue)
        self.spinBox_6.valueChanged.connect(self.rgb_r.setValue)
        self.x_rot.valueChanged.connect(self.spinBox_9.setValue)
        self.spinBox_11.valueChanged.connect(self.line_width.setValue)
        self.x_slolar.valueChanged.connect(self.spinBox.setValue)
        self.spinBox.valueChanged.connect(self.x_slolar.setValue)
        self.y_slolar.valueChanged.connect(self.spinBox_2.setValue)
        self.spinBox_2.valueChanged.connect(self.y_slolar.setValue)
        self.z_slolar.valueChanged.connect(self.spinBox_4.setValue)
        self.spinBox_4.valueChanged.connect(self.z_slolar.setValue)
        self.fovy.valueChanged.connect(self.spinBox_13.setValue)
        self.spinBox_13.valueChanged.connect(self.fovy.setValue)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OpenGL", None))
        self.open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"\u8bf4\u660e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u5236\u53f0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u9876\u70b9", None))
#if QT_CONFIG(statustip)
        self.flines_num.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9876\u70b9\u4e2a\u6570", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.spinBox_3.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9876\u70b9\u4e2a\u6570", None))
#endif // QT_CONFIG(statustip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u5f84", None))
#if QT_CONFIG(statustip)
        self.diameter.setStatusTip(QCoreApplication.translate("MainWindow", u"\u591a\u8fb9\u5f62\u5916\u63a5\u5706\u76f4\u5f84", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.spinBox_5.setStatusTip(QCoreApplication.translate("MainWindow", u"\u591a\u8fb9\u5f62\u5916\u63a5\u5706\u76f4\u5f84", None))
#endif // QT_CONFIG(statustip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u5bbd", None))
#if QT_CONFIG(statustip)
        self.line_width.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236\u7ebf\u5bbd", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.spinBox_11.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236\u7ebf\u5bbd", None))
#endif // QT_CONFIG(statustip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u989c\u8272", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"R", None))
#if QT_CONFIG(statustip)
        self.rgb_r.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u989c\u8272R\u503c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.spinBox_6.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u989c\u8272R\u503c", None))
#endif // QT_CONFIG(statustip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"G", None))
#if QT_CONFIG(statustip)
        self.rgb_g.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u989c\u8272G\u503c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.spinBox_7.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u989c\u8272G\u503c", None))
#endif // QT_CONFIG(statustip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"B", None))
#if QT_CONFIG(statustip)
        self.rgb_b.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u989c\u8272B\u503c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.spinBox_8.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u989c\u8272B\u503c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.groupBox_3.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6309XYZ\u7684\u987a\u5e8f\u8fdb\u884c\u65cb\u8f6c", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"X\u8f74", None))
#if QT_CONFIG(statustip)
        self.x_rot.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7ed5X\u8f74\u65cb\u8f6c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.spinBox_9.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7ed5X\u8f74\u65cb\u8f6c", None))
#endif // QT_CONFIG(statustip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Y\u8f74", None))
#if QT_CONFIG(statustip)
        self.y_rot.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7ed5Y\u8f74\u65cb\u8f6c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.spinBox_10.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7ed5Y\u8f74\u65cb\u8f6c", None))
#endif // QT_CONFIG(statustip)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Z\u8f74", None))
#if QT_CONFIG(statustip)
        self.z_rot.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7ed5Z\u8f74\u65cb\u8f6c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.spinBox_12.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7ed5Z\u8f74\u65cb\u8f6c", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.check_coor.setStatusTip(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u663e\u793a\u6a21\u578b\u7684\u5750\u6807\u7cfb", None))
#endif // QT_CONFIG(statustip)
        self.check_coor.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u6a21\u578b\u5750\u6807\u7cfb", None))
#if QT_CONFIG(statustip)
        self.flines.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5feb\u6377\u952e\uff1a<\u6eda\u8f6e\uff1a\u63a7\u5236\u76f4\u5f84> <F1,F2,F3,F4\uff1a\u63a7\u5236XY\u8f74\u65cb\u8f6c>", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u591a\u8fb9\u5f62", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u5236\u53f0", None))
        self.entity.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u4f53\u56fe", None))
        self.wire.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u6846\u56fe", None))
        self.perspective.setText(QCoreApplication.translate("MainWindow", u"\u900f\u89c6\u6295\u5f71", None))
        self.ortho.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u884c\u6295\u5f71", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u91ce\u9525\u89d2", None))
#if QT_CONFIG(statustip)
        self.fovy.setStatusTip(QCoreApplication.translate("MainWindow", u"\u900f\u89c6\u6a21\u5f0f\u4e0b\u76f8\u673a\u5782\u76f4\u89c6\u91ce\u7684\u9525\u89d2", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.groupBox_4.setStatusTip(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u663e\u793a\u5404\u4e2a\u661f\u7403", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.earth.setText(QCoreApplication.translate("MainWindow", u"\u5730\u7403", None))
        self.moon.setText(QCoreApplication.translate("MainWindow", u"\u6708\u7403", None))
        self.sun.setText(QCoreApplication.translate("MainWindow", u"\u592a\u9633", None))
        self.shui.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u661f", None))
        self.jin.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u661f", None))
        self.huo.setText(QCoreApplication.translate("MainWindow", u"\u706b\u661f", None))
        self.mu.setText(QCoreApplication.translate("MainWindow", u"\u6728\u661f", None))
        self.tu.setText(QCoreApplication.translate("MainWindow", u"\u571f\u661f", None))
        self.tian.setText(QCoreApplication.translate("MainWindow", u"\u5929\u738b\u661f", None))
        self.hai.setText(QCoreApplication.translate("MainWindow", u"\u6d77\u738b\u661f", None))
#if QT_CONFIG(statustip)
        self.groupBox_6.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6309 XYZ\u987a\u5e8f\u65cb\u8f6c\u6a21\u578b\u5750\u6807\u7cfb", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X\u8f74", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y\u8f74", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Z\u8f74", None))
#if QT_CONFIG(statustip)
        self.showtrack.setStatusTip(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u663e\u793a\u8f68\u9053", None))
#endif // QT_CONFIG(statustip)
        self.showtrack.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8f68\u9053", None))
#if QT_CONFIG(statustip)
        self.colortrack.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8f68\u9053\u8272\u5f69\u968f\u65f6\u95f4\u53d8\u5316", None))
#endif // QT_CONFIG(statustip)
        self.colortrack.setText(QCoreApplication.translate("MainWindow", u"\u5f69\u8272\u8f68\u9053", None))
#if QT_CONFIG(statustip)
        self.flag.setStatusTip(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u663e\u793a\u56fd\u65d7", None))
#endif // QT_CONFIG(statustip)
        self.flag.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u56fd\u65d7", None))
#if QT_CONFIG(statustip)
        self.stop.setStatusTip(QCoreApplication.translate("MainWindow", u"\u64ad\u653e\u548c\u6682\u505c\u52a8\u753b", None))
#endif // QT_CONFIG(statustip)
        self.stop.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
#if QT_CONFIG(statustip)
        self.solar.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6309\u4f4f\u9f20\u6807\u5de6\u952e\u65cb\u8f6c\u89c6\u56fe\uff01\u6eda\u52a8\u6eda\u8f6e\u7f29\u653e\u89c6\u56fe\uff01", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u592a\u9633\u7cfb", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

