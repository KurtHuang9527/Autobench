
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import sys
import os
from PyQt4 import QtGui, QtCore


class Form(QtGui.QWidget):
    def __init__(self):
        super(Form, self).__init__()

        label1 = QtGui.QLabel('Host')
        label2 = QtGui.QLabel('uri')
        label3 = QtGui.QLabel('Low_Rate')
        label4 = QtGui.QLabel('High_Rate')
        label5 = QtGui.QLabel('Rate_step')
        label6 = QtGui.QLabel('Num_call')
        label7 = QtGui.QLabel('Num_connection')
        label8 = QtGui.QLabel('Timeout')
        label9 = QtGui.QLabel('File_name')



        self.host = QtGui.QLineEdit()
        self.host.setFixedWidth(200)
        self.host.setToolTip('Enter Host name.')
        self.host.setEchoMode(0)

        self.uri = QtGui.QLineEdit()
        self.uri.setFixedWidth(200)
        self.uri.setToolTip('Enter URI.')
        self.uri.setEchoMode(0)

        self.l_r = QtGui.QLineEdit()
        self.l_r.setFixedWidth(50)
        self.l_r.setToolTip('Enter Low Rate.')
        self.l_r.setEchoMode(0)

        self.h_r = QtGui.QLineEdit()
        self.h_r.setFixedWidth(50)
        self.h_r.setToolTip('Enter High Rate.')
        self.h_r.setEchoMode(0)

        self.rate_step = QtGui.QLineEdit()
        self.rate_step.setFixedWidth(50)
        self.rate_step.setToolTip('Enter Rate of Step.')
        self.rate_step.setEchoMode(0)

        self.n_c = QtGui.QLineEdit()
        self.n_c.setFixedWidth(50)
        self.n_c.setToolTip('Enter Number of Call.')
        self.n_c.setEchoMode(0)

        self.n_con = QtGui.QLineEdit()
        self.n_con.setFixedWidth(50)
        self.n_con.setToolTip('Enter Number of Connection.')
        self.n_con.setEchoMode(0)

        self.timeout = QtGui.QLineEdit()
        self.timeout.setFixedWidth(50)
        self.timeout.setToolTip('Enter Timeout peorid.')
        self.timeout.setEchoMode(0)

        self.f_n = QtGui.QLineEdit()
        self.f_n.setFixedWidth(200)
        self.f_n.setToolTip('Enter File name.')
        self.f_n.setEchoMode(0)


        self.send = QtGui.QPushButton('Send')
        self.send.setFixedSize(50,30)


        self.send.clicked.connect(self.press)


        layout1 = QtGui.QFormLayout()
        layout1.addRow(label1, self.host)
        layout1.addRow(label2, self.uri)
        layout1.addRow(label3, self.l_r)
        layout1.addRow(label4, self.h_r)
        layout1.addRow(label5, self.rate_step)
        layout1.addRow(label6, self.n_c)
        layout1.addRow(label7, self.n_con)
        layout1.addRow(label8, self.timeout)
        layout1.addRow(label9, self.f_n)
        layout1.addWidget(self.send)




        layout = QtGui.QVBoxLayout()
        layout.addLayout(layout1)



        self.setLayout(layout)
        self.setGeometry(400,400,300,10)
        self.setWindowTitle("Input data")
        self.show()

    def press(self):

        if self.host.text() and self.l_r.text() and self.n_con.text() and self.h_r.text() and self.rate_step.text() and self.n_c.text() and self.timeout.text() and self.f_n.text() !="" :

            a=str("autobench")
            b=str("--single_host")
            c=str("--host1="+self.host.text())
            d=str("--port1=80")
            e=str("--uri1="+self.uri.text())
            f=str("--quiet")
            g=str("--low_rate="+self.l_r.text())
            h=str("--high_rate="+self.h_r.text())
            i=str("--rate_step="+self.rate_step.text())
            j=str("--num_call="+self.n_c.text())
            k=str("--num_conn="+self.n_con.text())
            l=str("--timeout="+self.timeout.text())
            m=str("--file")
            n=str("/home/"+self.f_n.text())


            args = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
            print(args)
            subprocess.call(args)
            self.close()


            super(Form, self).__init__()

            self.rlabel1 = QtGui.QLabel('Finished')
            self.send = QtGui.QPushButton('See Result')
            self.send.pressed.connect(self.result)
            self.send.clicked.connect(self.close)



            rlayout1 = QtGui.QVBoxLayout()
            rlayout1.addWidget(self.rlabel1)
            rlayout1.addWidget(self.send)


            self.setLayout(rlayout1)
            self.setGeometry(400,400,300,10)
            self.setWindowTitle("Finished")
            self.show()



        else:

            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Information)
            message.setWindowTitle("Oops!")
            message.setText("All Fields are must filled.")
            message.setStandardButtons(QtGui.QMessageBox.Close)
            message.exec_()



    def result(self):
        fn=self.f_n.text()
        if os.path.getsize('/home/'+fn) > 0:

            a=str("bench2graph")
            b=str("/home/"+self.f_n.text())
            c=str("/home/Pic.png")
            args=[a, b, c]
            print(args)
            subprocess.call(args)



            super(Form, self).__init__()

            self.ilabel1 = QtGui.QLabel('Result')
            close = QtGui.QPushButton('Close')
            close.clicked.connect(self.close)

            label_Image = QtGui.QLabel()
            image_path = '/home/Pic.png'
            image_profile = QtGui.QImage(image_path)
            image_profile = image_profile.scaled(800,800, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            label_Image.setPixmap(QtGui.QPixmap.fromImage(image_profile))

            ilayout1 = QtGui.QVBoxLayout()
            ilayout1.addWidget(self.ilabel1)
            ilayout1.addWidget(label_Image)
            ilayout1.addWidget(close)


            self.setLayout(ilayout1)
            self.setGeometry(400,400,300,10)
            self.setWindowTitle("Result")
            self.show()


        else:
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Information)
            message.setWindowTitle("Oops!")
            message.setText("Program is runngin, try again later.")
            message.setStandardButtons(QtGui.QMessageBox.Close)
            message.exec_()




app = QtGui.QApplication(sys.argv)
mainWindow = Form()
status = app.exec_()
sys.exit(status)


