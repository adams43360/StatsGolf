import sys
from PyQt5.QtWidgets import QPushButton, QGridLayout, QDialog, QLabel, QScrollBar
from PyQt5.QtCore import QDate
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class cardDetail(QDialog):
    def __init__(self, parent=None):
        super(cardDetail, self).__init__(parent)

        # Resize the page
        self.resize(600, 800)
        self.setWindowTitle("Ma carte de score")

        self.setupUi()

    def setupUi(self):
        # Create layout
        self.gridLayout = QGridLayout()
        self.verticalScrollBar = QScrollBar()
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)

        # Form generic structuration
        self.lbl_date = QtWidgets.QLabel("Date de jeu")
        self.gridLayout.addWidget(self.lbl_date, 0, 0, 1, 2)
        self.date_score = QtWidgets.QDateEdit(QDate.currentDate())
        self.gridLayout.addWidget(self.date_score, 0, 2, 1, 3)
        self.lbl_course = QtWidgets.QLabel("Parcours")
        self.gridLayout.addWidget(self.lbl_course, 0, 5, 1, 2)
        self.cmb_course = QtWidgets.QComboBox()

        self.cmb_course.currentIndexChanged.connect(self.nbHoles)


        self.gridLayout.addWidget(self.cmb_course, 0, 7, 1, 3)
        self.lbl_speed = QtWidgets.QLabel("Vitesse de jeu")
        self.gridLayout.addWidget(self.lbl_speed, 1, 0, 1, 2)
        self.cmb_speed = QtWidgets.QComboBox()
        self.gridLayout.addWidget(self.cmb_speed, 1, 2, 1, 3)
        self.lbl_starter = QtWidgets.QLabel("Départ")
        self.gridLayout.addWidget(self.lbl_starter, 1, 5, 1, 2)
        self.cmb_starter = QtWidgets.QComboBox()
        self.gridLayout.addWidget(self.cmb_starter, 1, 7, 1, 3)
        self.lbl_weather = QtWidgets.QLabel("Météo")
        self.gridLayout.addWidget(self.lbl_weather, 2, 0, 1, 2)
        self.cmb_weather = QtWidgets.QComboBox()
        self.gridLayout.addWidget(self.cmb_weather, 2, 2, 1, 3)
        self.lbl_party = QtWidgets.QLabel("Type de partie")
        self.gridLayout.addWidget(self.lbl_party, 2, 5, 1, 2)
        self.cmb_party = QtWidgets.QComboBox()
        self.gridLayout.addWidget(self.cmb_party, 2, 7, 1, 3)
        self.lbl_balls = QtWidgets.QLabel("Mes balles")
        self.gridLayout.addWidget(self.lbl_balls, 3, 0, 1, 2)
        self.cmb_balls = QtWidgets.QComboBox()
        self.gridLayout.addWidget(self.cmb_balls, 3, 2, 1, 3)

        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.line, 4, 0, 2, 10)

        # Insert data in ComboBox
        self.lstCourses()
        self.lstWeather()
        self.lstSpeed()
        self.lstStarter()
        self.lstParty()
        self.lstBalls()

        # Form generic structuration Footer
        self.btn_valid = QtWidgets.QDialogButtonBox()
        self.btn_valid.setOrientation(QtCore.Qt.Horizontal)
        self.btn_valid.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close | QtWidgets.QDialogButtonBox.Save)
        self.gridLayout.addWidget(self.btn_valid, 12, 6, 1, 4)

        self.btn_valid.accepted.connect(self.validForm)
        self.btn_valid.rejected.connect(self.close)

        self.setLayout(self.gridLayout)

    def bddConnect(self, request):
        try:
            conn = sqlite3.connect('golfstats.db')
            cur = conn.cursor()

            return cur.execute(request)

            cur.close()
            conn.close()
        except sqlite3.Error as error:
            print("Erreur lors de la connexion à SQLite", error)

    def nbHoles(self):
        hole_number = self.bddConnect("SELECT coursesholes FROM courses WHERE courses.idcourses = " + self.cmb_course.itemData(0))
        j = 5

        for i in range(hole_number.fetchone()[0]):
            print(i + 1)

            self.lbl_hole_1 = QtWidgets.QLabel("Trou " + str(i + 1))
            self.gridLayout.addWidget(self.lbl_hole_1, j, 0, 2, 1)
            self.cmb_hole_1 = QtWidgets.QComboBox()
            self.gridLayout.addWidget(self.cmb_hole_1, j, 1, 2, 2)
            self.lbl_club_1 = QtWidgets.QLabel("Club")
            self.gridLayout.addWidget(self.lbl_club_1, j, 3, 2, 1)
            self.cmb_club_1 = QtWidgets.QComboBox()
            self.gridLayout.addWidget(self.cmb_club_1, j, 4, 2, 2)
            self.chk_farway_1 = QtWidgets.QCheckBox("Fairway")
            self.gridLayout.addWidget(self.chk_farway_1, j, 6, 2, 2)
            self.chk_green_1 = QtWidgets.QCheckBox("Green")
            self.gridLayout.addWidget(self.chk_green_1, j, 8, 2, 2)
            self.txt_comment_1 = QtWidgets.QTextEdit("")
            self.gridLayout.addWidget(self.txt_comment_1, j + 2, 0, 1, 10)

            self.line = QtWidgets.QFrame()
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.gridLayout.addWidget(self.line, j + 3, 0, 2, 10)
            j = j + 4

        self.gridLayout.addWidget(self.verticalScrollBar, 0, 10, j - 4, 1)


    def lstCourses(self):
        liste_courses = self.bddConnect("SELECT courses.coursesname, courses.idcourses, golfs.golfsname FROM golfs, courses WHERE courses.idgolfs = golfs.idgolfs ORDER BY golfs.golfsname")

        for row in liste_courses:
            self.cmb_course.addItem(str(row[0] + " : " + row[2]), str(row[1]))

    def lstWeather(self):
        liste_weather = self.bddConnect("SELECT * FROM weather ORDER BY weathername")

        for row in liste_weather:
            self.cmb_weather.addItem(str(row[1]), str(row[0]))

    def lstSpeed(self):
        liste_speed = self.bddConnect("SELECT * FROM termes ORDER BY termesname")

        for row in liste_speed:
            self.cmb_speed.addItem(str(row[1]), str(row[0]))

    def lstStarter(self):
        liste_starter = self.bddConnect("SELECT * FROM starterballs ORDER BY starterballsname")

        for row in liste_starter:
            self.cmb_starter.addItem(str(row[1]), str(row[0]))

    def lstParty(self):
        liste_party = self.bddConnect("SELECT * FROM partytype ORDER BY partytypename")

        for row in liste_party:
            self.cmb_party.addItem(str(row[1]), str(row[0]))

    def lstBalls(self):
        liste_balls = self.bddConnect("SELECT * FROM balls ORDER BY ballsname")

        for row in liste_balls:
            self.cmb_balls.addItem(str(row[1]), str(row[0]))

    def validForm(self):
        pass