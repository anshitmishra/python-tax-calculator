from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QLineEdit
from PyQt5 import uic
from PyQt5 import QtGui
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("tax.ui",self)

        self.setWindowTitle("Tax calculator")
        self.setWindowIcon(QtGui.QIcon('image/logo.jpg'))
        self.input = self.findChild(QLineEdit,"lineEdit")
        self.calculate = self.findChild(QPushButton,"pushButton")
        self.answer = self.findChild(QLabel,'label_2')

        self.calculate.clicked.connect(lambda:self.cal())

        # show the app
        self.show()

    def cal(self):
        income = int(self.input.text())
        tax = 0
        if income <= 250000:  #2 Lakh 50 thousand
            tax = 0
        elif income <= 500000: #5 Lakh
            tax = (income - 250000) * 0.05
        elif income <= 750000: #7 lakh 50 thousand
            tax = (income - 500000) * 0.10 + 12500 
        elif income <= 1000000: #10 Lakh
            tax = (income - 750000) * 0.15 + 37500 
        elif income <= 1250000: #12 lakh 50 thousand
            tax = (income - 1000000) * 0.20 + 75000 
        elif income <= 1500000: #15 lakh
            tax = (income - 1250000) * 0.25 + 125000 
        else:
            tax = (income - 1500000) * 0.30 + 187500
        self.answer.setText(f'you owe {tax} Rupees in tax!')




app = QApplication(sys.argv)
UIWindow= UI()
app.exec_()



