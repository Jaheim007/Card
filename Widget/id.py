# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/idcard.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Idcard(object):
    def setupUi(self, Idcard):
        Idcard.setObjectName("Idcard")
        Idcard.resize(1228, 855)
        self.centralwidget = QtWidgets.QWidget(Idcard)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1231, 861))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(-10, 0, 1241, 911))
        self.label_7.setStyleSheet("")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/img/Static/124907004-pink-abstract-background-geometric-for-presentation-banner-poster-or-flyer-artwork-background-design.webp"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.table = QtWidgets.QTableWidget(self.page)
        self.table.setGeometry(QtCore.QRect(60, 150, 1091, 581))
        self.table.setAutoScroll(True)
        self.table.setAlternatingRowColors(False)
        self.table.setShowGrid(True)
        self.table.setGridStyle(QtCore.Qt.DashLine)
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.table.horizontalHeader().setDefaultSectionSize(215)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(60, 70, 471, 71))
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.search_btn = QtWidgets.QPushButton(self.page)
        self.search_btn.setGeometry(QtCore.QRect(970, 80, 161, 41))
        self.search_btn.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:rgb(50, 121, 234);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 121, 234);\n"
"}")
        self.search_btn.setAutoDefault(True)
        self.search_btn.setDefault(True)
        self.search_btn.setFlat(False)
        self.search_btn.setObjectName("search_btn")
        self.refresh_btn = QtWidgets.QPushButton(self.page)
        self.refresh_btn.setGeometry(QtCore.QRect(990, 760, 161, 41))
        self.refresh_btn.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:rgb(50, 121, 234);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 121, 234);\n"
"}")
        self.refresh_btn.setAutoDefault(True)
        self.refresh_btn.setDefault(True)
        self.refresh_btn.setFlat(False)
        self.refresh_btn.setObjectName("refresh_btn")
        self.search_line = QtWidgets.QLineEdit(self.page)
        self.search_line.setGeometry(QtCore.QRect(730, 80, 231, 41))
        self.search_line.setObjectName("search_line")
        self.take_screen = QtWidgets.QPushButton(self.page)
        self.take_screen.setGeometry(QtCore.QRect(720, 760, 261, 41))
        self.take_screen.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:rgb(50, 121, 234);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 121, 234);\n"
"}")
        self.take_screen.setAutoDefault(True)
        self.take_screen.setDefault(True)
        self.take_screen.setFlat(False)
        self.take_screen.setObjectName("take_screen")
        self.save_page = QtWidgets.QPushButton(self.page)
        self.save_page.setGeometry(QtCore.QRect(470, 760, 231, 41))
        self.save_page.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:rgb(50, 121, 234);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 121, 234);\n"
"}")
        self.save_page.setAutoDefault(True)
        self.save_page.setDefault(True)
        self.save_page.setFlat(False)
        self.save_page.setObjectName("save_page")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(-10, -10, 1241, 871))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/img/Static/job545-wit-56_1_1.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.frame_3 = QtWidgets.QFrame(self.page_3)
        self.frame_3.setGeometry(QtCore.QRect(300, 180, 701, 371))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(460, 30, 201, 191))
        self.label_9.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label_9.setObjectName("label_9")
        self.prenom_label = QtWidgets.QLabel(self.frame_3)
        self.prenom_label.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.prenom_label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.prenom_label.setObjectName("prenom_label")
        self.nom_label = QtWidgets.QLabel(self.frame_3)
        self.nom_label.setGeometry(QtCore.QRect(20, 80, 71, 31))
        self.nom_label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.nom_label.setObjectName("nom_label")
        self.sexe_label = QtWidgets.QLabel(self.frame_3)
        self.sexe_label.setGeometry(QtCore.QRect(20, 150, 81, 31))
        self.sexe_label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.sexe_label.setObjectName("sexe_label")
        self.date_de_label = QtWidgets.QLabel(self.frame_3)
        self.date_de_label.setGeometry(QtCore.QRect(20, 220, 201, 31))
        self.date_de_label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.date_de_label.setObjectName("date_de_label")
        self.show_prenom = QtWidgets.QLabel(self.frame_3)
        self.show_prenom.setGeometry(QtCore.QRect(120, 40, 231, 31))
        self.show_prenom.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.show_prenom.setText("")
        self.show_prenom.setObjectName("show_prenom")
        self.show_nom = QtWidgets.QLabel(self.frame_3)
        self.show_nom.setGeometry(QtCore.QRect(90, 100, 201, 31))
        self.show_nom.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.show_nom.setText("")
        self.show_nom.setObjectName("show_nom")
        self.show_sexe = QtWidgets.QLabel(self.frame_3)
        self.show_sexe.setGeometry(QtCore.QRect(90, 160, 151, 31))
        self.show_sexe.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.show_sexe.setText("")
        self.show_sexe.setObjectName("show_sexe")
        self.show_date = QtWidgets.QLabel(self.frame_3)
        self.show_date.setGeometry(QtCore.QRect(230, 220, 251, 31))
        self.show_date.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.show_date.setText("")
        self.show_date.setObjectName("show_date")
        self.date_de_label_2 = QtWidgets.QLabel(self.frame_3)
        self.date_de_label_2.setGeometry(QtCore.QRect(20, 290, 61, 31))
        self.date_de_label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.date_de_label_2.setObjectName("date_de_label_2")
        self.capture = QtWidgets.QPushButton(self.page_3)
        self.capture.setGeometry(QtCore.QRect(480, 600, 271, 61))
        self.capture.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:rgb(50, 121, 234);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 121, 234);\n"
