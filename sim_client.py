# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sim_client.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 251)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sim_uuid_le = QtWidgets.QLineEdit(self.centralwidget)
        self.sim_uuid_le.setObjectName("sim_uuid_le")
        self.horizontalLayout.addWidget(self.sim_uuid_le)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.mavlink1_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.mavlink1_ip.setObjectName("mavlink1_ip")
        self.horizontalLayout_2.addWidget(self.mavlink1_ip)
        self.mavlink1_port_le = QtWidgets.QLineEdit(self.centralwidget)
        self.mavlink1_port_le.setMaximumSize(QtCore.QSize(100, 16777215))
        self.mavlink1_port_le.setObjectName("mavlink1_port_le")
        self.horizontalLayout_2.addWidget(self.mavlink1_port_le)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.mavlink2_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.mavlink2_ip.setObjectName("mavlink2_ip")
        self.horizontalLayout_4.addWidget(self.mavlink2_ip)
        self.mavlink2_port_le = QtWidgets.QLineEdit(self.centralwidget)
        self.mavlink2_port_le.setMaximumSize(QtCore.QSize(100, 16777215))
        self.mavlink2_port_le.setObjectName("mavlink2_port_le")
        self.horizontalLayout_4.addWidget(self.mavlink2_port_le)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.mavlink3_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.mavlink3_ip.setObjectName("mavlink3_ip")
        self.horizontalLayout_5.addWidget(self.mavlink3_ip)
        self.mavlink3_port_le = QtWidgets.QLineEdit(self.centralwidget)
        self.mavlink3_port_le.setMaximumSize(QtCore.QSize(100, 16777215))
        self.mavlink3_port_le.setObjectName("mavlink3_port_le")
        self.horizontalLayout_5.addWidget(self.mavlink3_port_le)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.connect_pb = QtWidgets.QPushButton(self.centralwidget)
        self.connect_pb.setObjectName("connect_pb")
        self.horizontalLayout_3.addWidget(self.connect_pb)
        self.disconnect_pb = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_pb.setObjectName("disconnect_pb")
        self.horizontalLayout_3.addWidget(self.disconnect_pb)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 22))
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
        self.label.setText(_translate("MainWindow", "Simulation UUID"))
        self.label_2.setText(_translate("MainWindow", "mavlink1 out"))
        self.mavlink1_ip.setText(_translate("MainWindow", "127.0.0.1"))
        self.mavlink1_port_le.setText(_translate("MainWindow", "14550"))
        self.label_3.setText(_translate("MainWindow", "mavlink2 out"))
        self.mavlink2_ip.setText(_translate("MainWindow", "127.0.0.1"))
        self.mavlink2_port_le.setText(_translate("MainWindow", "14551"))
        self.label_4.setText(_translate("MainWindow", "mavlink3 out"))
        self.mavlink3_ip.setText(_translate("MainWindow", "127.0.0.1"))
        self.mavlink3_port_le.setText(_translate("MainWindow", "14552"))
        self.connect_pb.setText(_translate("MainWindow", "Connect"))
        self.disconnect_pb.setText(_translate("MainWindow", "disconnect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
