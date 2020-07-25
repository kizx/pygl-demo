# -*- coding: utf-8 -*-
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
from PySide2.QtCore import Qt, QTimer
from PySide2.QtWidgets import *
from stl import mesh


def LoadTexture():
    # 加载图片
    img = Image.open('flag.png')
    width, height = img.size
    img = img.tobytes('raw', 'RGBA', 0, -1)
    # 生成纹理
    glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, 0)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)


class Solor(QOpenGLWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.view = np.array([-1, 1, -1, 1, 1.0, 20.0])
        self.perspective = True
        self.fovy = 60
        self.eye = np.array([0, 0, 150])
        self.lookat = np.array([0.0, 0.0, 0.0])
        self.lookup = np.array([0, 1, 0])
        self.sph = mesh.Mesh.from_file('ljsphere_s.stl')
        # self.DIST, self.PHI, self.THETA = self.getposture()
        self.DIST, self.PHI, self.THETA = 180, 0.5, 0.0
        self.eye[0] = self.DIST * np.cos(self.PHI) * np.sin(self.THETA) + self.lookat[0]
        self.eye[1] = self.DIST * np.sin(self.PHI) + self.lookat[1]
        self.eye[2] = self.DIST * np.cos(self.PHI) * np.cos(self.THETA) + self.lookat[2]
        self.ShowTrack = True
        self.ShowFlag = True
        self.colored = False
        self.XRot = 270
        self.YRot = 0
        self.ZRot = 0
        self.LineModel = False
        self.ShowSun = True
        self.ASun = 0
        self.ShowEarth = True
        self.AEarth = 0
        self.ShowMoon = True
        self.AMoon = 0
        self.ShowShui = True
        self.AShui = 0
        self.ShowJin = True
        self.AJin = 0
        self.ShowHuo = True
        self.AHuo = 0
        self.ShowMu = True
        self.AMu = 0
        self.ShowTu = True
        self.ATu = 0
        self.ShowTian = True
        self.ATian = 0
        self.ShowHai = True
        self.AHai = 0

    def getposture(self):
        """从笛卡尔坐标系变换到球坐标系 仅作示意"""
        x, y, z = self.eye - self.lookat
        dist = np.sqrt(np.power((self.eye - self.lookat), 2).sum())
        phi = np.arcsin(y / dist)
        theta = np.arctan(x / z)
        return dist, phi, theta

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)

        glClearColor(0, 0, 0, 1)
        LoadTexture()
        self.time = QTimer(self)
        self.time.setInterval(100)
        self.time.timeout.connect(self.refresh)
        self.time.start()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        k = w / h
        if w >= h:
            if self.perspective:
                gluPerspective(self.fovy, k, 1.0, 1000)
            else:
                glOrtho(-self.DIST * k, self.DIST * k, -self.DIST, self.DIST, -100, 1000)
        else:
            if self.perspective:
                gluPerspective(self.fovy, k, 1.0, 1000)
            else:
                glOrtho(-self.DIST, self.DIST, -self.DIST / k, self.DIST / k, -100, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.resizeGL(self.width(), self.height())  # 为了及时改变投影参数
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(self.eye[0], self.eye[1], self.eye[2],
                  self.lookat[0], self.lookat[1], self.lookat[2],
                  self.lookup[0], self.lookup[1], self.lookup[2])
        glRotate(self.XRot, 1, 0, 0)
        glRotate(self.YRot, 0, 1, 0)
        glRotate(self.ZRot, 0, 0, 1)
        # 太阳
        if self.ShowSun:
            glPushMatrix()
            glRotate(self.ASun, 0, 0, 1)
            self.sun(self.LineModel)
            glPopMatrix()
        # 地球和月亮
        glPushMatrix()
        self.draw_track(30)
        glRotate(self.AEarth, 0, 0, 1)
        glTranslatef(30, 0, 0)
        if self.ShowEarth:
            self.earth(self.LineModel)
        self.draw_track(4)
        glRotate(self.AMoon, 0, 0, 1)
        glTranslatef(4, 0, 0)
        if self.ShowMoon:
            self.moon(self.LineModel)
            if self.ShowFlag:
                # 绘制旗杆
                glBegin(GL_LINES)
                glColor4f(1, 1, 1, 1.0)
                glVertex3f(0, 0, 0)
                glVertex3f(0, 0, 50)
                glEnd()
                # 开启贴图模式
                glEnable(GL_TEXTURE_2D)
                glBindTexture(GL_TEXTURE_2D, 0)  # 选择纹理
                # 绘制国旗
                glBegin(GL_QUADS)
                glTexCoord2f(0.0, 0.0)  # 设置纹理坐标
                glVertex3f(0, 0, 30)
                glTexCoord2f(1, 0)
                glVertex3f(30, 0, 30)
                glTexCoord2f(1, 1)
                glVertex3f(30, 0, 50)
                glTexCoord2f(0, 1)
                glVertex3f(0, 0, 50)
                glEnd()
                glDisable(GL_TEXTURE_2D)  # 关闭纹理
        glPopMatrix()
        # 水星
        if self.ShowShui:
            glPushMatrix()
            self.draw_track(12)
            glRotate(self.AShui, 0, 0, 1)
            glTranslatef(12, 0, 0)
            self.shui(self.LineModel)
            glPopMatrix()
        # 金星
        if self.ShowJin:
            glPushMatrix()
            self.draw_track(20)
            glRotate(self.AJin, 0, 0, 1)
            glTranslatef(20, 0, 0)
            self.jin(self.LineModel)
            glPopMatrix()
        # 火星
        if self.ShowHuo:
            glPushMatrix()
            self.draw_track(40)
            glRotate(self.AHuo, 0, 0, 1)
            glTranslatef(40, 0, 0)
            self.huo(self.LineModel)
            glPopMatrix()
        # 木星
        if self.ShowMu:
            glPushMatrix()
            self.draw_track(55)
            glRotate(self.AMu, 0, 0, 1)
            glTranslatef(55, 0, 0)
            self.mu(self.LineModel)
            glPopMatrix()
        # 土星
        if self.ShowTu:
            glPushMatrix()
            self.draw_track(70)
            glRotate(self.ATu, 0, 0, 1)
            glTranslatef(70, 0, 0)
            self.tu(self.LineModel)
            glPopMatrix()
        # 天王星
        if self.ShowTian:
            glPushMatrix()
            self.draw_track(90)
            glRotate(self.ATian, 0, 0, 1)
            glTranslatef(90, 0, 0)
            self.tian(self.LineModel)
            glPopMatrix()
        # 海王星
        if self.ShowHai:
            glPushMatrix()
            self.draw_track(100)
            glRotate(self.AHai, 0, 0, 1)
            glTranslatef(100, 0, 0)
            self.hai(self.LineModel)
            glPopMatrix()

    def wheelEvent(self, event):
        angle = event.angleDelta().y() / 16
        self.DIST -= angle
        if self.DIST < 10:
            self.DIST = 10
        self.eye[0] = self.DIST * np.cos(self.PHI) * np.sin(self.THETA) + self.lookat[0]
        self.eye[1] = self.DIST * np.sin(self.PHI) + self.lookat[1]
        self.eye[2] = self.DIST * np.cos(self.PHI) * np.cos(self.THETA) + self.lookat[2]
        self.update()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.MouseX = event.x()
            self.MouseY = event.y()
            # print('按下')
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.setCursor(Qt.OpenHandCursor)
            x = event.x()
            y = event.y()
            dx = self.MouseX - x
            dy = y - self.MouseY
            self.MouseX, self.MouseY = x, y

            self.PHI += np.pi * dy / self.height()
            self.PHI %= 2 * np.pi
            self.THETA += np.pi * dx / self.width()
            self.THETA %= 2 * np.pi

            self.eye[0] = self.DIST * np.cos(self.PHI) * np.sin(self.THETA) + self.lookat[0]
            self.eye[1] = self.DIST * np.sin(self.PHI) + self.lookat[1]
            self.eye[2] = self.DIST * np.cos(self.PHI) * np.cos(self.THETA) + self.lookat[2]

            if np.pi / 2 < self.PHI < 3 * np.pi / 2:  # 摄像机仰角到一定角度 头朝向得反过来
                self.lookup = np.array([0, -1, 0])
            else:
                self.lookup = np.array([0, 1, 0])
            event.accept()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # print('松开')
            self.unsetCursor()

    def refresh(self):
        self.ASun += 14.6
        self.AEarth += 1
        self.AMoon += 12
        self.AShui += 4.15
        self.AJin += 1.63
        self.AHuo += 0.53
        self.AMu += 0.08
        self.ATu += 0.03
        self.ATian += 0.01
        self.AHai += 0.006
        self.update()

    def draw_sph(self, LineModel=False):
        if LineModel:
            glBegin(GL_LINES)
            for i in self.sph.points:
                glVertex3f(i[0], i[1], i[2])
                glVertex3f(i[3], i[4], i[5])
                glVertex3f(i[3], i[4], i[5])
                glVertex3f(i[6], i[7], i[8])
                glVertex3f(i[6], i[7], i[8])
                glVertex3f(i[0], i[1], i[2])
            glEnd()
        else:
            glBegin(GL_TRIANGLES)
            for i in self.sph.points:
                glVertex3f(i[0], i[1], i[2])
                glVertex3f(i[3], i[4], i[5])
                glVertex3f(i[6], i[7], i[8])
            glEnd()

    def draw_track(self, rad):
        if self.ShowTrack:
            if self.colored:
                glColor4f(np.random.rand(), np.random.rand(), np.random.rand(), 1.0)
            glBegin(GL_POINTS)
            for i in np.linspace(0, 2 * np.pi, rad * 3):
                glVertex3f(rad * np.cos(i), rad * np.sin(i), 0)
            glEnd()

    def sun(self, LineModel):
        glScale(10, 10, 10)
        glColor3ub(200, 0, 0)
        self.draw_sph(LineModel)

    def earth(self, LineModel):
        glScale(1, 1, 1)
        glColor3ub(66, 200, 225)
        self.draw_sph(LineModel)

    def moon(self, LineModel):
        glScale(0.5, 0.5, 0.5)
        glColor3ub(221, 221, 221)
        self.draw_sph(LineModel)

    def shui(self, LineModel):
        glScale(0.5, 0.5, 0.5)
        glColor3ub(189, 162, 93)
        self.draw_sph(LineModel)

    def jin(self, LineModel):
        glScale(1, 1, 1)
        glColor3ub(195, 171, 123)
        self.draw_sph(LineModel)

    def huo(self, LineModel):
        glScale(0.9, 0.9, 0.9)
        glColor3ub(196, 114, 60)
        self.draw_sph(LineModel)

    def mu(self, LineModel):
        glScale(4, 4, 4)
        glColor3ub(225, 152, 119)
        self.draw_sph(LineModel)

    def tu(self, LineModel):
        glScale(3, 3, 3)
        glColor3ub(241, 205, 102)
        self.draw_sph(LineModel)

    def tian(self, LineModel):
        glScale(2, 2, 2)
        glColor3ub(13, 240, 250)
        self.draw_sph(LineModel)

    def hai(self, LineModel):
        glScale(2, 2, 2)
        glColor3ub(69, 102, 243)
        self.draw_sph(LineModel)

    def changeModel(self, btn):
        btnname = btn.objectName()
        if btnname == 'entity':
            self.LineModel = False
        elif btnname == 'wire':
            self.LineModel = True
        self.update()

    def changePlanet(self, s):
        self.ShowEarth = s[0]
        self.ShowMoon = s[1]
        self.ShowSun = s[2]
        self.ShowShui = s[3]
        self.ShowJin = s[4]
        self.ShowHuo = s[5]
        self.ShowMu = s[6]
        self.ShowTu = s[7]
        self.ShowTian = s[8]
        self.ShowHai = s[9]
        self.update()

    def changeX(self, value):
        self.XRot = value
        self.update()

    def changeY(self, value):
        self.YRot = value
        self.update()

    def changeZ(self, value):
        self.ZRot = value
        self.update()

    def showTrack(self):
        btn = self.sender()
        self.ShowTrack = btn.isChecked()
        self.update()

    def colorTrack(self):
        btn = self.sender()
        self.colored = btn.isChecked()
        self.update()

    def changeProject(self, btn):
        btnname = btn.objectName()
        if btnname == 'perspective':
            self.perspective = True
        elif btnname == 'ortho':
            self.perspective = False
        self.update()

    def changeFovy(self, value):
        self.fovy = value
        self.update()

    def play(self, ok):
        if ok:
            self.time.start()
        else:
            self.time.stop()
        self.update()

    def changeFlag(self):
        btn = self.sender()
        self.ShowFlag = btn.isChecked()
        self.update()
