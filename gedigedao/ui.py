# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 564)
        MainWindow.setStyleSheet("background:rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 490, 75, 23))
        self.pushButton.setStyleSheet("background:rgb(0, 0, 57);\n"
"color: rgb(177, 177, 177);")
        self.pushButton.setObjectName("pushButton")
        self.blur_btn = QtWidgets.QPushButton(self.centralwidget)
        self.blur_btn.setGeometry(QtCore.QRect(600, 490, 75, 23))
        self.blur_btn.setStyleSheet("background:rgb(0, 0, 57);\n"
"color: rgb(177, 177, 177);")
        self.blur_btn.setObjectName("blur_btn")
        self.mirror_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mirror_btn.setGeometry(QtCore.QRect(520, 490, 75, 23))
        self.mirror_btn.setStyleSheet("background:rgb(0, 0, 57);\n"
"color: rgb(177, 177, 177);")
        self.mirror_btn.setObjectName("mirror_btn")
        self.right_btn = QtWidgets.QPushButton(self.centralwidget)
        self.right_btn.setGeometry(QtCore.QRect(440, 490, 75, 23))
        self.right_btn.setStyleSheet("background:rgb(0, 0, 57);\n"
"color: rgb(177, 177, 177);")
        self.right_btn.setObjectName("right_btn")
        self.left_btn = QtWidgets.QPushButton(self.centralwidget)
        self.left_btn.setGeometry(QtCore.QRect(350, 490, 75, 23))
        self.left_btn.setStyleSheet("background:rgb(0, 0, 57);\n"
"color: rgb(177, 177, 177);")
        self.left_btn.setObjectName("left_btn")
        self.image_list = QtWidgets.QListWidget(self.centralwidget)
        self.image_list.setGeometry(QtCore.QRect(40, 70, 256, 491))
        self.image_list.setStyleSheet("background:rgb(0, 0, 57)")
        self.image_list.setObjectName("image_list")
        self.floder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.floder_btn.setGeometry(QtCore.QRect(50, 20, 75, 23))
        self.floder_btn.setStyleSheet("background: rgb(0, 0, 57);\n"
"color: rgb(177, 177, 177)")
        self.floder_btn.setObjectName("floder_btn")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(300, 40, 471, 431))
        self.image_label.setStyleSheet("color:rgb(0, 0, 0);\n"
"")
        self.image_label.setObjectName("image_label")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(160, 20, 75, 23))
        self.save_btn.setStyleSheet("background: rgb(0, 0, 57);\n"
"color: rgb(177, 177, 177)")
        self.save_btn.setObjectName("save_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Ч/Б"))
        self.blur_btn.setText(_translate("MainWindow", "Різкість"))
        self.mirror_btn.setText(_translate("MainWindow", "Дзеркало"))
        self.right_btn.setText(_translate("MainWindow", "Праворуч"))
        self.left_btn.setText(_translate("MainWindow", "Ліворуч"))
        self.floder_btn.setText(_translate("MainWindow", "папка"))
        self.image_label.setText(_translate("MainWindow", "картинка"))
        self.save_btn.setText(_translate("MainWindow", "зберегти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
