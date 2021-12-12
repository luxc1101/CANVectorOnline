from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import os
import can
import can.interfaces.vector
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox,QFileDialog
import bgimage_rc
from datetime import date, datetime
import re
import numpy as np
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import psutil


class Ui_V_Online(QMainWindow):
    tx_msg = can.Message(dlc=8,
                         arbitration_id=0x01,
                         data=[0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88], 
                         channel=0)
    ValueErrorFlag = 0
    setid = {'all'}

        
    def setupUi(self, V_Online):
        V_Online.setObjectName("V_Online")
        V_Online.resize(880, 880)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),"Vector.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        V_Online.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(V_Online)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.TraceWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.TraceWidget.setObjectName("TraceWidget")
        self.tabreceive = QtWidgets.QWidget()
        self.tabreceive.setObjectName("tabreceive")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabreceive)
        self.gridLayout_3.setObjectName("gridLayout_3")
        # self.textEdit = QtWidgets.QTextEdit(self.tabreceive)
        self.textEdit_receive = QtWidgets.QTextEdit(self.tabreceive, readOnly= True ) 
        self.textEdit_receive.setPlaceholderText("Trace Window showing real time received data" )
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.textEdit_receive.setFont(font)
        self.textEdit_receive.setObjectName("textEdit_receive")
        self.gridLayout_3.addWidget(self.textEdit_receive, 0, 0, 1, 1)
        self.trackmessage = QtWidgets.QLineEdit(self.tabreceive)
        self.trackmessage.setStyleSheet( """QLineEdit { background-color: #2a045e; color: #f2f205 }""")
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.trackmessage.setFont(font)
        self.trackmessage.setReadOnly(True)
        self.trackmessage.setObjectName("trackmessage")
        self.gridLayout_3.addWidget(self.trackmessage, 1, 0, 1, 1)
        self.TraceWidget.addTab(self.tabreceive, "")
        self.tabsend = QtWidgets.QWidget()
        self.tabsend.setObjectName("tabsend")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabsend)
        self.gridLayout_4.setObjectName("gridLayout_4")
        # self.textEdit_send = QtWidgets.QTextEdit(self.tabsend)
        self.textEdit_send = QtWidgets.QTextEdit(self.tabsend, readOnly= True, ) 
        self.textEdit_send.setPlaceholderText("Trace Window showing real time sent data" )
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.textEdit_send.setFont(font)
        self.textEdit_send.setObjectName("textEdit_send")
        self.gridLayout_4.addWidget(self.textEdit_send, 0, 0, 1, 1)
        self.TraceWidget.addTab(self.tabsend, "")
        self.gridLayout_2.addWidget(self.TraceWidget, 6, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Quickselector = QtWidgets.QLabel(self.centralwidget)
        self.label_Quickselector.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Quickselector.setObjectName("label_Quickselector")
        self.horizontalLayout.addWidget(self.label_Quickselector)
        self.zero = QtWidgets.QCheckBox(self.centralwidget)
        self.zero.setObjectName("zero")
        self.horizontalLayout.addWidget(self.zero)
        self.eins = QtWidgets.QCheckBox(self.centralwidget)
        self.eins.setObjectName("eins")
        self.horizontalLayout.addWidget(self.eins)
        self.zwei = QtWidgets.QCheckBox(self.centralwidget)
        self.zwei.setObjectName("zwei")
        self.horizontalLayout.addWidget(self.zwei)
        self.drei = QtWidgets.QCheckBox(self.centralwidget)
        self.drei.setObjectName("drei")
        self.horizontalLayout.addWidget(self.drei)
        self.vier = QtWidgets.QCheckBox(self.centralwidget)
        self.vier.setObjectName("vier")
        self.horizontalLayout.addWidget(self.vier)
        self.funf = QtWidgets.QCheckBox(self.centralwidget)
        self.funf.setObjectName("funf")
        self.horizontalLayout.addWidget(self.funf)
        self.sechs = QtWidgets.QCheckBox(self.centralwidget)
        self.sechs.setObjectName("sechs")
        self.horizontalLayout.addWidget(self.sechs)
        self.sieben = QtWidgets.QCheckBox(self.centralwidget)
        self.sieben.setObjectName("sieben")
        self.horizontalLayout.addWidget(self.sieben)
        self.label_startbit = QtWidgets.QLabel(self.centralwidget)
        self.label_startbit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_startbit.setObjectName("label_startbit")
        self.horizontalLayout.addWidget(self.label_startbit)
        self.spinBox_startbit = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_startbit.setObjectName("spinBox_startbit")
        self.horizontalLayout.addWidget(self.spinBox_startbit)
        self.label_length = QtWidgets.QLabel(self.centralwidget)
        self.label_length.setAlignment(QtCore.Qt.AlignCenter)
        self.label_length.setObjectName("label_length")
        self.horizontalLayout.addWidget(self.label_length)
        self.spinBox_length = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_length.setObjectName("spinBox_length")
        self.horizontalLayout.addWidget(self.spinBox_length)
        self.dataplot = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.dataplot.setFont(font)
        self.dataplot.setObjectName("dataplot")
        self.dataplot.setEnabled(False)
        self.horizontalLayout.addWidget(self.dataplot)
        self.stopdataplot = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.stopdataplot.setFont(font)
        self.stopdataplot.setObjectName("stopdataplot")
        self.stopdataplot.setEnabled(False)
        self.horizontalLayout.addWidget(self.stopdataplot)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setBackgroundBrush(QtGui.QColor(232, 232, 232))
        self.graphicsView.getAxis('left').setPen('black')
        self.graphicsView.getAxis('left').setTextPen('black')
        self.graphicsView.getAxis('bottom').setPen('black')
        self.graphicsView.getAxis('bottom').setTextPen('black')
        self.graphicsView.showGrid(x=True, y=True, alpha=0.4)
        self.graphicsView.setMouseEnabled(x=True, y=True)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 8, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 5, 1, 1)
        self.comboBox_receiver_app = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_receiver_app.setObjectName("comboBox_receiver_app")
        self.comboBox_receiver_app.addItem("")
        self.comboBox_receiver_app.addItem("")
        self.gridLayout.addWidget(self.comboBox_receiver_app, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 5, 1, 1)
        self.receiver_serial = QtWidgets.QLineEdit(self.centralwidget)
        self.receiver_serial.setObjectName("receiver_serial")
        self.gridLayout.addWidget(self.receiver_serial, 3, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 7, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.comboBox_sender_app = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_sender_app.setObjectName("comboBox_sender_app")
        self.comboBox_sender_app.addItem("")
        self.comboBox_sender_app.addItem("")
        self.gridLayout.addWidget(self.comboBox_sender_app, 2, 8, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.bitrate_receiver = QtWidgets.QLineEdit(self.centralwidget)
        self.bitrate_receiver.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.bitrate_receiver, 3, 1, 1, 1)
        self.comboBox_receiver_chn = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_receiver_chn.setObjectName("comboBox_receiver_chn")
        self.comboBox_receiver_chn.addItem("")
        self.comboBox_receiver_chn.addItem("")
        self.comboBox_receiver_chn.addItem("")
        self.comboBox_receiver_chn.addItem("")
        self.comboBox_receiver_chn.addItem("")
        self.comboBox_receiver_chn.addItem("")
        self.gridLayout.addWidget(self.comboBox_receiver_chn, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 5, 1, 1)
        self.bitrate_sender = QtWidgets.QLineEdit(self.centralwidget)
        self.bitrate_sender.setObjectName("bitrate_sender")
        self.gridLayout.addWidget(self.bitrate_sender, 3, 6, 1, 1)
        self.toolButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 1, 7, 1, 1)

        self.radioButton_R = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_R.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton_R, 0, 7, 1, 2)

        self.comboBox_sender_chn = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_sender_chn.setObjectName("comboBox_sender_chn")
        self.comboBox_sender_chn.addItem("")
        self.comboBox_sender_chn.addItem("")
        self.comboBox_sender_chn.addItem("")
        self.comboBox_sender_chn.addItem("")
        self.comboBox_sender_chn.addItem("")
        self.comboBox_sender_chn.addItem("")
        self.gridLayout.addWidget(self.comboBox_sender_chn, 2, 6, 1, 1)
        self.StartRBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.StartRBtn.setFont(font)
        self.StartRBtn.setObjectName("StartRBtn")
        self.gridLayout.addWidget(self.StartRBtn, 1, 4, 1, 1)
        self.logpath_le = QtWidgets.QLineEdit(self.centralwidget)
        self.logpath_le.setObjectName("logpath_le")
        self.gridLayout.addWidget(self.logpath_le, 1, 3, 1, 1)
        self.fileopen_le = QtWidgets.QLineEdit(self.centralwidget)
        self.fileopen_le.setObjectName("fileopen_le")
        self.gridLayout.addWidget(self.fileopen_le, 1, 6, 1, 1)
        self.StopRBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.StopRBtn.setFont(font)
        self.StopRBtn.setObjectName("StopRBtn")
        self.gridLayout.addWidget(self.StopRBtn, 2, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 5, 1, 1)
        self.sender_serial = QtWidgets.QLineEdit(self.centralwidget)
        self.sender_serial.setObjectName("sender_serial")
        self.gridLayout.addWidget(self.sender_serial, 3, 8, 1, 1)
        self.StopSBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.StopSBtn.setFont(font)
        self.StopSBtn.setObjectName("StopSBtn")
        self.gridLayout.addWidget(self.StopSBtn, 3, 9, 1, 1)
        self.StartSBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.StartSBtn.setFont(font)
        self.StartSBtn.setObjectName("StartSBtn")
        self.gridLayout.addWidget(self.StartSBtn, 2, 9, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 2, 1)
        V_Online.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(V_Online)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 22))
        self.menubar.setObjectName("menubar")
        V_Online.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(V_Online)
        self.statusbar.setObjectName("statusbar")
        V_Online.setStatusBar(self.statusbar)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setStyleSheet("border-image: url(:/newPrefix/pycanlogo.png);")
        self.label_15.setText("")
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 8, 2, 2)


        self.retranslateUi(V_Online)
        QtCore.QMetaObject.connectSlotsByName(V_Online)
        self.radioButton.toggled.connect(self.logfile)
        self.toolButton.clicked.connect(self.readfile)

        self.thread = {}
        # start and stop sending event
        self.StartSBtn.clicked.connect(self.start_sending)
        self.StopSBtn.clicked.connect(self.stop_sending)
        # start and stop receiving event
        self.StartRBtn.clicked.connect(self.start_receiving)
        self.StopRBtn.clicked.connect(self.stop_receiving)
        # start thrawing cirve
        self.dataplot.clicked.connect(self.start_plotting)
        self.stopdataplot.clicked.connect(self.clear_plotting)

    def retranslateUi(self, V_Online):
        _translate = QtCore.QCoreApplication.translate
        V_Online.setWindowTitle(_translate("V_Online", "VectorWindow"))
        self.label_7.setText(_translate("V_Online", "Graphics"))
        self.label_5.setText(_translate("V_Online", "Trace"))
        self.label_Quickselector.setText(_translate("V_Online", "Quick Select:"))
        self.zero.setText(_translate("V_Online", "0"))
        self.eins.setText(_translate("V_Online", "1"))
        self.zwei.setText(_translate("V_Online", "2"))
        self.drei.setText(_translate("V_Online", "3"))
        self.vier.setText(_translate("V_Online", "4"))
        self.funf.setText(_translate("V_Online", "5"))
        self.sechs.setText(_translate("V_Online", "6"))
        self.sieben.setText(_translate("V_Online", "7"))
        self.label_length.setText(_translate("V_Online", "Length:"))
        self.label_startbit.setText(_translate("V_Online", "Startbit:"))
        self.dataplot.setText(_translate("V_Online", "Plot/Replot"))
        self.stopdataplot.setText(_translate("V_Online", "Stop"))
        self.label_10.setText(_translate("V_Online", "Sender Setup"))
        self.comboBox.setItemText(0, _translate("V_Online", "all"))
        self.comboBox_receiver_app.setItemText(0, _translate("V_Online", "python-can"))
        self.comboBox_receiver_app.setItemText(1, _translate("V_Online", "CANalyzer"))
        self.label_3.setText(_translate("V_Online", "Serial Nr."))
        self.label.setText(_translate("V_Online", "Channel"))
        self.radioButton.setText(_translate("V_Online", "Logging"))
        self.label_11.setText(_translate("V_Online", "Baudrate (bps)"))
        self.receiver_serial.setText(_translate("V_Online", "88399"))
        self.label_13.setText(_translate("V_Online", "Serial Nr."))
        self.label_12.setText(_translate("V_Online", "App Name"))
        self.label_2.setText(_translate("V_Online", "Baudrate (bps)"))
        self.label_4.setText(_translate("V_Online", "App Name"))
        self.label_6.setText(_translate("V_Online", "File Name"))
        self.comboBox_sender_app.setItemText(0, _translate("V_Online", "python-can"))
        self.comboBox_sender_app.setItemText(1, _translate("V_Online", "CANalyzer"))
        self.label_8.setText(_translate("V_Online", "Receiver Setup"))
        self.bitrate_receiver.setText(_translate("V_Online", "500000"))
        self.comboBox_receiver_chn.setItemText(0, _translate("V_Online", '1'))
        self.comboBox_receiver_chn.setItemText(1, _translate("V_Online", '0'))
        self.comboBox_receiver_chn.setItemText(2, _translate("V_Online", '3'))
        self.comboBox_receiver_chn.setItemText(3, _translate("V_Online", '2'))
        self.comboBox_receiver_chn.setItemText(4, _translate("V_Online", '5'))
        self.comboBox_receiver_chn.setItemText(5, _translate("V_Online", '4'))
        self.label_9.setText(_translate("V_Online", "Channel"))
        self.bitrate_sender.setText(_translate("V_Online", "500000"))
        self.toolButton.setText(_translate("V_Online", "Open File"))
        self.radioButton_R.setText(_translate("V_Online", "Repeat"))
        self.comboBox_sender_chn.setItemText(0, _translate("V_Online", '0'))
        self.comboBox_sender_chn.setItemText(1, _translate("V_Online", '1'))
        self.comboBox_sender_chn.setItemText(2, _translate("V_Online", '2'))
        self.comboBox_sender_chn.setItemText(3, _translate("V_Online", '3'))
        self.comboBox_sender_chn.setItemText(4, _translate("V_Online", '4'))
        self.comboBox_sender_chn.setItemText(5, _translate("V_Online", '5'))
        self.StartRBtn.setText(_translate("V_Online", "Start receiving"))
        self.StopRBtn.setText(_translate("V_Online", "Stop receiving"))
        self.label_14.setText(_translate("V_Online", "File Open"))
        self.sender_serial.setText(_translate("V_Online", "88399"))
        self.StopSBtn.setText(_translate("V_Online", "Stop sending"))
        self.StartSBtn.setText(_translate("V_Online", "Start sending"))
        self.TraceWidget.setTabText(self.TraceWidget.indexOf(self.tabreceive), _translate("V_Online", "Receive"))
        self.TraceWidget.setTabText(self.TraceWidget.indexOf(self.tabsend), _translate("V_Online", "Send"))
        # self.trackmessage.setText(_translate("V_Online", "Showing the tracked message"))
        self.trackmessage.setPlaceholderText(_translate("V_Online", "Showing the tracked message"))
