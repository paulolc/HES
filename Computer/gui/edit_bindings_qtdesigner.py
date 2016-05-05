# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/edit_bindings_qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 348)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(732, 348))
        MainWindow.setMaximumSize(QtCore.QSize(732, 348))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("image: url(:/background/HES_front.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_profile = QtWidgets.QComboBox(self.centralwidget)
        self.input_profile.setGeometry(QtCore.QRect(40, 20, 161, 21))
        self.input_profile.setObjectName("input_profile")
        self.action_save_new_profile = QtWidgets.QPushButton(self.centralwidget)
        self.action_save_new_profile.setGeometry(QtCore.QRect(630, 20, 75, 23))
        self.action_save_new_profile.setObjectName("action_save_new_profile")
        self.action_delete_profile = QtWidgets.QPushButton(self.centralwidget)
        self.action_delete_profile.setGeometry(QtCore.QRect(210, 20, 75, 23))
        self.action_delete_profile.setObjectName("action_delete_profile")
        self.input_new_profile_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_new_profile_name.setGeometry(QtCore.QRect(470, 20, 151, 20))
        self.input_new_profile_name.setObjectName("input_new_profile_name")
        self.input_key_choice = QtWidgets.QComboBox(self.centralwidget)
        self.input_key_choice.setGeometry(QtCore.QRect(260, 100, 101, 21))
        self.input_key_choice.setMaxVisibleItems(50)
        self.input_key_choice.setObjectName("input_key_choice")
        self.action_change_binding = QtWidgets.QPushButton(self.centralwidget)
        self.action_change_binding.setGeometry(QtCore.QRect(370, 100, 41, 23))
        self.action_change_binding.setObjectName("action_change_binding")
        self.action_cancel_binding = QtWidgets.QPushButton(self.centralwidget)
        self.action_cancel_binding.setGeometry(QtCore.QRect(420, 100, 51, 23))
        self.action_cancel_binding.setObjectName("action_cancel_binding")
        self.up = QtWidgets.QPushButton(self.centralwidget)
        self.up.setGeometry(QtCore.QRect(120, 110, 41, 41))
        self.up.setText("")
        self.up.setObjectName("up")
        self.controller_buttons = QtWidgets.QButtonGroup(MainWindow)
        self.controller_buttons.setObjectName("controller_buttons")
        self.controller_buttons.addButton(self.up)
        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(70, 160, 41, 41))
        self.left.setText("")
        self.left.setObjectName("left")
        self.controller_buttons.addButton(self.left)
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(170, 160, 41, 41))
        self.right.setText("")
        self.right.setObjectName("right")
        self.controller_buttons.addButton(self.right)
        self.down = QtWidgets.QPushButton(self.centralwidget)
        self.down.setGeometry(QtCore.QRect(120, 200, 41, 41))
        self.down.setText("")
        self.down.setObjectName("down")
        self.controller_buttons.addButton(self.down)
        self.b = QtWidgets.QPushButton(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(520, 200, 41, 41))
        self.b.setText("")
        self.b.setObjectName("b")
        self.controller_buttons.addButton(self.b)
        self.a = QtWidgets.QPushButton(self.centralwidget)
        self.a.setGeometry(QtCore.QRect(610, 200, 41, 41))
        self.a.setText("")
        self.a.setObjectName("a")
        self.controller_buttons.addButton(self.a)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(390, 220, 61, 21))
        self.start.setText("")
        self.start.setObjectName("start")
        self.controller_buttons.addButton(self.start)
        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(280, 220, 61, 21))
        self.select.setText("")
        self.select.setObjectName("select")
        self.controller_buttons.addButton(self.select)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.action_save_new_profile.setText(_translate("MainWindow", "Create new"))
        self.action_delete_profile.setText(_translate("MainWindow", "Delete"))
        self.action_change_binding.setText(_translate("MainWindow", "Ok"))
        self.action_cancel_binding.setText(_translate("MainWindow", "Cancel"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

