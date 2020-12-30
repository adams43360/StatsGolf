import sys
from PySide6.QtWidgets import *
import sqlite3
import cardddetail
import cardnew

class ScoreCard(QDialog):
    def __init__(self, parent=None):
        super(ScoreCard, self).__init__(parent)

        # Resize the page
        self.resize(1200, 800)
        self.setWindowTitle("Page statistiques")

        self.setupUi()

    def setupUi(self):
        # Create layout
        self.layout = QGridLayout()

        # Form structuration
        self.lbl_title = QLabel('Mes cartes de score')
        self.btn_add = QPushButton('+')
        self.btn_add.clicked.connect(self.addClick)

        # Table BDD integration
        self.tab_result = QTableWidget(self)
        self.tab_result.setColumnCount(9)
        self.tab_result.setHorizontalHeaderLabels(["Id carte", "Date", "Parcours", "Score", "Nb Fairway", "Greens en régulation", "Météo", "Fluidité de jeu", "Mode de jeu"])
        self.tab_result.verticalHeader().setVisible(False)
        self.tab_result.cellDoubleClicked.connect(lambda item: self.printClick(item))

        # Add widgets
        self.layout.addWidget(self.lbl_title, 1, 0, 1, 1)
        self.layout.addWidget(self.tab_result, 2, 0, 1, 4)
        self.layout.addWidget(self.btn_add, 3, 3, 1, 1)

        self.setLayout(self.layout)

        self.connectBdd()

    def printClick(self, value):
        dialog = cardddetail.cardDetail(value=self.tab_result.item(value, 0).text())
        dialog.show()
        dialog.exec_()

    def addClick(self, value):
        dialog = cardnew.cardDetail()
        dialog.show()
        dialog.exec_()

    def connectBdd(self):
        try:
            conn = sqlite3.connect('golfstats.db')
            cur = conn.cursor()
            sql = "SELECT scorecards.idscorecards, " \
                  "scorecards.scorecardsdate, " \
                  "courses.coursesname, " \
                  "sum(results.resultscore) as resultat, " \
                  "sum(results.resultfairway) as fairway, " \
                  "sum(results.resultgreen) as green, " \
                  "weather.weathername, " \
                  "partytype.partytypename, " \
                  "termes.termesname " \
                  "FROM scorecards, courses, results, weather, partytype, termes " \
                  "WHERE scorecards.idcourses = courses.idcourses AND " \
                  "scorecards.idweather = weather.idweather AND " \
                  "scorecards.idtermes = termes.idtermes AND " \
                  "scorecards.idpartytype = partytype.idpartytype AND " \
                  "scorecards.idscorecards = results.idscorecards " \
                  "GROUP BY scorecards.idscorecards;"

            res = cur.execute(sql)
            self.tab_result.setRowCount(0)

            for row_number, row_data in enumerate(res):
                self.tab_result.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tab_result.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            cur.close()
            conn.close()
        except sqlite3.Error as error:
            print("Erreur lors de la connexion à SQLite", error)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the form
    form = ScoreCard()
    form.show()

    # Run the main Qt loop
    sys.exit(app.exec_())