"}")
        self.capture.setObjectName("capture")
        self.back_btn_2 = QtWidgets.QPushButton(self.page_3)
        self.back_btn_2.setGeometry(QtCore.QRect(30, 20, 131, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Static/left_32px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn_2.setIcon(icon)
        self.back_btn_2.setIconSize(QtCore.QSize(100, 100))
        self.back_btn_2.setDefault(False)
        self.back_btn_2.setFlat(False)
        self.back_btn_2.setObjectName("back_btn_2")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(-10, -50, 1241, 911))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/Static/rm222-mind-22_1_2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(320, 20, 611, 831))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 331, 71))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 91, 71))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 340, 91, 41))
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 430, 81, 51))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 510, 281, 71))
        self.label_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.prenom_line = QtWidgets.QLineEdit(self.frame)
        self.prenom_line.setGeometry(QtCore.QRect(40, 290, 511, 41))
        self.prenom_line.setObjectName("prenom_line")
        self.nom_line = QtWidgets.QLineEdit(self.frame)
        self.nom_line.setGeometry(QtCore.QRect(40, 380, 511, 41))
        self.nom_line.setObjectName("nom_line")
        self.register_btn = QtWidgets.QPushButton(self.frame)
        self.register_btn.setGeometry(QtCore.QRect(200, 770, 171, 51))
        self.register_btn.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:rgb(50, 121, 234);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 121, 234);\n"
"}")
        self.register_btn.setAutoDefault(True)
        self.register_btn.setDefault(True)
        self.register_btn.setFlat(False)
        self.register_btn.setObjectName("register_btn")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(40, 480, 511, 41))
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dateEdit_combo = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_combo.setGeometry(QtCore.QRect(40, 570, 511, 41))
        self.dateEdit_combo.setObjectName("dateEdit_combo")
        self.add_photo_btn = QtWidgets.QPushButton(self.frame)
        self.add_photo_btn.setGeometry(QtCore.QRect(280, 130, 171, 51))
        self.add_photo_btn.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:rgb(50, 121, 234);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 121, 234);\n"
"}")
        self.add_photo_btn.setObjectName("add_photo_btn")
        self.add_photo = QtWidgets.QLabel(self.frame)
        self.add_photo.setGeometry(QtCore.QRect(60, 80, 151, 141))
        self.add_photo.setStyleSheet("image: url(:/img/Static/images (1).png);\n"
"border: 2px solid black;")
        self.add_photo.setText("")
        self.add_photo.setScaledContents(False)
        self.add_photo.setObjectName("add_photo")
        self.error = QtWidgets.QLabel(self.frame)
        self.error.setGeometry(QtCore.QRect(40, 710, 491, 41))
        self.error.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.error.setText("")
        self.error.setObjectName("error")
        self.email_line = QtWidgets.QLineEdit(self.frame)
        self.email_line.setGeometry(QtCore.QRect(40, 660, 511, 41))
        self.email_line.setObjectName("email_line")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(40, 620, 91, 41))
        self.label_10.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.page_2)
        Idcard.setCentralWidget(self.centralwidget)

        self.retranslateUi(Idcard)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Idcard)

    def retranslateUi(self, Idcard):
        _translate = QtCore.QCoreApplication.translate
        Idcard.setWindowTitle(_translate("Idcard", "MainWindow"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Idcard", "Prenom"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Idcard", "Nom"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Idcard", "Sexe"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Idcard", "Date de naissance"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("Idcard", "Email"))
        self.label_14.setText(_translate("Idcard", "<html><head/><body><p><span style=\" font-size:24pt; text-decoration: underline;\">Recherche par pr??nom</span></p></body></html>"))
        self.search_btn.setText(_translate("Idcard", "Search"))
        self.refresh_btn.setText(_translate("Idcard", "Refresh"))
        self.take_screen.setText(_translate("Idcard", "Prendre une capture d\'??cran"))
        self.save_page.setText(_translate("Idcard", "Enregister une personne"))
        self.label_9.setText(_translate("Idcard", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Profile img</span></p></body></html>"))
        self.prenom_label.setText(_translate("Idcard", "Prenom :"))
        self.nom_label.setText(_translate("Idcard", "Nom :"))
        self.sexe_label.setText(_translate("Idcard", "Sexe :"))
        self.date_de_label.setText(_translate("Idcard", "Date de naissance :"))
        self.date_de_label_2.setText(_translate("Idcard", "Email:"))
        self.capture.setText(_translate("Idcard", "Capture d\'ecran"))
        self.back_btn_2.setText(_translate("Idcard", "Back"))
        self.label_2.setText(_translate("Idcard", "<html><head/><body><p align=\"center\">Carte d\'identit??</p></body></html>"))
        self.label_3.setText(_translate("Idcard", "<html><head/><body><p>Prenom</p></body></html>"))
        self.label_4.setText(_translate("Idcard", "<html><head/><body><p>Nom</p></body></html>"))
        self.label_5.setText(_translate("Idcard", "<html><head/><body><p>Sexe</p></body></html>"))
        self.label_6.setText(_translate("Idcard", "<html><head/><body><p>Date de naissance</p></body></html>"))
        self.register_btn.setText(_translate("Idcard", "Enregister"))
        self.comboBox.setCurrentText(_translate("Idcard", "Masculin"))
        self.comboBox.setItemText(0, _translate("Idcard", "Masculin"))
        self.comboBox.setItemText(1, _translate("Idcard", "Feminin"))
        self.add_photo_btn.setText(_translate("Idcard", "Add Photo"))
        self.label_10.setText(_translate("Idcard", "<html><head/><body><p>Email</p></body></html>"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Idcard = QtWidgets.QMainWindow()
    ui = Ui_Idcard()
    ui.setupUi(Idcard)
    Idcard.show()
    sys.exit(app.exec_())
