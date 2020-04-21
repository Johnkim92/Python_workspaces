# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# =============================================================================
#   GUI 창 만들기
# =============================================================================
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle('My First Application') 
        # 타이틀바에 나타나는 창의 제목을 설정
        self.move(300, 300) # 위젯을 스크린의 좌표 위치로 이동시킨다.
        self.resize(400, 200)   # 위젯의 크기를 (너비, 높이)로 조절해준다.
        self.show()
        
if __name__ == 'MyApp':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''


'''
1. __name__ 의 경우 모듈을 직접 사용하게 된다면 __main__으로 되지만, import를 통해서
 가지고 들어오는 경우에는 __모듈명__ 이 된다.
2. PyQt5 어플리케이션은 어플리케이션 객체를 생성해야한다. 
 app = QApplication(sys.argv) 
'''


# =============================================================================
#   어플리케이션 아이콘 만들기
# =============================================================================
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class MyApp1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('C:/acon_python/apple.png')) 
        # 앱 아이콘을 생성해주는 함수
        # png 이미지 파일확장자가 가장 프로그램에 사용하기 좋다.
        # QIcon : 특정 이미지를 아이콘으로 만들어주는 함수
        self.setGeometry(300, 300, 300, 200)
        # 창의 위치와 크기를 지정해주는 함수 위치와 크기 순서로 넣으면 된다.
        self.show()

if __name__ == '__main__':
    app1 = QApplication(sys.argv)
    ex1 = MyApp1()
    sys.exit(app1.exec_())
'''

# =============================================================================
#   Absolute positioning(절대적 배치)
# =============================================================================
'''
절대적 배치 방식은 각 위젯의 위치와 크기를 픽셀 단위로 설정해서 배치한다.
절대 배치 방식을 사용할 때는 다음의 제약을 이해해야한다.
1. 창의 크기를 조절해도 위젯의 크기와 위치는 변하지 않는다.
2. 다양한 플랫폼에서 어플리케이션이 다르게 보일 수 있다.
3. 어플리케이션의 폰트를 바꾸면 레이아웃이 망가질 수 있다.
4. 레이아웃을 바꾸고 싶다면 완전히 새로 고쳐야 하며 이는 매우 번거롭다.
'''
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MyApp2(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20,20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)
        btn1 = QPushButton('Button1', self)
        btn1.move(80,13)
        btn2 = QPushButton('Button1', self)
        btn2.move(80,53)
        
        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300,300,400,200)
        self.show()
if __name__ == '__main__':
    app2 = QApplication(sys.argv)
    ex2 = MyApp2()
    sys.exit(app2.exec_())
'''

# =============================================================================
#   QBoxLayout(박스레이아웃)
# =============================================================================

'''
QHBoxLayout, QVBoxLayout은 여러 위젯을 수평으로 수직으로 정렬하는 레이아웃 클래스이다.
생성자는 수평, 수직의 박스를 하나 만드는데, 다른 레이아웃 박스를 넣을 수 도 있고 위젯을 
배치할 수 도 있다.
'''
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton

class MyApp3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)  # 좌우 빈공간을 1의 비율로 지정(크기가 아니라 비율이다)
        
        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
if __name__ == '__main__':
    app3 = QApplication(sys.argv)
    ex3 = MyApp3()
    sys.exit(app3.exec_())    
'''

# =============================================================================
#  Grid Layout (그리드 레이아웃) 행과 열로 배치해주는 레이아웃
# =============================================================================
'''
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)


