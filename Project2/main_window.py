# Form implementation generated from reading ui file 'second.ui'
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 70, 495, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_edit.setText("")
        self.line_edit.setObjectName("line_edit")
        self.horizontalLayout.addWidget(self.line_edit)
        self.combo_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.combo_box.addItem("Email")
        self.combo_box.addItem("URL")
        self.combo_box.addItem("Date")
        self.combo_box.addItem("Number")
        self.combo_box.addItem("Credit Card")
        self.combo_box.addItem("Phone Number")
        self.combo_box.setObjectName("combo_box")
        self.horizontalLayout.addWidget(self.combo_box)
        self.btn_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check.setGeometry(QtCore.QRect(387, 160, 111, 32))
        self.btn_check.setObjectName("btn_check")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Validator"))
        self.btn_check.setText(_translate("MainWindow", "Check"))
