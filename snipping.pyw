import os
import sys
import tempfile
from shutil import rmtree

import cv2
import pyperclip
import pytesseract
import numpy as np
import tkinter as tk
from PIL import Image, ImageGrab
from PyQt5 import QtWidgets, QtCore, QtGui


class Snipper(QtWidgets.QWidget):
    def __init__(self, app):
        # desk = app.desktop()
        # screens = [desk.screenGeometry(ix) for ix in range(desk.screenCount())]
        # minx = min(scr.x() for scr in screens)
        # miny = min(scr.y() for scr in screens)
        # maxx = max(scr.x() + scr.width() for scr in screens)
        # maxy = max(scr.y() + scr.height() for scr in screens)

        super().__init__()
        root = tk.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.setGeometry(0, 0, width, height)
        self.setWindowTitle('')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def read_image(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return pytesseract.image_to_string(gray), gray

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        text, img = self.read_image(np.array(img))
        pyperclip.copy(text)

        cv2.imshow('Captured Image', img)
        cv2.waitKey(10000)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Snipper(app)
    sys.exit(app.exec_())