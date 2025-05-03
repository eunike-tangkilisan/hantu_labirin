#test ruffier app

#step 1: import modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#instruction file koneksiin
from instructions import *

#koneksiin ke halaman selanjutnya
from nike_ruffier3 import *

#step 2: buat app 
app = QApplication([])


#step 3: buat kelas halaman kedua
class get_result():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3 

class secondPage(QWidget):
    #karakteristik
    def __init__(self):
        super().__init__() #inherts semua data dan method dari class parents
        self.design() #design halaman startpage
        self.koneksi() #koneksiin antar halaman (ex: hal 1 -> hal 2)
        self.set_apperance() #atur ukuran window app, nama window app dll
        self.show() #tampilin hal 1
    
    def design(self):
        #masukin 15 element

        #element nama
        self.lb_name = QLabel(text="Enter your name:")
        self.in_name = QLineEdit()

        #element umur
        self.lb_age = QLabel(text="Enter your age:")
        self.in_age = QLineEdit(txt_hintage)

        #element test 1
        self.lb_test1 = QLabel(text="- Test 1 -")
        self.lb_inst1 = QLabel(text=txt_test1)
        self.in_res1 = QLineEdit(txt_hinttest1)
        self.btn_test1 = QPushButton(txt_starttest1)

        #element test 2
        self.lb_test2 = QLabel(text="- Test 2 -")
        self.lb_inst2 = QLabel(text=txt_test2)
        self.in_res2 = QLineEdit(txt_hinttest2)
        self.btn_test2 = QPushButton(txt_starttest2)

        #element test 3
        self.lb_test3 = QLabel(text="- Test 3 -")
        self.lb_inst3 = QLabel(text=txt_test3)
        self.in_res3 = QLineEdit(txt_hinttest3)
        self.btn_test3 = QPushButton(txt_starttest3)

        #element timer
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        #element btn scr 2
        self.btn = QPushButton(txt_sendresults)

        #layoutnya
        self.main_layout = QVBoxLayout()

        #layout nama
        self.name_layout = QHBoxLayout()
        self.name_layout.addWidget(self.lb_name)
        self.name_layout.addWidget(self.in_name)

        #layout umur
        self.age_layout = QHBoxLayout()
        self.age_layout.addWidget(self.lb_age)
        self.age_layout.addWidget(self.in_age)

        #layout btn + input test 1
        self.test1_layout = QHBoxLayout()
        self.test1_layout.addWidget(self.btn_test1)
        self.test1_layout.addWidget(self.in_res1)

        #layout btn + input test 2
        self.test2_layout = QVBoxLayout()
        self.btn_input_layout2 = QHBoxLayout()

        self.test2_layout.addWidget(self.lb_test2)
        self.test2_layout.addWidget(self.lb_inst2)

        #kelompok btn-input
        self.btn_input_layout2.addWidget(self.btn_test2)
        self.btn_input_layout2.addWidget(self.in_res2)

        #kelompok btn-input di taruh ke test2 layout
        self.test2_layout.addLayout(self.btn_input_layout2)

        #test2-timer layout
        self.test2_timer_layout = QHBoxLayout()
        self.test2_timer_layout.addLayout(self.test2_layout)
        self.test2_timer_layout.addWidget(self.text_timer)

        #layout btn + input test 3
        self.test3_layout = QHBoxLayout()
        self.test3_layout.addWidget(self.btn_test3)
        self.test3_layout.addWidget(self.in_res3)

        #set ke main layout
        self.main_layout.addLayout(self.name_layout)
        self.main_layout.addLayout(self.age_layout)

        #cara 1 - test 1
        self.main_layout.addWidget(self.lb_test1)
        self.main_layout.addWidget(self.lb_inst1)
        self.main_layout.addLayout(self.test1_layout)

        #cara 2 - test 2
        self.main_layout.addLayout(self.test2_timer_layout)

        #test 3
        self.main_layout.addWidget(self.lb_test3)
        self.main_layout.addWidget(self.lb_inst3)
        self.main_layout.addLayout(self.test3_layout)

        #btn
        self.main_layout.addWidget(self.btn)

        #set jadi layout screen 2
        self.setLayout(self.main_layout)

    def next_page(self):
        #hal 2 di hide
        self.hide()
        #hal 3 kita harus munculi
        #1 hal yang di ingat -> data dari hal 2 -> masuk ke hal 3
        #get_result => fungsi di hal 3
        self.exp = get_result(int(self.in_age.text()),int(self.in_res1.text()),int(self.in_res2.text()),int(self.in_res3.text()))


        
        #pindah hal
        self.third_page = thirdPage(self.exp)

    def timer_design_test_1(self):
        global time
        time =time.addSecs(1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 30, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:15":
            self.timer.stop()
        
    def timer_design_test_3(self):
        global time
        time = time.addSecs(1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 30, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:01:00":
            self.timer.stop()

    def timer_design_test_2(self):
        global time
        time = time.addSecs(1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 30, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:45":
            self.timer.stop()
    
    #timer
    def timer_test1(self):
        global time
        time = QTime(0,0,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_design_test_1)
        self.timer.start(1000) #perpindahan detik 1000 miliseconds = 1 seconds

    def timer_test2(self):
        global time
        time = QTime(0,0,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_design_test_2)
        self.timer.start(1000) #perpindahan detik 1000 miliseconds = 1 seconds

    def timer_test3(self):
        global time
        time = QTime(0,0,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_design_test_3)
        self.timer.start(1000) #perpindahan detik 1000 miliseconds = 1 seconds
    
    def koneksi(self): #koneksi btn
        self.btn.clicked.connect(self.next_page)
        self.btn_test1.clicked.connect(self.timer_test1)
        self.btn_test2.clicked.connect(self.timer_test2)
        self.btn_test3.clicked.connect(self.timer_test3)

    def set_apperance(self):
        self.resize(win_width, win_height)
        self.setWindowTitle("ruffier apk")
        self.move(win_x,win_y)

