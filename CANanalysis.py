import os
import numpy as np
import pandas as pd
from shutil import copyfile
import pathlib
import subprocess
from datetime import date, datetime
import calendar
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QDir, Qt, QUrl, QThread, pyqtSignal, QObject
from PyQt5.QtMultimediaWidgets import QVideoWidget, QGraphicsVideoItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView, QMessageBox, QVBoxLayout, QPushButton, QStyle
from pyqtgraph import PlotWidget

import pyqtgraph as pg
import math
from pathlib import Path, PureWindowsPath
from videoplayer import VideoWindow
from vectorGUI import Ui_V_Online




class Worker(QObject):
    """docstring for Worker"""
    finished = pyqtSignal()
    progress = pyqtSignal(list)


    def run(self, btn,tabWidget, df):
        '''tablefit'''
        tabWidget.setColumnCount(len(df.columns))
        tabWidget.setRowCount(len(df.index))
        tabWidget.setHorizontalHeaderLabels(list(df))
        if btn.isChecked():
            for i in range(len(df.index)):
                self.progress.emit([i, df.values.shape[0]])
                for j in range(len(df.columns)):
                    tabWidget.setItem(i,j,QTableWidgetItem(df.iloc[i,j]))

            for col in range(len(df.columns)):      
                tabWidget.horizontalHeader().setSectionResizeMode(col, QHeaderView.ResizeToContents)
        else:
            tabWidget.setRowCount(0)

        self.finished.emit()