####################################################
#                                                 
#                  Graphics                       
#                                                 
####################################################
    def start_plotting(self):
        selectID = self.comboBox.currentText()
        if selectID != 'all':
            title = selectID
            self.dataplot.setEnabled(True)
            self.stopdataplot.setEnabled(True)
        else:
            title = ''
        if (True not in self.bitselection()) and (self.bitselection2()[1] == 0):
            QMessageBox.information(self,'Info', 'Please select starbit and length')
        else:
            self.graphicsView.clear()
            self.thread[3] = CANgraph(parent = None, plotWidget=self.graphicsView, title= title, receiver=self.thread[2], mask=self.bitselection(), mask2=self.bitselection2())
            self.thread[3].start()
            self.dataplot.setEnabled(False)
            self.zero.setEnabled(False)
            self.eins.setEnabled(False)
            self.zwei.setEnabled(False)
            self.drei.setEnabled(False)
            self.vier.setEnabled(False)
            self.funf.setEnabled(False)
            self.sechs.setEnabled(False)
            self.sieben.setEnabled(False)
            self.spinBox_startbit.setEnabled(False)
            self.spinBox_length.setEnabled(False)

    def clear_plotting(self):
        self.thread[3].stop()
        self.dataplot.setEnabled(True)
        self.zero.setEnabled(True)
        self.eins.setEnabled(True)
        self.zwei.setEnabled(True)
        self.drei.setEnabled(True)
        self.vier.setEnabled(True)
        self.funf.setEnabled(True)
        self.sechs.setEnabled(True)
        self.sieben.setEnabled(True)
        self.spinBox_startbit.setEnabled(True)
        self.spinBox_length.setEnabled(True)

    def bitselection(self):
        mask = [False]*8
        if self.zero.isChecked(): mask[0]    = True
        if self.eins.isChecked(): mask[1]    = True
        if self.zwei.isChecked(): mask[2]    = True
        if self.drei.isChecked(): mask[3]    = True
        if self.vier.isChecked(): mask[4]    = True
        if self.funf.isChecked(): mask[5]    = True
        if self.sechs.isChecked(): mask[6]   = True
        if self.sieben.isChecked(): mask[7]  = True
        else: mask = mask
        return mask

    def bitselection2(self):
       startbit = self.spinBox_startbit.value()
       datalength = self.spinBox_length.value()
       return startbit, datalength 