class MyApp4(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app4 = QApplication(sys.argv)
    ex = MyApp4()
    sys.exit(app4.exec_())
'''

# =============================================================================
# QCheckBox 위젯 on/off 기능 복합위젯으로 라벨과 버튼 기능을 동시에 갖는다.
# =============================================================================
'''
체크 박스가 선택되거나 해제될 때, stateChange()시그널을 발생한다.
변할 때마다 어떤 동작을 발생시키고 싶을 댸, 이 시그널을 특정슬롯에 연결할 수 있다.
체크 박스의 선택 여부를 확인하기 위해서 isChecked()메서드를 사용할 수 있다. 
(boolean으로 리턴)
일반적인 체크 박스는 선택/해제 상태만을 갖지만, setTristate() 메서드를 사용하면, 
변경없음(no change) 상태를 가질 수 있다. 이 체크박스는 사용자에게 선택하거나 선택하지 않음
옵션을 줄 때 유용하다.
세가지 상태를 갖는 체크 박스의 상태를 얻기 위해서는 checkState()메서드를 사용한다. 여부에
따라 2/1/0(선택/변경없음/해제)값을 반환한다.
text() 체크 박스의 라벨 텍스트를 반환
setText() 체크 박스의 라벨 텍스트를 설정
isChecked() 체크 박스의 상태를 반환
checkState() 체크 박스의 상태를 반환(2/1/0)
toggle() 체크박스의 상태를 변경.
시그널 관련 함수
pressed() 체크 박스를 누를 때 신호를 발생
released() 체크 박스에서 뗄 때 신호를 발생
clicked() 체크 박스를 클릭 할 때 신호를 발생
stateChanged() 체크 박스의 상태가 바뀔때 신호를 발생
'''
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt
# Qt는 상태를 전달 받아줄 때 사용하는 모듈

class MyApp5(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ') 

if __name__ == '__main__' :
    app5 = QApplication(sys.argv)
    ex = MyApp5()
    sys.exit(app5.exec_())
'''
# =============================================================================
#  QRadioButton
# =============================================================================
'''
라디오버튼은 단일 선택만 가능하다는 점이 체크박스와의 차이이다.
사용할 수 있는 함수
text() 버튼의 텍스트를 반환
setText() 라벨에 들어갈 텍스트를 설정
setChecked() 버튼의 선택여부를 설정
isChecked() 버튼의 선택 여부를 반환
toggle() 버튼의 상태를 변경한다.
'''
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton

class MyApp6(QWidget):
    
    def __init__ (self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)
        
        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()

if __name__ == '__main__' :
    app6 = QApplication(sys.argv)
    ex = MyApp6()
    sys.exit(app6.exec_())
'''

# =============================================================================
# QComboBox
# =============================================================================
'''
객체를 생성한 뒤 item들을 추가해주어야한다.
'''
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class MyApp7(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app7 = QApplication(sys.argv)
    ex = MyApp7()
    sys.exit(app7.exec_())
'''

# =============================================================================
# QLineEdit
# =============================================================================
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

class MyApp8(QWidget):
    
    def __init__ (self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60,40)
        
        qle = QLineEdit(self)
        qle.move(60,100)
        qle.textChanged[str].connect(self.onChanged)
        
        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        
if __name__ == '__main__':
    app8 = QApplication(sys.argv)
    ex = MyApp8()
    sys.exit(app8.exec_())        
'''

# =============================================================================
#  QProgressBar
# =============================================================================

'''
진행 표시줄의 최소값과 최대값을 모두 0으로 설정하면, 
진행 표시줄은 위의 그림과 같이 항상 진행 중인 상태로 표시됩니다. 
이 기능은 다운로드 하고 있는 파일의 용량을 알 수 없을 때 유용하게 사용 할 수 있습니다.
'''
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer

class MyApp9(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        
        self.btn = QPushButton('Strat', self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)
        
        self.timer = QBasicTimer()
        self.step = 0
        
        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def timerEvent(self, e): # 상속받은 함수 내용 고쳐쓰기(재정의하기)
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step+1
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
        
        
if __name__ == '__main__':
  app9 = QApplication(sys.argv)
  ex = MyApp9()
  sys.exit(app9.exec_())     
'''

# =============================================================================
# QSlider & QDial
# =============================================================================
'''
QSlider는 수평 또는 수직 방향의 슬라이더를 제공합니다.
슬라이더 틱의 간격을 조절하기 위해서는 setTickInterval() 메서드,
틱의 위치를 조절하기 위해서는 setTickPosition() 메서드를 사용한다.
setTickInterval()메서드의 입력값은 픽셀이아닌 값을 의미한다.
setTickPosition()의 값들
1.QSlider.NoTicks/0 틱표시 x
2.Qslider.TicksAbove/1 틱을 수평 슬라이더 위쪽에 표시
3.QSlider.TicksBelow/2 틱을 수평 슬라이더 아래쪽에 표시
4.QSlider.TicksBothSides/3 틱을 수평 슬라이더 양쪽에 표시
5.QSlider.TicksLeft/TicksAbove 틱을 수직 슬라이더 왼쪽에 표시
6.QSlider.TicksRight/TicksBelow 틱을 수직 슬라이더 오른쪽에 표시

QDial에서 notch를 표시하기 위해서는 setNotchesVisible(True) 메서드를 사용

두 기능에서 얻을 수 있는 시그널 (이벤트)
valueChanged() 슬라이더의 값이 변할 때
sliderPressed() 슬라이더를 움직이기 시작할 때
sliderMoved() 슬라이더를 움직이면 발생
sliderReleased() 슬라이더를 놓을 때 발생
'''
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt

class MyApp10(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.slider = QSlider(Qt.Vertical, self)
        self.slider.move(30,30)
        self.slider.setRange(0,50)
        self.slider.setSingleStep(2)
        
        self.dial = QDial(self)
        self.dial.move(50, 50)
        self.dial.setRange(0, 50)
        
        btn = QPushButton('Default', self)
        btn.move(35, 160)
        
        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)
        
        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300,300,300,200)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == '__main__':
  app10 = QApplication(sys.argv)
  ex = MyApp10()
  sys.exit(app10.exec_())
