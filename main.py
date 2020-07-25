# -*- coding: utf-8 -*-
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QMessageBox

from mainwindow import Ui_MainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.flines_num.valueChanged.connect(self.ui.flines.changeNum)
        self.ui.diameter.valueChanged.connect(self.ui.flines.changeDia)
        self.ui.line_width.valueChanged.connect(self.ui.flines.changeWidth)
        self.ui.rgb_r.valueChanged.connect(self.ui.flines.changeR)
        self.ui.rgb_g.valueChanged.connect(self.ui.flines.changeG)
        self.ui.rgb_b.valueChanged.connect(self.ui.flines.changeB)
        self.ui.x_rot.valueChanged.connect(self.ui.flines.RotX)
        self.ui.y_rot.valueChanged.connect(self.ui.flines.RotY)
        self.ui.z_rot.valueChanged.connect(self.ui.flines.RotZ)
        self.ui.check_coor.stateChanged.connect(self.ui.flines.showcoor)

        self.ui.model.buttonClicked.connect(self.ui.solar.changeModel)
        self.ui.showplanet.buttonClicked.connect(self.changeShow)
        self.ui.x_slolar.valueChanged.connect(self.ui.solar.changeX)
        self.ui.y_slolar.valueChanged.connect(self.ui.solar.changeY)
        self.ui.z_slolar.valueChanged.connect(self.ui.solar.changeZ)
        self.ui.showtrack.stateChanged.connect(self.ui.solar.showTrack)
        self.ui.colortrack.stateChanged.connect(self.ui.solar.colorTrack)
        self.ui.projection.buttonClicked.connect(self.ui.solar.changeProject)
        self.ui.fovy.valueChanged.connect(self.ui.solar.changeFovy)
        self.ui.stop.clicked.connect(self.play)
        self.isplay = True
        self.ui.flag.stateChanged.connect(self.ui.solar.changeFlag)

        self.ui.about.triggered.connect(self.about)
        self.ui.description.triggered.connect(self.description)
        self.ui.open.triggered.connect(self.open)

    def changeShow(self):
        earth = self.ui.earth.isChecked()
        moon = self.ui.moon.isChecked()
        sun = self.ui.sun.isChecked()
        shui = self.ui.shui.isChecked()
        jin = self.ui.jin.isChecked()
        huo = self.ui.huo.isChecked()
        mu = self.ui.mu.isChecked()
        tu = self.ui.tu.isChecked()
        tian = self.ui.tian.isChecked()
        hai = self.ui.hai.isChecked()
        showp = (earth, moon, sun, shui, jin, huo, mu, tu, tian, hai)
        self.ui.solar.changePlanet(showp)

    def play(self):
        if self.isplay:
            self.ui.solar.play(False)
            self.ui.stop.setText('播放')
        else:
            self.ui.solar.play(True)
            self.ui.stop.setText('暂停')
        self.isplay = not self.isplay

    def about(self):
        html = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000000;">学号：2019261331</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000000;">姓名：张欣</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000000;">基于Python和Pyside2开发</span></p>
<p align="right" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000000;">--2020.06</span></p>
</body></html>
        """
        QMessageBox.about(self.ui.menubar, '关于', html)

    def description(self):
        QMessageBox.information(self.ui.menubar, '帮助', '请参考说明文档和软件左下角的提示')

    def open(self):
        QMessageBox.information(self.ui.menubar, '打开', '没有需要打开的文件')


if __name__ == "__main__":
    app = QApplication()
    app.setWindowIcon(QIcon('logo.png'))
    window = Window()
    window.show()
    app.exec_()
