from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LA_god = QtWidgets.QLabel(self.centralwidget)
        self.LA_god.setGeometry(QtCore.QRect(270, 10, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LA_god.setFont(font)
        self.LA_god.setAlignment(QtCore.Qt.AlignCenter)
        self.LA_god.setObjectName("LA_god")
        self.BU_delete = QtWidgets.QPushButton(self.centralwidget)
        self.BU_delete.setGeometry(QtCore.QRect(620, 200, 151, 61))
        self.BU_delete.setObjectName("BU_delete")
        self.BU_create = QtWidgets.QPushButton(self.centralwidget)
        self.BU_create.setGeometry(QtCore.QRect(320, 200, 151, 61))
        self.BU_create.setAutoFillBackground(False)
        self.BU_create.setObjectName("BU_create")
        self.BU_edit = QtWidgets.QPushButton(self.centralwidget)
        self.BU_edit.setGeometry(QtCore.QRect(20, 200, 151, 61))
        self.BU_edit.setObjectName("BU_edit")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(270, 320, 256, 192))
        self.listView.setObjectName("listView")
        self.LA_text_list = QtWidgets.QLabel(self.centralwidget)
        self.LA_text_list.setGeometry(QtCore.QRect(360, 300, 67, 17))
        self.LA_text_list.setObjectName("LA_text_list")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.LA_god.setText(_translate("mainWindow", "GOD DAMN IT"))
        self.BU_delete.setText(_translate("mainWindow", "DELETE"))
        self.BU_create.setText(_translate("mainWindow", "CREATE"))
        self.BU_edit.setText(_translate("mainWindow", "EDIT"))
        self.LA_text_list.setText(_translate("mainWindow", "TEXT LIST"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())