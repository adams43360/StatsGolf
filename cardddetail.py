import sys
from PySide6.QtWidgets import *
import sqlite3


class cardDetail(QDialog):
    def __init__(self, value="", parent=None):
        self.v = value
        super(cardDetail, self).__init__(parent)

        # Resize the page
        self.resize(600, 800)
        self.setWindowTitle("Ma carte de score")

        self.setupUi(self.v)

    def setupUi(self, v):
        # Create layout
        self.layout = QGridLayout()

        # Form structuration
        self.lbl_title = QLabel("Value = " + str(self.v))

        # If isset v
        if self.v != "":
            self.btn_add = QPushButton('Ajouter')
            self.btn_add.clicked.connect(self.newBdd)

            # Add widgets
            self.layout.addWidget(self.lbl_title, 1, 0, 1, 1)
            self.layout.addWidget(self.btn_add, 3, 3, 1, 1)
        else:
            self.btn_add = QPushButton('Modifier')
            self.btn_add.clicked.connect(self.existingBdd)

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
    def existingBdd(self):
        print("Existing scoreCard")
        '''
        try:
            conn = sqlite3.connect('golfstats.db')
            cur = conn.cursor()
            sql = "SELECT scorecards.*, resultat.*, courses.* " \
                  "FROM scorecards, courses, results " \
                  "WHERE scorecards.idscorecards = result.idscorecards AND " \
                  "scorecards.idcourses = courses.idcourses;"

            res = cur.execute(sql)

            cur.close()
            conn.close()
        except sqlite3.Error as error:
            print("Erreur lors de la connexion à SQLite", error)
        '''

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = cardDetail()
    form.show()

    # Run the main Qt loop
    sys.exit(app.exec_())