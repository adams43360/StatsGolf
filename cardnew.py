import sys
from PySide6.QtWidgets import *
import sqlite3


class cardDetail(QDialog):
    def __init__(self, parent=None):
        super(cardDetail, self).__init__(parent)

        # Resize the page
        self.resize(600, 800)
        self.setWindowTitle("Ma carte de score")

        self.setupUi(self)

    def setupUi(self):
        # Create layout
        self.layout = QGridLayout()

        # Form structuration
        self.lbl_title = QLabel("Carte neuve")

        self.btn_add = QPushButton('Ajouter')
        self.btn_add.clicked.connect(self.newBdd)

        # Add widgets
        self.layout.addWidget(self.lbl_title, 1, 0, 1, 1)
        self.layout.addWidget(self.btn_add, 3, 3, 1, 1)


        self.setLayout(self.layout)

    def newBdd(self):
        print("New Scorecard")
        '''
        try:
            conn = sqlite3.connect('golfstats.db')
            cur = conn.cursor()
            sql = "SELECT * " \
                  "FROM courses " \
                  "WHERE courses.idcourses = 1;"

            res = cur.execute(sql)

            cur.close()
            conn.close()
        except sqlite3.Error as error:
            print("Erreur lors de la connexion à SQLite", error)
        '''