class Ui_LUXC(QMainWindow):
    COMPLETED_STYLE = """
    QProgressBar{
        border: 2px solid grey;
        border-radius: 0px;
        text-align: center
    }

    QProgressBar::chunk {
        background-color: lightgreen;
        width: 10px;
        margin: 1px;
    }
    """

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.player = VideoWindow()
        self.player.resize(640, 480)
        self.player.show()

    def vectorWindow(self):
        self.V_Online = QtWidgets.QMainWindow()
        self.ui = Ui_V_Online()
        self.ui.setupUi(self.V_Online)
        self.V_Online.show()

    def setupUi(self, LUXC):
        LUXC.setObjectName("LUXC")
        LUXC.resize(800, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),"Icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LUXC.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LUXC)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.getAxis('left').setPen('white')
        self.graphicsView.getAxis('left').setTextPen('white')
        self.graphicsView.getAxis('bottom').setPen('white')
        self.graphicsView.getAxis('bottom').setTextPen('white')
        self.graphicsView.showGrid(x=True, y=True, alpha=0.3)
        self.gridLayout.addWidget(self.graphicsView, 11, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow )
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        # self.tableWidget.setGeometry(QtCore.QRect(10, 150, 680, 170))
        font = QtGui.QFont()
        font.setBold(True)
        self.tableWidget.horizontalHeader().setFont(font)
        self.tableWidget.verticalHeader().setFont(font)
        self.gridLayout.addWidget(self.tableWidget, 10, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.getbit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.getbit.setFont(font)
        self.getbit.setObjectName("getbit")
        self.horizontalLayout.addWidget(self.getbit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 1, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.logging = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.logging.setFont(font)
        self.logging.setObjectName("logging")
        self.verticalLayout_3.addWidget(self.logging)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 11, 2, 1, 3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 10, 4, 2, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet(Ui_LUXC().COMPLETED_STYLE)
        font = QtGui.QFont()
        font.setBold(True)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 2, 2, 1, 1)
        self.ZLGToV = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.ZLGToV.setFont(font)
        self.ZLGToV.setObjectName("ZLGToV")
        self.gridLayout_2.addWidget(self.ZLGToV, 0, 0, 1, 1)
        self.VideoPlayer = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.VideoPlayer.setFont(font)
        self.VideoPlayer.setObjectName("VideoPlayer")
        self.gridLayout_2.addWidget(self.VideoPlayer, 2, 0, 1, 1)
        self.LoadButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.LoadButton.setFont(font)
        self.LoadButton.setObjectName("LoadButton")
        self.gridLayout_2.addWidget(self.LoadButton, 0, 2, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.path = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.path.setFont(font)
        self.path.setObjectName("path")
        self.verticalLayout.addWidget(self.path)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 6, 0, 1, 1)
        LUXC.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LUXC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuVector = QtWidgets.QMenu(self.menubar)
        self.menuVector.setObjectName("menuVector")
        LUXC.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LUXC)
        self.statusbar.setObjectName("statusbar")
        LUXC.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(LUXC)
        self.actionOpen.setObjectName("actionOpen")
        self.actionPy_CAN = QtWidgets.QAction(LUXC)
        self.actionPy_CAN.setObjectName("actionPy_CAN")
        self.menuFile.addAction(self.actionOpen)
        self.menuVector.addAction(self.actionPy_CAN)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuVector.menuAction())


        self.retranslateUi(LUXC)
        QtCore.QMetaObject.connectSlotsByName(LUXC)


        # functions assign to items
        self.VideoPlayer.clicked.connect(lambda: self.openWindow())
        self.actionOpen.triggered.connect(lambda: self.openfile())
        self.actionPy_CAN.triggered.connect(lambda: self.vectorWindow())
        self.ZLGToV.clicked.connect(lambda: self.VECTOR_CANASC_TRANS(self.label.text()))
        self.LoadButton.clicked.connect(lambda: self.load_data())
        self.radioButton.toggled.connect(lambda: self.tablefit(self.df))
        self.comboBox.activated[str].connect(lambda: self.Messagefilter())
        self.getbit.clicked.connect(lambda: self.bitselection())
        self.logging.clicked.connect(lambda: self.logfile())
        self.comboBox_2.currentIndexChanged.connect(lambda: self.graphplot(x = self.x, y= self.value, ID = self.comboBox.currentText()))

    def retranslateUi(self, LUXC):
        _translate = QtCore.QCoreApplication.translate
        LUXC.setWindowTitle(_translate("LUXC", "CAN 2.0"))
        self.tableWidget.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        # self.tableWidget.setSortingEnabled(False)
        # self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.zero.setText(_translate("LUXC", "0"))
        self.eins.setText(_translate("LUXC", "1"))
        self.zwei.setText(_translate("LUXC", "2"))
        self.drei.setText(_translate("LUXC", "3"))
        self.vier.setText(_translate("LUXC", "4"))
        self.funf.setText(_translate("LUXC", "5"))
        self.sechs.setText(_translate("LUXC", "6"))
        self.sieben.setText(_translate("LUXC", "7"))
        self.getbit.setText(_translate("LUXC", "Go"))
        self.radioButton.setText(_translate("LUXC", "show in table"))
        self.logging.setText(_translate("LUXC", "Logging"))
        self.ZLGToV.setText(_translate("LUXC", "ZLG Transfer"))
        self.VideoPlayer.setText(_translate("LUXC", "Video Player"))
        self.LoadButton.setText(_translate("LUXC", "Load"))
        self.path.setText(_translate("LUXC", "Path:"))
        self.menuFile.setTitle(_translate("LUXC", "File"))
        self.actionOpen.setText(_translate("LUXC", "Open"))
        self.actionOpen.setShortcut(_translate("LUXC", "Ctrl+O"))
        self.actionPy_CAN.setText(_translate("LUXC", "Py CAN"))
        self.menuVector.setTitle(_translate("LUXC", "Vector"))
        self.label_2.setText(_translate("LUXC", "Plotting Style"))
        self.comboBox_2.setItemText(0, _translate("LUXC", "Style 1"))
        self.comboBox_2.setItemText(1, _translate("LUXC", "Style 2"))



    # show file path that be oppened
    def show_file_path(self, text):
        self.label.setText(text)
        self.label.adjustSize()
    # open and select asc file
    def openfile(self):
        file = QFileDialog.getOpenFileName(parent = self, caption = "Open File",directory= "", filter= "Data file (*.asc)")
        fileName, ext = file[0], file[1]
        self.show_file_path(fileName)
        print(fileName)
    # create a asc file
    def WRITE_ASC(self, w_path):
        my_date    = date.today()
        weekday    = calendar.day_name[my_date.weekday()][:3]
        month      = calendar.month_name[my_date.month][:3]
        day        = my_date.day
        timestamp  = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[11:-3]
        year       = my_date.year
        asc_write  = open(w_path, 'w')
        asc_write.write('date {} {} {} {} am {}'.format(weekday, month, day, timestamp, year) + '\n')
        asc_write.write('base hex  timestamps absolute' + '\n')
        asc_write.write('internal events logged' + '\n')
        asc_write.write('// version 15.2.0' + '\n')
        asc_write.write('// Measurement UUID: 6353be44-7a15-4a4f-9b74-67bef98c7810' + '\n'*3)
        return asc_write
    # convert ZLG to vector data format
    def VECTOR_CANASC_TRANS(self, file):
        '''
         0   timestamp  3 non-null      float64
         1   Chn        3 non-null      int64  
         2   ID         3 non-null      object 
         3   RxTx       3 non-null      object 
         4   d          3 non-null      object 
         5   len        3 non-null      int64  
         6   1          3 non-null      object 
         7   2          3 non-null      object 
         8   3          3 non-null      object 
         9   4          3 non-null      object 
         10  5          3 non-null      object 
         11  6          3 non-null      object 
         12  7          3 non-null      object 
         13  8          3 non-null      object 
        '''
        p = PureWindowsPath(file)
        print('ZLGs {} ASCII date being converted'.format(p.stem))
        # open and write ascii file
        asc_write  = self.WRITE_ASC(w_path=os.path.join(p.parents[0], p.stem + '_vector' + p.suffixes[0]))
        df         = pd.read_csv(file,engine ='python', encoding='ascii', skiprows=2, skipfooter=1,sep=' ', header = None,index_col=None).iloc[:, :-1]
        df.columns = ['timestamp', 'Chn','ID', 'RxTx', 'd', 'len', '1', '2', '3','4','5','6', '7', '8']
        for index, row in df.iterrows():
            self.ProgressBar_setVal([index, df.values.shape[0]])
            asc_write.write('{fill}{timestamp:.6f}{fill2}{Chn:<3}{ID:<16}{RxTx:<5}{D:<2}{Len:<2d}'.format(fill = ' '*3, 
                                                                                                          timestamp = row['timestamp'], 
                                                                                                          fill2 = ' ', 
                                                                                                          Chn = '1', 
                                                                                                          ID = row['ID'],
                                                                                                          RxTx = row['RxTx'],
                                                                                                          D = row['d'],
                                                                                                          Len = row['len']))
            for i in range(row['len']):
                asc_write.write('{bit:<3}'.format( bit = hex(int(row['{}'.format(i+1)], 16)).replace('0x','')))  
            asc_write.write('\n')
        asc_write.close()
        print('{} Conversion complete!'.format(p.name))

    def tablefit(self, df):
        df = self.selmsg
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setRowCount(len(df.index))
        self.tableWidget.setHorizontalHeaderLabels(list(df))
        if self.radioButton.isChecked():
            for i in range(len(df.index)):
                self.ProgressBar_setVal([i,df.values.shape[0]])
                for j in range(len(df.columns)):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(df.iloc[i,j]))

            for col in range(len(df.columns)):      
                self.tableWidget.horizontalHeader().setSectionResizeMode(col, QHeaderView.ResizeToContents)
        else:
            self.tableWidget.setRowCount(0)

    # setup value for progressBar
    def ProgressBar_setVal(self, val_list: list):
        value = round((val_list[0]+1)/val_list[1]*100)
        if value < 100:self.progressBar.setProperty("value", value)
        else: self.progressBar.setProperty("value", 0)

    # load file and write data in tabel
    def load_data(self):
        droprow = {1:'ErrorFrame', 2:'error', 3:'warning', 4:'Statistic:', 6:float(0)}
        pd.set_option('display.max_columns', None)
        dataName = self.label.text()
        self.df = pd.read_csv(dataName, engine ='python', 
                 encoding='ascii', skiprows=7,header=None, index_col=False,
                 delim_whitespace = True).iloc[:,:14].astype(str)
        # self.df = pd.read_csv(dataName, engine ='python', skiprows=7,header=None, index_col=False).astype(str)
        print(self.df.values.shape)
        # print(self.df.head(50))
        dropdf = self.df[(self.df.iloc[:,2] == droprow[1]) | (self.df.iloc[:,5] == droprow[2]) | (self.df.iloc[:,5] == droprow[3]) | (self.df.iloc[:,2] == droprow[4])].index
        self.df.drop(dropdf , inplace=True)
        self.df.dropna(axis=0,inplace = True)

        self.df.columns = ['timestamp', 'Chn','ID', 'RxTx', 'd', 'len', '0', '1', '2','3','4','5', '6', '7']
        self.comboBox.addItem("all")
        # self.tablefit(self.df)
        self.Messagefilter()
        msgID = sorted(self.df['ID'].unique())
        for i, ID in enumerate(msgID):
            self.comboBox.addItem("{}".format(ID))
        QMessageBox.information(self, "Loading",'Loading done!')

    # message ID filter 
    def Messagefilter(self):
        self.currtext = self.comboBox.currentText()
        if self.currtext == 'all':
            self.selmsg = self.df
        else:
            self.selmsg = self.df[self.df['ID'] == self.currtext]
        self.tablefit(self.selmsg)
    # change table header color
    def headercolor(self, position:int, color = QtGui.QColor(0,0,0)):
        header = self.tableWidget.horizontalHeaderItem(position)
        header.setForeground(color)
    # plot 
    def graphplot(self, x,y, ID:str):
        self.graphicsView.clear()
        pen = pg.mkPen(color=(245,223,77), width=1.5)
        if self.comboBox_2.currentText() == 'Style 2':
            self.graphicsView.plot(x, y, name = ID, pen = pen, symbol='+', symbolBrush=('b'))
        if self.comboBox_2.currentText() == 'Style 1':
            self.graphicsView.plot(x, y, name = ID, pen = pen)
        self.graphicsView.setLabel('bottom', 'Time [s]')
        self.graphicsView.addLegend()
    # select start bit and multi bytecombination and plot 
    def bitselection(self):
            checklist = [False]*8
            if self.zero.isChecked(): checklist[0]    = True
            if self.eins.isChecked(): checklist[1]    = True
            if self.zwei.isChecked(): checklist[2]    = True
            if self.drei.isChecked(): checklist[3]    = True
            if self.vier.isChecked(): checklist[4]    = True
            if self.funf.isChecked(): checklist[5]    = True
            if self.sechs.isChecked(): checklist[6]   = True
            if self.sieben.isChecked(): checklist[7]  = True
            else: checklist = checklist
            try:
                columns = np.array(list(self.df))[-8:][checklist]
                position = [int(idx) + 6 for idx in columns]
                for colposi in range(len(list(self.df))):
                    if colposi not in position:
                        self.headercolor(colposi)
                    else:
                        self.headercolor(colposi,QtGui.QColor(255,0,0))
                print(columns)
                if len(columns) != 0:
                    if self.comboBox.currentText() == 'all':
                        self.x  = self.df.timestamp.values.astype(np.float64)
                        value   = np.fliplr(self.df[columns].values)
                        value   = np.sum(value,dtype = object, axis = 1)
                        npfunc_hex_to_dec  = np.vectorize(lambda x: int(x, 16))
                        npfunc_dec_to_hex  = np.vectorize(lambda x: '{:x}'.format(x))
                        self.value   = npfunc_hex_to_dec(value)
                    else:
                        self.x  = self.df[self.df["ID"] == self.comboBox.currentText()].timestamp.values.astype(np.float64)
                        value   = np.fliplr(self.df[self.df["ID"] == self.comboBox.currentText()][columns].values)
                        value   = np.sum(value,dtype = object, axis = 1)
                        npfunc_hex_to_dec  = np.vectorize(lambda x: int(x, 16))
                        npfunc_dec_to_hex  = np.vectorize(lambda x: '{:x}'.format(x))
                        self.value   = npfunc_hex_to_dec(value)
                    self.graphplot(self.x,self.value,self.comboBox.currentText())
                else:
                    QMessageBox.warning(self, "Warning", "please select data of current message ID")
            except AttributeError:
                QMessageBox.critical(self, "Error", "please load data first")
                self.openfile()
            except OverflowError:
                QMessageBox.critical(self, "Error", "int too big to convert")

            self.plainTextEdit.appendPlainText('Message ID: {} Byte: {}'.format(self.comboBox.currentText(),columns))


    def logfile(self):
        # name = QFileDialog.getSaveFileName(self, 'Save File', filter="Dat Files (*.dat)")
        root = QFileDialog.getExistingDirectory(self, 'Select directory')
        try:
            i = 0
            while os.path.exists(root + '/' + "logging_%s.dat" % i):
                i += 1

            f = open(root + '/' + "logging_%s.dat" % i, "w")
            f.write('Data: {} Autor: {}'.format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 'XiaoChuan') + '\n')
            f.write('Attempts will be logged' + '\n')
            f.write('-'*50 + '\n')
            f.write(str(self.plainTextEdit.toPlainText()))

            f.close()
            QMessageBox.information(self, "Logging",'Save successful!')

        except:
            QMessageBox.critical(self, "Error", "Save failed!")

        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LUXC = QtWidgets.QMainWindow()
    ui = Ui_LUXC()
    ui.setupUi(LUXC)
    LUXC.show()
    sys.exit(app.exec_())
