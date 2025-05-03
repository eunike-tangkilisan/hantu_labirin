#test ruffier app

#step 1: import modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#instruction file koneksiin
from instructions import *

from nike_ruffier2 import *

#koneksiin ke halaman selanjutnya
#....

#step 2: buat app 
app = QApplication([])


#step 3: buat kelas halaman start
class startPage(QWidget):
    #karakteristik
    def __init__(self):
        super().__init__() #inherts semua data dan method dari class parents
        self.design() #design halaman startpage
        self.koneksi() #koneksiin antar halaman (ex: hal 1 -> hal 2)
        self.set_apperance() #atur ukuran window app, nama window app dll
        self.show() #tampilin hal 1
    #method
    def design(self):
        #3 elements -> text welcome, text deskripsi, btn start
        self.welcome_txt = QLabel(txt_hello)
        self.desc_txt = QLabel(txt_instruction)
        self.btn = QPushButton(txt_next, self)
        #design
        self.layout = QVBoxLayout() #layout secara vertical
        #tambahin element di layout
        self.layout.addWidget(self.welcome_txt, alignment=Qt.AlignCenter) #alignment modifikasiin ya
        self.layout.addWidget(self.desc_txt, alignment=Qt.AlignCenter) 
        self.layout.addWidget(self.btn, alignment=Qt.AlignCenter) 
        #set layout ke hal start page
        self.setLayout(self.layout)
    
    def ganti_page(self):

        self.second_page = secondPage() #hal 2 -> nama kelas di file hal 2
        #karena mau ganti halaman -> hal 1 hide
        self.hide()
    def koneksi(self):
        self.btn.clicked.connect(self.ganti_page)
    
    def set_apperance(self):
        self.resize(win_width, win_height)
        self.setWindowTitle("ruffier apk")
        self.move(win_x,win_y)

start_page = startPage()
app.exec_()