####################################################
#                                                 
#                  Sender                       
#                                                 
####################################################
    def start_sending(self):
        # send message
        self.thread[1] = SendThread(parent    = None, 
                                    tx_msg    = self.tx_msg,
                                    channel   = [int(self.comboBox_sender_chn.currentText())],
                                    bitrate   = int(self.bitrate_sender.text()),
                                    serial    = int(self.sender_serial.text()),
                                    app_name  = self.comboBox_sender_app.currentText(),
                                    r_btn     = self.radioButton_R.isChecked(),
                                    ascfile   = self.fileopen_le.text())
        try:
            QMessageBox.critical(self,'Error', self.thread[1].error)
        except:
            self.thread[1].error = ''
            pass

        self.textEdit_send.clear()
        self.thread[1].start()
        self.thread[1].tx_signal.connect(self.Update_tx_msg)
        if len(self.thread[1].error) > 0:
            self.StartSBtn.setEnabled(True)
            self.comboBox_sender_chn.setEnabled(True)
            self.comboBox_sender_app.setEnabled(True)
            self.toolButton.setEnabled(True) 
            self.radioButton_R.setEnabled(True)
        else: 
            self.StartSBtn.setEnabled(False)
            self.comboBox_sender_chn.setEnabled(False)
            self.comboBox_sender_app.setEnabled(False)
            self.toolButton.setEnabled(False)
            self.radioButton_R.setEnabled(False)

    def stop_sending(self):
        # stop sending message
        self.thread[1].stop()
        self.StopSBtn.setEnabled(True)
        self.StartSBtn.setEnabled(True)
        self.comboBox_sender_chn.setEnabled(True)
        self.comboBox_sender_app.setEnabled(True)
        self.toolButton.setEnabled(True)
        self.radioButton_R.setEnabled(True)
