# INSTRUCTIONS: Drag folder to "C:\Program Files\

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class UI_MainWindow(object):

    def setupUI(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)

        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        self.whiteBG = QtWidgets.QLabel(Form)
        self.whiteBG.setScaledContents(True)
        self.whiteBG.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.whiteBG.setText("")
        self.whiteBG.setPixmap(QtGui.QPixmap("C:/Users/618984/OneDrive - TGS Kew/Michael Wu/2023/Programming/synergeticv2/synergetic/img/white.jpg"))
        self.whiteBG.setObjectName("whiteBG")

        self.SynergeticLogo = QtWidgets.QLabel(Form)
        self.SynergeticLogo.setScaledContents(True)
        self.SynergeticLogo.setGeometry(QtCore.QRect(25, 25, 400, 63))
        self.SynergeticLogo.setText("")
        self.SynergeticLogo.setPixmap(QtGui.QPixmap("C:/Users/618984/OneDrive - TGS Kew/Michael Wu/2023/Programming/synergeticv2/synergetic/img/synergeticlogo.jpg"))
        self.SynergeticLogo.setObjectName("SynergeticLogo")

        self.LoginText = QtWidgets.QLabel(Form)
        self.LoginText.setText("Logged in as TGSADMIN")
        self.LoginText.setFont(font)
        self.LoginText.setGeometry(QtCore.QRect(1460, 25, 450, 50))
        self.LoginText.setObjectName("LoginText")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def mainMenu(self, Form):
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        startL = 150
        dist = 440
        row1Y = 250

        self.ClassesLogo = QtWidgets.QLabel(Form)
        self.ClassesLogo.setScaledContents(True)
        self.ClassesLogo.setGeometry(QtCore.QRect(startL, row1Y, 250, 250))
        self.ClassesLogo.setText("")
        self.ClassesLogo.setPixmap(QtGui.QPixmap("C:/Users/618984/OneDrive - TGS Kew/Michael Wu/2023/Programming/synergeticv2/synergetic/img/classeslogo.png"))
        self.ClassesLogo.setObjectName("ClassesLogo")
        self.ClassesLogoText = QtWidgets.QLabel(Form)
        self.ClassesLogoText.setText("View Classes")
        self.ClassesLogoText.setFont(font)
        self.ClassesLogoText.setGeometry(QtCore.QRect(startL + 10, row1Y+170, 250, 250))
        self.ClassesLogoText.setObjectName("ClassesLogoText")

        self.CalendarLogo = QtWidgets.QLabel(Form)
        self.CalendarLogo.setScaledContents(True)
        self.CalendarLogo.setGeometry(QtCore.QRect(startL + (1 * dist), row1Y, 250, 250))
        self.CalendarLogo.setText("")
        self.CalendarLogo.setPixmap(QtGui.QPixmap("C:/Users/618984/OneDrive - TGS Kew/Michael Wu/2023/Programming/synergeticv2/synergetic/img/calendarlogo.png"))
        self.CalendarLogo.setObjectName("CalenderLogo")
        self.CalendarLogoText = QtWidgets.QLabel(Form)
        self.CalendarLogoText.setText("View Calendar")
        self.CalendarLogoText.setFont(font)
        self.CalendarLogoText.setGeometry(QtCore.QRect(startL + (1 * dist), row1Y + 170, 250, 250))
        self.CalendarLogoText.setObjectName("CalenderLogoText")

        self.ViewGradesLogo = QtWidgets.QLabel(Form)
        self.ViewGradesLogo.setScaledContents(True)
        self.ViewGradesLogo.setGeometry(QtCore.QRect(startL + (2 * dist), row1Y, 250, 250))
        self.ViewGradesLogo.setText("")
        self.ViewGradesLogo.setPixmap(QtGui.QPixmap("C:/Users/618984/OneDrive - TGS Kew/Michael Wu/2023/Programming/synergeticv2/synergetic/img/viewgrades.png"))
        self.ViewGradesLogo.setObjectName("ViewGradesLogo")
        self.ViewGradesText = QtWidgets.QLabel(Form)
        self.ViewGradesText.setText("View Grades")
        self.ViewGradesText.setFont(font)
        self.ViewGradesText.setGeometry(QtCore.QRect(startL + (2 * dist) + 15, row1Y + 170, 250, 250))
        self.ViewGradesText.setObjectName("ViewGradesText")

        self.TimetableLogo = QtWidgets.QLabel(Form)
        self.TimetableLogo.setScaledContents(True)
        self.TimetableLogo.setGeometry(QtCore.QRect(startL + (3 * dist), row1Y, 250, 250))
        self.TimetableLogo.setText("")
        self.TimetableLogo.setPixmap(QtGui.QPixmap("C:/Users/618984/OneDrive - TGS Kew/Michael Wu/2023/Programming/synergeticv2/synergetic/img/timetablelogo.png"))
        self.TimetableLogo.setObjectName("TimetableLogo")
        self.TimetableText = QtWidgets.QLabel(Form)
        self.TimetableText.setText("View Timetable")
        self.TimetableText.setFont(font)
        self.TimetableText.setGeometry(QtCore.QRect(startL + (3 * dist) - 5, row1Y + 170, 300, 250))
        self.TimetableText.setObjectName("TimetableText")

        self.AdminPanelLogo = QtWidgets.QLabel(Form)
        self.AdminPanelLogo.setScaledContents(True)
        self.AdminPanelLogo.setGeometry(QtCore.QRect(startL, row1Y+400, 250, 250))
        self.AdminPanelLogo.setText("")
        self.AdminPanelLogo.setPixmap(QtGui.QPixmap("C:/Users/618984/OneDrive - TGS Kew/Michael Wu/2023/Programming/synergeticv2/synergetic/img/adminpanellogo.png"))
        self.AdminPanelLogo.setObjectName("TimetableLogo")
        self.AdminPanelText = QtWidgets.QLabel(Form)
        self.AdminPanelText.setText("Admin Panel")
        self.AdminPanelText.setFont(font)
        self.AdminPanelText.setGeometry(QtCore.QRect(startL+15, row1Y + 400 + 170, 300, 250))
        self.AdminPanelText.setObjectName("TimetableText")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindow()
    ui.setupUI(MainWindow)
    ui.mainMenu(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())