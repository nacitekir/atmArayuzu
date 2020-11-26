import sys
from PyQt5 import QtWidgets,QtGui


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("ANA MENÜ")
        self.setGeometry(100, 100, 500, 500)
        self.yaziAlani = QtWidgets.QLabel("PYTHON Bank'a Hoşgeldiniz")


        self.buton = QtWidgets.QPushButton("Para Çek")
        self.buton1 = QtWidgets.QPushButton("Para Yatır")
        self.buton2 = QtWidgets.QPushButton("Bakiye Sor")
        self.buton3 = QtWidgets.QPushButton("Çıkış")

        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap("python.jpeg"))



        v_box = QtWidgets.QVBoxLayout()

        h_box =QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.logo)
        h_box.addStretch()

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.yaziAlani)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.buton)
        h_box2.addWidget(self.buton1)

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.buton2)
        h_box3.addWidget(self.buton3)

        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addStretch()

        self.setLayout(v_box)


        self.buton.clicked.connect(self.paraCek)
        self.buton1.clicked.connect(self.paraYatir)
        self.buton2.clicked.connect(self.bakiyeSor)
        self.buton3.clicked.connect(self.cikis)

        self.show()

    def paraCek(self):
        self.pencere1 = Pencere1()

    def paraYatir(self):
        self.pencere2 = Pencere2()

    def bakiyeSor(self):
        self.pencere3 = Pencere3()

    def cikis(self):
        QtWidgets.qApp.quit()





class Pencere1(QtWidgets.QWidget):
    def __init__(self):
            super().__init__()

            self.init_ui()
    def init_ui(self):

        self.setWindowTitle("PARA ÇEKME")
        self.setGeometry(100, 100, 500, 500)

        self.buton =QtWidgets.QPushButton("TAMAM")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.buton)
        v_box.addStretch()
        self.setLayout(v_box)

        self.buton.clicked.connect(self.cikis)


        self.show()

    def cikis(self):
        QtWidgets.qApp.quit()

class Pencere2(QtWidgets.QWidget):
    def __init__(self):
            super().__init__()

            self.init_ui()
    def init_ui(self):

        self.setWindowTitle("PARA YATIR")
        self.setGeometry(100, 100, 500, 500)

        self.etiket =QtWidgets.QLabel("Para Yatırmaya Hoşgeldin")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.etiket)
        self.setLayout(v_box)


        self.show()

class Pencere3(QtWidgets.QWidget):
    def __init__(self):
            super().__init__()

            self.init_ui()
    def init_ui(self):

        self.setWindowTitle("BAKİYE ÖĞRENME")
        self.setGeometry(100, 100, 500, 500)

        self.etiket =QtWidgets.QLabel("Bakiye öğrenmeye Hoşgeldin")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.etiket)
        self.setLayout(v_box)


        self.show()




app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()


sys.exit(app.exec_())