####################################################
#                                                 
#                  Receiver                       
#                                                 
####################################################
    def start_receiving(self):
        self.comboBox.addItem('all')
        self.thread[2] = ReceiveThread(parent    = None, 
                                       channel   = [int(self.comboBox_receiver_chn.currentText())],
                                       bitrate   = int(self.bitrate_receiver.text()),
                                       serial    = int(self.receiver_serial.text()),
                                       app_name  = self.comboBox_receiver_app.currentText(),
                                       )
        try:
            QMessageBox.critical(self,'Error', self.thread[2].error)
        except:
            self.thread[2].error = ''
            pass
        self.textEdit_receive.clear()
        self.thread[2].start()
        self.thread[2].rx_signal.connect(self.Update_rx_msg)
        if len(self.thread[2].error) > 0:
            self.StartRBtn.setEnabled(True)
            self.comboBox_receiver_chn.setEnabled(True)
            self.comboBox_receiver_app.setEnabled(True) 
        else: 
            self.StartRBtn.setEnabled(False)
            self.comboBox_receiver_chn.setEnabled(False)
            self.comboBox_receiver_app.setEnabled(False)
        self.ValueErrorFlag = 0

    def stop_receiving(self):
        # stop receiving message
        if self.radioButton.isChecked():
            self.ascwriter.stop()

        #TODO: try except thread[3] is isRuning or not
        try:
            self.thread[3].stop()
        except:
            pass
        self.thread[2].stop()
        self.setid = {'all'}
        self.comboBox.clear()
        self.trackmessage.clear()
        self.StopRBtn.setEnabled(True)
        self.StartRBtn.setEnabled(True)
        self.comboBox_receiver_chn.setEnabled(True)
        self.comboBox_receiver_app.setEnabled(True)
        self.dataplot.setEnabled(False)
        self.stopdataplot.setEnabled(False)

