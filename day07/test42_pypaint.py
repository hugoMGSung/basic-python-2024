# file: text42_pypaint.py
# desc: 그림판 만들기
# date: 2024-02-01

import sys
from PyQt5 import uic # QtDesigner 호출시 필요
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self): # 화면초기화
        # uic.loadUi('./day07/pyPaint.ui', self)
        uic.loadUi('C:/Sources/basic-python-2024/day07/pyPaint.ui', self) # 실행파일 생성시는 절대경로 사용
        # self.setWindowIcon(QIcon('./images/iot.png'))    
        self.setWindowIcon(QIcon('C:/Sources/basic-python-2024/day07/iot.png')) # 실행파일 생성시는 절대경로 사용
        self.setWindowTitle('Py그림판')
        # 캔버스 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('white')) 
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background:black;')
        self.btn_red.setStyleSheet('background:red;')
        self.btn_blue.setStyleSheet('background:blue;')

        self.show()
        self.setCenter()

    def initSignal(self): # 동작초기화
        self.btn_black.clicked.connect(self.buttonClicked)
        self.btn_red.clicked.connect(self.buttonClicked)
        self.btn_blue.clicked.connect(self.buttonClicked)
        self.btn_clear.clicked.connect(self.buttonClicked)
        # 2024-02-06 이미지로드 및 저장버튼 추가
        self.btn_load.clicked.connect(self.btnLoadClicked)
        self.btn_save.clicked.connect(self.btnSaveClicked)

    def btnLoadClicked(self):
        image = QFileDialog.getOpenFileName(None, '이미지로드', '', 'Image file(*.jpg;*.png)')
        imagePath = image[0]
        pixmap = QPixmap(imagePath).scaledToHeight(381) # 파일 경로에 있는 이미지를 읽어서 pixmap객체에 담기
        self.lb_canvas.setPixmap(pixmap) 
        self.lb_canvas.adjustSize() # 이미지를 라벨크기에 맞추기

    def btnSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '이미지저장', '', 'Image file(*.jpg;*.png)') 
        if filePath == '': return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)
    
    def buttonClicked(self): # black, red, blue를 다 통일한 함수
        btn_val = self.sender().objectName()
        print(btn_val)
        if btn_val == 'btn_black': # 검은버튼 클릭
            self.brushColor = Qt.black
        elif btn_val == 'btn_red': # 빨간버튼 클릭
            self.brushColor = Qt.red
        elif btn_val == 'btn_blue': # 파란버튼 클릭
            self.brushColor = Qt.blue
        elif btn_val == 'btn_clear': # 클리어
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap(self.canvas)

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap()) # 
        brush.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap))
        brush.drawPoint(e.x(), e.y())
        brush.end()
        self.update() # 화면 업데이트

    def setCenter(self): ## 화면정중앙 위치
        gm = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        gm.moveCenter(cp)
        self.move(gm.topLeft())   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())