'''

# =============================================================================
# QSplitter
# =============================================================================
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt
# QFrame : 틀잡아주는 모듈 구분선 만들어주는 역할

class MyApp11(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        hbox = QHBoxLayout()
        
        top = QFrame()
        top.setFrameShape(QFrame.Box)
        
        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)
        
        midright = QFrame()
        midright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)
        
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        
        self.setWindowTitle('QSplitter')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
  app11 = QApplication(sys.argv)
  ex = MyApp11()
  sys.exit(app11.exec_())
'''

# =============================================================================
# QTabWidget
# =============================================================================
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout

class MyApp12(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        tab1 = QWidget()
        tab2 = QWidget()
        
        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')
        
        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        
        self.setLayout(vbox)      
        
        self.setWindowTitle('QSTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        

if __name__ == '__main__':
  app12 = QApplication(sys.argv)
  ex = MyApp12()
  sys.exit(app12.exec_())
'''

# =============================================================================
#  QPixmap 이미지를 뿌려줄 때 사용하는 모듈
# =============================================================================
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
# QLabel : 뿌릴 이미지의 가로, 세로 픽셀을 뽑아내서 출력하기 위해 사용

class MyApp13(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        pixmap = QPixmap('Apple.png')
        
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)
        
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)
        
        self.setWindowTitle('QPixmap')
        self.move(300,300)
        self.show()
        

if __name__ == '__main__':
  app13 = QApplication(sys.argv)
  ex = MyApp13()
  sys.exit(app13.exec_())
'''

# =============================================================================
#  QCalendarWidget
# =============================================================================
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate
# QDate : 클릭한 날짜를 str형태로 뽑기 위해 필요

class MyApp14(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)    # True일 경우 구분선이 나타남
        cal.clicked[QDate].connect(self.showDate)
        # 날짜관련모듈은 클릭시그널이 있음
        
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString('dd-MM-yyyy'))
        
        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def showDate(self, date):
        self.lbl.setText(date.toString('dd-MM-yyyy'))
        

        

if __name__ == '__main__':
  app14 = QApplication(sys.argv)
  ex = MyApp14()
  sys.exit(app14.exec_())
'''

# =============================================================================
#  QTextBrowser
# =============================================================================
'''
하이퍼텍스트 내비게이션을 포함하는 리치 텍스트 브라우저를 제공한다.
이는 QTextEdit의 확장형으로서 하이퍼 텍스트 문서의 링크들을 사용 할 수 있다.
편집 가능한 리치 텍스트 편집기를 사용하기 위해서는 QTextEdit을 사용해야한다.
하이퍼텍스트 네비게이션이 없는 텍스트 브라우저를 사용하기 위해서는 QTextEdit을
setReadOnly()를 사용해서 편집이 불가능하도록 해준다.
짧은 리치 텍스트를 표시하기 위해서는 QLabel을 사용할 수 있다.
'''
'''
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QTextBrowser,
                             QPushButton, QVBoxLayout)

class MyApp15(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)
        
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        
        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)
        
        self.setLayout(vbox)    
        
        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def clear_text(self):
        self.tb.clear()

if __name__ == '__main__':
  app15 = QApplication(sys.argv)
  ex = MyApp15()
  sys.exit(app15.exec_())
'''

# =============================================================================
#  QTextEdit
# =============================================================================

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit

class MyApp16(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.lbl2 = QLabel('The number of words is 0')
        
        self.te.textChanged.connect(self.text_changed)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()
        
        self.setLayout(vbox)
        
        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is '+str(len(text.split())))
        

if __name__ == '__main__':
  app16 = QApplication(sys.argv)
  ex = MyApp16()
  sys.exit(app16.exec_())

