####################################################
#                                                 
#                  Update RxTx message                       
#                                                 
####################################################
    def Update_tx_msg(self,msg):
        tx_msg = msg
        self.textEdit_send.append('Timestamp:{timestamp:10.6f}{fill1}Channel:{channel}{fill1}ID: {ID:<10}{fill1}Tx  DLC:{DLC:^5d}'.format(timestamp = tx_msg.timestamp, channel = tx_msg.channel, fill1 = '\t',ID = hex(tx_msg.arbitration_id), DLC = tx_msg.dlc) + '{}'.format(' '.join(re.findall('..', tx_msg.data.hex()))))

    def Update_rx_msg(self,msg):
        rx_msg = msg
        selectID = self.comboBox.currentText()
        # if none of specific message be selected will plot button unable to be clicked and if can plot thread is running it should be stopped
        if selectID == 'all' or selectID == None:
            self.dataplot.setEnabled(False)
            self.stopdataplot.setEnabled(False)
            try:
                self.thread[3].stop()
            except:
                pass
        else:
            self.dataplot.setEnabled(True)
            self.stopdataplot.setEnabled(True)

        if rx_msg.dlc != 0:
            # add message line by line
            # update the ranked Message-IDs into comboBox
            if hex(rx_msg.arbitration_id) not in self.setid:
                self.setid.add(hex(rx_msg.arbitration_id))
                sorted_setid_idx = list(sorted(self.setid,reverse=True)).index(hex(rx_msg.arbitration_id))
                self.comboBox.insertItem(sorted_setid_idx,hex(rx_msg.arbitration_id))

            if selectID == 'all':    
                self.textEdit_receive.append('Timestamp:{timestamp:10.6f}{fill1}Channel:{channel}{fill1}ID: {ID:<10}{fill1}Rx  DLC:{DLC:^5d}'.format(timestamp = rx_msg.timestamp, channel = rx_msg.channel,fill1 = '\t',ID = hex(rx_msg.arbitration_id), DLC = rx_msg.dlc) + '{}'.format(' '.join(re.findall('..', rx_msg.data.hex()))))
            if selectID == hex(rx_msg.arbitration_id):
                self.textEdit_receive.append('Timestamp:{timestamp:10.6f}{fill1}Channel:{channel}{fill1}ID: {ID:<10}{fill1}Rx  DLC:{DLC:^5d}'.format(timestamp = rx_msg.timestamp, channel = rx_msg.channel,fill1 = '\t',ID = hex(rx_msg.arbitration_id), DLC = rx_msg.dlc) + '{}'.format(' '.join(re.findall('..', rx_msg.data.hex()))))
                self.trackmessage.setText('Timestamp:{timestamp:10.6f}{fill1}Channel:{channel}{fill1}ID: {ID:<10}{fill1}Rx  DLC:{DLC:^5d}'.format(timestamp = rx_msg.timestamp, channel = rx_msg.channel,fill1 = '\t',ID = hex(rx_msg.arbitration_id), DLC = rx_msg.dlc) + '{}'.format(' '.join(re.findall('..', rx_msg.data.hex()))))
        if self.radioButton.isChecked():
            try:
                self.ascwriter.on_message_received(rx_msg)
            except ValueError as e:
                self.ValueErrorFlag += 1
                if self.ValueErrorFlag == 1:
                    QMessageBox.critical(self,'Error',str(e))
