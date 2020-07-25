# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QMenu
from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor
from PySide2.QtGui import QKeySequence
from OpenGL.GL import *
from math import *
from collections import namedtuple


class FLines(QOpenGLWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.num = 3  # 顶点数
        self.dia = 100  # 直径
        self.linewidth = 2  # 线宽
        self.r = 255
        self.g = 255
        self.b = 0
        self.xRot = 0.0
        self.yRot = 0.0
        self.zRot = 0.0
        self.show_coor = True  # 是否显示模型坐标轴
        # 右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenu)
        # 快捷键
        QShortcut(QKeySequence(Qt.Key_F1), self, lambda: self.RotF('F1'))
        QShortcut(QKeySequence(Qt.Key_F2), self, lambda: self.RotF('F2'))
        QShortcut(QKeySequence(Qt.Key_F3), self, lambda: self.RotF('F3'))
        QShortcut(QKeySequence(Qt.Key_F4), self, lambda: self.RotF('F4'))

    def rightMenu(self):
        self.contextMenu = QMenu(self)
        self.DD = self.contextMenu.addMenu('顶点个数')
        self.D4 = self.DD.addAction('4')
        self.D10 = self.DD.addAction('10')
        self.D20 = self.DD.addAction('20')
        self.ZJ = self.contextMenu.addMenu('直径')
        self.ZJ50 = self.ZJ.addAction('50')
        self.ZJ150 = self.ZJ.addAction('150')
        self.ZJ200 = self.ZJ.addAction('200')
        self.YS = self.contextMenu.addMenu('颜色')
        self.YS1 = self.YS.addAction('绿色')
        self.YS2 = self.YS.addAction('黑色')
        self.YS3 = self.YS.addAction('白色')
        self.contextMenu.popup(QCursor.pos(), None)  # 菜单显示的位置

        self.D4.triggered.connect(lambda: self.changeNum(4))
        self.D10.triggered.connect(lambda: self.changeNum(10))
        self.D20.triggered.connect(lambda: self.changeNum(20))
        self.ZJ50.triggered.connect(lambda: self.changeDia(50))
        self.ZJ150.triggered.connect(lambda: self.changeDia(150))
        self.ZJ200.triggered.connect(lambda: self.changeDia(200))
        self.YS1.triggered.connect(lambda: self.changeRGB([0, 255, 0]))
        self.YS2.triggered.connect(lambda: self.changeRGB([0, 0, 0]))
        self.YS3.triggered.connect(lambda: self.changeRGB([255, 255, 255]))

    def initializeGL(self):
        glClearColor(0.3, 0.3, 0.6, 1)  # 背景色

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # 用当前背景色清屏
        glPushMatrix()
        glRotatef(self.xRot, 1.0, 0.0, 0.0)
        glRotatef(self.yRot, 0.0, 1.0, 0.0)
        glRotatef(self.zRot, 0.0, 0.0, 1.0)

        glLineWidth(self.linewidth)  # 设置线宽

        # 圆弧等分点
        theta = 2 * pi / self.num
        angle = 0
        z = 0
        Point = namedtuple('Point', ['x', 'y', 'z'])
        points_list = []
        for i in range(self.num):
            x = self.dia / 2 * cos(angle)
            y = self.dia / 2 * sin(angle)
            angle += theta
            p = Point(x, y, z)
            points_list.append(p)

        glColor3ub(self.r, self.g, self.b)  # 画笔色
        glBegin(GL_LINES)
        points_list2 = points_list[:]
        for i1 in points_list:
            points_list2.pop(0)
            for i in points_list2:
                glVertex3f(i1.x, i1.y, i1.z)
                glVertex3f(i.x, i.y, i.z)
        glEnd()

        if self.show_coor:  # 绘制模型坐标系
            glBegin(GL_LINES)
            # 以红色绘制x轴
            glColor4f(1.0, 0.0, 0.0, 1.0)  # 设置当前颜色为红色不透明
            glVertex3f(0.0, 0.0, 0.0)  # 设置x轴顶点（x轴负方向）
            glVertex3f(20, 0.0, 0.0)  # 设置x轴顶点（x轴正方向）
            # 以绿色绘制y轴
            glColor4f(0.0, 1.0, 0.0, 1.0)  # 设置当前颜色为绿色不透明
            glVertex3f(0.0, 0.0, 0.0)  # 设置y轴顶点（y轴负方向）
            glVertex3f(0.0, 20, 0.0)  # 设置y轴顶点（y轴正方向）
            # 以蓝色绘制z轴
            glColor4f(0.0, 0.0, 1.0, 1.0)  # 设置当前颜色为蓝色不透明
            glVertex3f(0.0, 0.0, 0.0)  # 设置z轴顶点（z轴负方向）
            glVertex3f(0.0, 0.0, 20)  # 设置z轴顶点（z轴正方向）
            glEnd()  # 结束绘制线段

            glPointSize(6)  # 设置点大小
            glBegin(GL_POINTS)  # 画点表示坐标轴正方向
            glColor4f(1.0, 0.0, 0.0, 1.0)
            glVertex3f(20, 0, 0)
            glColor4f(0.0, 1.0, 0.0, 1.0)
            glVertex3f(0, 20, 0)
            glColor4f(0.0, 0.0, 1.0, 1.0)
            glVertex3f(0, 0, 20)
            glEnd()

        glPopMatrix()  # 弹出矩阵

    def resizeGL(self, w: int, h: int):
        nRange = 100.0
        glViewport(0, 0, w, h)  # 设置视区和窗口等大
        glMatrixMode(GL_PROJECTION)  # 投影坐标系
        glLoadIdentity()  # 单位矩阵
        if w <= h:  # 平行投影
            glOrtho(-nRange, nRange, -nRange * h / w, nRange * h / w, -nRange, nRange)
        else:
            glOrtho(-nRange * w / h, nRange * w / h, -nRange, nRange, -nRange, nRange)
        glMatrixMode(GL_MODELVIEW)  # 模型坐标系
        glLoadIdentity()

    def changeNum(self, val):
        self.num = val
        self.update()

    def changeDia(self, val):
        self.dia = val
        self.update()

    def changeWidth(self, val):
        self.linewidth = val
        self.update()

    def changeR(self, val):
        self.r = val
        self.update()

    def changeG(self, val):
        self.g = val
        self.update()

    def changeB(self, val):
        self.b = val
        self.update()

    def changeRGB(self, RGB):
        self.r = RGB[0]
        self.g = RGB[1]
        self.b = RGB[2]
        self.update()

    def RotX(self, val):
        self.xRot = val
        self.update()

    def RotY(self, val):
        self.yRot = val
        self.update()

    def RotZ(self, val):
        self.zRot = val
        self.update()

    def RotF(self, F):
        if F == 'F1':
            self.xRot += 5
        elif F == 'F2':
            self.xRot -= 5
        elif F == 'F3':
            self.yRot += 5
        elif F == 'F4':
            self.yRot -= 5
        self.update()

    def showcoor(self, val):
        self.show_coor = val
        self.update()

    def wheelEvent(self, event):
        angle = event.angleDelta().y() / 8
        self.dia += angle
        if self.dia <= 50:
            self.dia = 50
        self.update()
