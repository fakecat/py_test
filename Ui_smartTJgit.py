# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\tj\work_code\PyQt\smartTJgit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gitTree = QtWidgets.QTreeView(self.centralwidget)
        self.gitTree.setGeometry(QtCore.QRect(0, 0, 221, 561))
        self.gitTree.setObjectName("gitTree")
        self.commitMsg = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.commitMsg.setGeometry(QtCore.QRect(530, 0, 271, 151))
        self.commitMsg.setObjectName("commitMsg")
        self.workTree = QtWidgets.QTextBrowser(self.centralwidget)
        self.workTree.setGeometry(QtCore.QRect(220, 0, 311, 341))
        self.workTree.setObjectName("workTree")
        self.showDiff = QtWidgets.QTextBrowser(self.centralwidget)
        self.showDiff.setGeometry(QtCore.QRect(220, 340, 581, 221))
        self.showDiff.setObjectName("showDiff")
        self.gitTreeHorizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.gitTreeHorizontalScrollBar.setGeometry(QtCore.QRect(10, 540, 191, 20))
        self.gitTreeHorizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.gitTreeHorizontalScrollBar.setObjectName("gitTreeHorizontalScrollBar")
        self.gitTreeVerticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.gitTreeVerticalScrollBar.setGeometry(QtCore.QRect(200, 10, 20, 531))
        self.gitTreeVerticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.gitTreeVerticalScrollBar.setObjectName("gitTreeVerticalScrollBar")
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_2.setGeometry(QtCore.QRect(230, 320, 281, 20))
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(510, 10, 20, 311))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.horizontalScrollBar_3 = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_3.setGeometry(QtCore.QRect(230, 540, 551, 20))
        self.horizontalScrollBar_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_3.setObjectName("horizontalScrollBar_3")
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar_3.setGeometry(QtCore.QRect(780, 350, 20, 191))
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.horizontalScrollBar_4 = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_4.setGeometry(QtCore.QRect(540, 130, 241, 20))
        self.horizontalScrollBar_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_4.setObjectName("horizontalScrollBar_4")
        self.verticalScrollBar_4 = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar_4.setGeometry(QtCore.QRect(780, 10, 20, 121))
        self.verticalScrollBar_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_4.setObjectName("verticalScrollBar_4")
        self.addMsg = QtWidgets.QPushButton(self.centralwidget)
        self.addMsg.setGeometry(QtCore.QRect(530, 150, 271, 28))
        self.addMsg.setObjectName("addMsg")
        self.gitLogMsg = QtWidgets.QTextBrowser(self.centralwidget)
        self.gitLogMsg.setGeometry(QtCore.QRect(530, 180, 271, 161))
        self.gitLogMsg.setObjectName("gitLogMsg")
        self.horizontalScrollBar_5 = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_5.setGeometry(QtCore.QRect(540, 320, 241, 20))
        self.horizontalScrollBar_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_5.setObjectName("horizontalScrollBar_5")
        self.verticalScrollBar_5 = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar_5.setGeometry(QtCore.QRect(780, 190, 20, 131))
        self.verticalScrollBar_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_5.setObjectName("verticalScrollBar_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        self.menuCode = QtWidgets.QMenu(self.menubar)
        self.menuCode.setObjectName("menuCode")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen_Git_Repository = QtWidgets.QAction(MainWindow)
        self.actionOpen_Git_Repository.setObjectName("actionOpen_Git_Repository")
        self.actionGit_Config = QtWidgets.QAction(MainWindow)
        self.actionGit_Config.setObjectName("actionGit_Config")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExecute_Command = QtWidgets.QAction(MainWindow)
        self.actionExecute_Command.setObjectName("actionExecute_Command")
        self.actionPull = QtWidgets.QAction(MainWindow)
        self.actionPull.setObjectName("actionPull")
        self.actionPush = QtWidgets.QAction(MainWindow)
        self.actionPush.setObjectName("actionPush")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen_Git_Repository)
        self.menuFile.addAction(self.actionGit_Config)
        self.menuFile.addAction(self.actionExecute_Command)
        self.menuExit.addAction(self.actionExit)
        self.menuCode.addAction(self.actionPull)
        self.menuCode.addAction(self.actionPush)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCode.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addMsg.setText(_translate("MainWindow", "Push"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.menuCode.setTitle(_translate("MainWindow", "Code"))
        self.actionNew.setText(_translate("MainWindow", "New Git Repository"))
        self.actionOpen_Git_Repository.setText(_translate("MainWindow", "Open Git Repository"))
        self.actionGit_Config.setText(_translate("MainWindow", "Git Config"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExecute_Command.setText(_translate("MainWindow", "Execute Command"))
        self.actionPull.setText(_translate("MainWindow", "Pull"))
        self.actionPush.setText(_translate("MainWindow", "Push"))