####################################################
#                                                 
#                  Update RxTx message                       
#                                                 
####################################################
    def logfile(self):
        if self.radioButton.isChecked():
            root = QFileDialog.getExistingDirectory(self, 'Select directory', directory= "C:/Code/PycanData")
            date = datetime.utcnow().strftime('%d%m')
            # trying to creat a log file
            try:
                i = 0
                while os.path.exists(root + '/' + 'pycan_{}_logging_{}.asc'.format(date,i)):
                    i += 1
                self.logfilepath = root + '/' + 'pycan_{}_logging_{}.asc'.format(date,i)
                # showing the log file path in lineEdit
                self.logpath_le.setText(self.logfilepath)
                # set a ascwriter to log the reveived message in Vector format
                self.ascwriter = can.ASCWriter(file = self.logfilepath, channel= [int(self.comboBox_receiver_chn.currentText())])
                QMessageBox.information(self, 'Logging', 'Get ready to log.')
            except:
                QMessageBox.critical(self,'Error', 'logging failed.') 
                self.logfilepath = None
        else:
            pass

    def readfile(self):
        file = QFileDialog.getOpenFileName(parent = self, caption = "Open File",directory= "C:/Autel/Doc/Data/CAN_ASC/2010ASC/Contaktless_Reader_Test_losfahren", filter= "Data file (*.asc)")
        fileName, ext = file[0], file[1]
        self.fileopen_le.setText(fileName)
        print(self.fileopen_le.text())
        try:
            self.tx_msg = can.ASCReader(file = self.fileopen_le.text())
            self.comboBox.clear()
        except:
            QMessageBox.critical(self,'Error', 'Failed to open file, Test message will be sent') 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                                                 
