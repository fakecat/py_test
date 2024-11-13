import sys, os, math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QHBoxLayout, QFileDialog, QAction, QScrollArea, QTextBrowser, QInputDialog, QLineEdit, QHeaderView
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from subprocess import Popen, PIPE
from Ui_smartTJgit import Ui_MainWindow

def setUiStatusBarText(path):
    os.chdir(path)
    print(f"Selected folder: {path}")
    process = Popen('git branch -a', shell=True, stdout=PIPE, stderr=PIPE, text=True)
    stdout, stderr = process.communicate()
    lineOne = display_first_line(stdout)
    print(f"branch1: {lineOne}")
    ui.statusBar.showMessage(path + "   , branch : " + lineOne)
    return

def display_first_line(text):
    lines = text.split('\n')
    return lines[0] if lines else ''

def traverse_directory(folder_path, folder_name):
    top_item = QStandardItem(folder_name)
    dir = QDir(folder_path)
    file_list = dir.entryInfoList([])
    for file in file_list:
        file_item = QStandardItem(file.fileName())
        if file.isDir():
            traverse_directory(file.dir(), top_item)
        else:
            child_item = QStandardItem(f"{file}")
            top_item.appendRow(child_item)
    return top_item

def funcExecuteCommand():
    text, ok = QInputDialog.getText(None, 'Execute Command', 'Input Command:', QLineEdit.Normal, "")
    if ok:
        funcShowMessageBox(text, 'Execute Command')

def funcShowMessageBox(command, mess_title):
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    stdout, stderr = process.communicate()
    if stderr:
        QMessageBox.information(None, mess_title, stderr)
    else:
        QMessageBox.information(None, mess_title, stdout)

def funcGitConfig():
    funcShowMessageBox('git config -l', 'Git Config')

def funcNew():
    folder_path = QFileDialog.getExistingDirectory(None, "Open Folder", "C:\\tj\\work_code\\aa")
    if folder_path:
        print(f"Selected folder: {folder_path}")
    else:
        return
    if not os.listdir(folder_path):
        QMessageBox.information(None, 'SUCCESS', 'Select an empty folder for a new git repository.')
        os.chdir(folder_path)
        ui.statusBar.showMessage(folder_path)
        Dialog_title = "Git Repository"
        Dialog_lable = "remote url"
        text, ok = QInputDialog.getText(None, Dialog_title, Dialog_lable, QLineEdit.Normal, "")
        if ok:
            print(f"remote url: {text}")
            Dialog_git_title = "Fetch"
            process = Popen(text, shell=True, stdout=PIPE, stderr=PIPE, text=True)
            stdout, stderr = process.communicate()
            if stderr:
                QMessageBox.information(None, Dialog_git_title, stderr)
                files_and_directories = os.listdir('.')
                if len(files_and_directories) > 1:
                    print(f"dirs is bigger than 1")
                    return
                if len(files_and_directories) == 0:
                    print(f"dirs equal with 0")
                    return
                for item in files_and_directories:
                    setUiStatusBarText(folder_path + "\\" + item)
            else:
                QMessageBox.information(None, Dialog_git_title, stdout)
        else:
            QMessageBox.information(None, 'ERROR', 'This folder is not empty path.')

def funcOpenFolder():
    folder_path = QFileDialog.getExistingDirectory(None, "Open Folder", "C:\\tj\\work_code\\ccs20\\ccs20")
    if folder_path:
        print(f"Selected folder: {folder_path}")
    if os.path.exists(os.path.join(folder_path, '.git')):
        QMessageBox.information(None, 'SUCCESS', 'Add one git repository.')
        ui.statusBar.showMessage(folder_path)
    else:
        QMessageBox.information(None, 'ERROR', 'This folder is not a git repository.')
        return
    dir = QDir(folder_path)
    file_list = dir.entryList()
    # print(len(file_list))
    # for file in file_list:
    #     print(file)
    gitTree = ui.gitTree
    model = QStandardItemModel()
    folder_name = folder_path.split('/')[-1]
    top_item = QStandardItem(folder_name)
    for file in file_list:
        if file == ".":
            continue
        if file == "..":
            continue
        if QFileInfo(folder_path + f"/{file}").isDir:
            top_item.appendRow(traverse_directory(folder_path + f"/{file}", file))
    #     child_item = QStandardItem(f"{file}")
    #     top_item.appendRow(child_item)
    model.appendRow(top_item)
    # model = traverse_directory(folder_path, top_item)
    gitTree.setModel(model)
    gitTree.header().setVisible(False)
    gitTree.setVerticalScrollBarPolicy(0)
    gitTree.setVerticalScrollBar(ui.gitTreeVerticalScrollBar)
    gitTree.setHorizontalScrollBarPolicy(0)
    gitTree.setHorizontalScrollBar(ui.gitTreeHorizontalScrollBar)
    gitTree.itemDelegateForRow(0)

def funcExit():
    print(f"exit...")
    quit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('./bg01.jpeg'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setMinimumSize(800, 616)
    MainWindow.setMaximumSize(800, 616)
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QColor(255, 255, 255)))
    MainWindow.setPalette(palette)
    ui.actionExit.triggered.connect(funcExit)
    ui.actionOpen_Git_Repository.triggered.connect(funcOpenFolder)
    ui.actionNew.triggered.connect(funcNew)
    ui.actionGit_Config.triggered.connect(funcGitConfig)
    MainWindow.show()
    sys.exit(app.exec_())