import sys, os, math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenu, QApplication, QWidget, QMessageBox, QHBoxLayout, QFileDialog, QAction, QScrollArea, QTextBrowser, QInputDialog, QLineEdit, QHeaderView
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

def add_items_from_folder(path, parent_item):
    hidden_dirs = []
    hidden_files = []
    dirs = []
    files = []

    for entry in os.scandir(path):
        if entry.name.startswith('.'):
            if entry.is_dir():
                hidden_dirs.append(entry)
            elif entry.is_file():
                hidden_files.append(entry)
        else:
            if entry.is_dir():
                dirs.append(entry)
            elif entry.is_file():
                files.append(entry)

    hidden_dirs = sorted(hidden_dirs, key=lambda x: x.name.lower())
    dirs = sorted(dirs, key=lambda x: x.name.lower())

    hidden_files = sorted(hidden_files, key=lambda x: x.name.lower())
    files = sorted(files, key=lambda x: x.name.lower())

    for hidden_dir in hidden_dirs:
        hidden_dir_item = QStandardItem(hidden_dir.name)
        hidden_dir_item.setEditable(False)
        parent_item.appendRow(hidden_dir_item)
        add_items_from_folder(hidden_dir.path, hidden_dir_item)

    for hidden_file in hidden_files:
        hidden_file_item = QStandardItem(hidden_file.name)
        hidden_file_item.setEditable(False)
        parent_item.appendRow(hidden_file_item)

    for dir_entry in dirs:
        dir_item = QStandardItem(dir_entry.name)
        dir_item.setEditable(False)
        parent_item.appendRow(dir_item)
        add_items_from_folder(dir_entry.path, dir_item)

    for file_entry in files:
        file_item = QStandardItem(file_entry.name)
        file_item.setEditable(False)
        parent_item.appendRow(file_item)

def show_context_menu(pos, tree, model):
    index = tree.indexAt(pos)
    item = model.itemFromIndex(index)

    context_menu = QMenu()

    if item:
        if item.hasChildren():
            open_action = QAction("Open Folder", tree)
            open_action.triggered.connect(lambda: open_folder_action(item))
            context_menu.addAction(open_action)
        else:
            edit_action = QAction("Edit File", tree)
            edit_action.triggered.connect(lambda: edit_file_action(item))
            context_menu.addAction(edit_action)

        view_history_action = QAction("View Commit History", tree)
        view_history_action.triggered.connect(lambda: view_commit_history_action(item))
        context_menu.addAction(view_history_action)

        delete_action = QAction("Delete", tree)
        delete_action.triggered.connect(lambda: delete_item_action(item))
        context_menu.addAction(delete_action)

    context_menu.exec_(tree.mapToGlobal(pos))

def open_folder_action(item):
    print(f"Opening folder: {item.text()}")

def edit_file_action(item):
    print(f"Editing file: {item.text()}")

def view_commit_history_action(item):
    print(f"Viewing commit history for: {item.text()}")

def delete_item_action(item):
    print(f"Deleting item: {item.text()}")
    parent = item.parent()
    if parent:
        reply = QMessageBox.question(None, 'Confirm Delete', f"Are you sure you want to delete '{item.text()}'?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            parent.removeRow(item.row())
            QMessageBox.information(None, 'Success', f"'{item.text()}' has been deleted.")

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
    gitTree = ui.gitTree
    model = QStandardItemModel()
    folder_name = folder_path.split('/')[-1]
    print(f"folder_name : {folder_name}")
    top_item = QStandardItem(folder_name)
    top_item.setEditable(False)
    add_items_from_folder(folder_path, top_item)
    model.appendRow(top_item)
    gitTree.setModel(model)
    gitTree.header().setVisible(False)
    gitTree.setVerticalScrollBarPolicy(0)
    gitTree.setVerticalScrollBar(ui.gitTreeVerticalScrollBar)
    gitTree.setHorizontalScrollBarPolicy(0)
    gitTree.setHorizontalScrollBar(ui.gitTreeHorizontalScrollBar)
    gitTree.itemDelegateForRow(0)
    gitTree.setContextMenuPolicy(Qt.CustomContextMenu)
    gitTree.customContextMenuRequested.connect(lambda pos: show_context_menu(pos, gitTree, model))

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