#                   Thread Class                   
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                                                 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ReceiveThread(QThread):
    """Thread for Receiving CAN Message"""
    rx_signal = pyqtSignal(can.message.Message)
    # rx_signal_dataplot = pyqtSignal(str)
    # rxmsg_signal = pyqtSignal()
    def __init__(self, parent, channel:list, bitrate: int, serial: int, app_name: str):
        super(ReceiveThread, self).__init__(parent)
        self.is_running  = True
        self.connected   = False
        self.channel     = channel
        self.bitrate     = bitrate
        self.serial      = serial
        self.app_name    = app_name
        self.fd          = True
        try:
            self.bus = can.interfaces.vector.VectorBus(channel= self.channel,
                                            poll_interval=0.0001, 
                                            bitrate = self.bitrate, 
                                            serial = self.serial, 
                                            app_name = self.app_name,
                                            fd= self.fd)
            self.connected = True
        except Exception as e:
            self.connected = False
            self.error = str(e)
    
    def run(self):
        start_time = time.time()
        while self.connected:
            rx_msg = self.bus.recv(10)
            if rx_msg is not None and rx_msg.dlc != 0:
                rx_msg.timestamp = time.time()-start_time
                # print(rx_msg.timestamp)
                # print(self.rx_msg_to_bitselection)
                self.rx_signal_dataplot = rx_msg
                self.rx_signal.emit(rx_msg)
                # self.rx_signal_dataplot.emit(str(rx_msg))

    def stop(self):
        self.is_running = False
        self.terminate()


class SendThread(QThread):
    """Thread for Sending CAN Message"""
    tx_signal = pyqtSignal(can.message.Message)
    def __init__(self, parent, tx_msg, channel:list, bitrate: int, serial: int, app_name: str, r_btn: bool, ascfile: str):
        super(SendThread, self).__init__(parent)
        self.is_running  = True
        self.connected   = False
        self.tx_msg      = tx_msg
        self.channel     = channel
        self.bitrate     = bitrate
        self.serial      = serial
        self.app_name    = app_name
        self.fd          = True
        self.repeat_btn  = r_btn
        self.ascfile        = ascfile
        try:
            self.bus = can.interfaces.vector.VectorBus(channel= self.channel,
                                                    poll_interval=0.0001, 
                                                    bitrate = self.bitrate, 
                                                    serial = self.serial, 
                                                    app_name = 'python-can',
                                                    fd = True)
            self.connected = True
        except Exception as e:
            self.connected = False
            self.error = str(e)

    def run(self):
        if self.connected:
            start_time = time.time()
            if type(self.tx_msg).__name__ == 'Message':          
                print('Start to send a message every 0.01s')
                while self.connected:    
                    self.tx_msg.timestamp = time.time()-start_time
                    self.bus.send(self.tx_msg)
                    self.tx_signal.emit(self.tx_msg)
                    # print('tx:{}'.format(self.tx_msg))
                    time.sleep(0.01)
            if type(self.tx_msg).__name__ == 'ASCReader':
                # start_time = 0.0
                if self.repeat_btn and self.ascfile !='':
                    while True:
                        for msg in self.tx_msg:
                            msg.timestamp = time.time()-start_time
                            self.bus.send(msg)
                            self.tx_signal.emit(msg)
                            # print('tx:{}'.format(msg))
                            time.sleep(0.00001)
                        self.tx_msg = can.ASCReader(file = self.ascfile)
                else: 
                    for msg in self.tx_msg:
                        msg.timestamp = time.time()-start_time
                        self.bus.send(msg)
                        self.tx_signal.emit(msg)
                        # print('tx:{}'.format(msg))
                        time.sleep(0.00001)


    def stop(self):
        self.is_running = False
        self.terminate()


class CANgraph(QThread):
    def __init__(self, parent, plotWidget, title, receiver, mask, mask2):
        super(CANgraph, self).__init__(parent)
        self.is_running = True
        # self.msg = msg
        self.plotWidget = plotWidget
        self.receiver = receiver
        self.y = []
        self.x = []
        self.pen = pg.mkPen(color='#440154FF', width=2)
        self.curve = self.plotWidget.plot(x = self.x,
                                          y = self.y, 
                                          symbol='x', 
                                          symbolBrush=('#FDE725FF'), 
                                          pen = self.pen,
                                          fillLevel=0, brush=(50,50,200,100),
                                          title='first graph')
        self.title = title
        self.plotWidget.setTitle("Message ID: {}".format(self.title), color="black", size="10pt")
        self.ptr1 = 0
        self.npfunc_hex_to_dec = np.vectorize(lambda x: int(x, 16))
        self.timestampoffset = self.receiver.rx_signal_dataplot.timestamp
        self.mask = np.array(mask)
        self.startbit, self.datalength = mask2[0],mask2[1]
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.run)
        self.timer.start(1) # unit: ms

    def mask2(self, data):
        hexadecimal  = data.hex()
        end_length = len(hexadecimal)*4
        hex_as_int = int(hexadecimal, 16)
        hex_as_binary = bin(hex_as_int)
        padded_binary = hex_as_binary[2:].zfill(end_length)
        layout_arr = np.array(list(padded_binary)).reshape(8,8)[::-1].reshape(1,-1)
        end = -1*self.startbit
        start = end - self.datalength
        return int(layout_arr[:,start:end].astype(object).sum(dtype = object, axis = 1)[0],2)        

    def run(self):
        timestamp = self.receiver.rx_signal_dataplot.timestamp - self.timestampoffset
        dlc       = self.receiver.rx_signal_dataplot.dlc
        msgdata   = self.receiver.rx_signal_dataplot.data
        if (dlc == 8) and (self.title == hex(self.receiver.rx_signal_dataplot.arbitration_id)) and (True in self.mask):
            byte_arr  = np.array('{}'.format(' '.join(re.findall('..', msgdata.hex()))).split(' '))[self.mask].astype(object).reshape((1,-1))
            byte_arr  = np.fliplr(byte_arr).sum(dtype = object, axis = 1)
            value = self.npfunc_hex_to_dec(byte_arr)[0]
            # self.y.append(psutil.cpu_percent()*1000) # pc cup percent for real data test   
            self.y.append(value)
            self.x.append(timestamp)    
            self.curve.setData(self.x,self.y)
        if dlc == 8 and self.title == hex(self.receiver.rx_signal_dataplot.arbitration_id):
            value = self.mask2(msgdata)
            self.y.append(value)
            self.x.append(timestamp)
            self.curve.setData(self.x,self.y) 

    def stop(self):
        self.is_running = False
        # self.plotWidget.clear()
        self.timer.stop()
        self.terminate()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.processEvents()
    V_Online = QtWidgets.QMainWindow()
    ui = Ui_V_Online()
    ui.setupUi(V_Online)
    V_Online.show()
    sys.exit(app.exec_())
