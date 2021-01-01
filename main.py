import sys
import sqlite3
import scorecard
import cardnew
from PyQt5.QtWidgets import (QApplication, QPushButton, QGridLayout, QDialog, QMenuBar)

class HomePage(QDialog):
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)

        # Resize the page
        self.resize(1200, 800)
        self.setWindowTitle("Outil de statistiques pour le Golf")

        self.setupUi()

    def setupUi(self):
        # Create QMenuBar
        self.header = QMenuBar()
        self.menu_carte = self.header.addMenu("Carte de score")
        self.menu_carte.addAction("Enregistrer une cartes", self.addNewCard)
        self.menu_carte.addAction("Mes cartes", self.scoreCards)
        self.menu_stats = self.header.addMenu("Statistiques")
        self.menu_stats.addAction("Ouvrir mes statistiques", self.toDefine)

        # Create layout
        self.layout = QGridLayout()


        # Form structuration
        self.btn_cards = QPushButton('Mes cartes')
        self.btn_stats = QPushButton('Mes Stats')
        self.btn_cards.setMinimumHeight(200)
        self.btn_stats.setMinimumHeight(200)
        self.btn_cards.clicked.connect(self.scoreCards)
        self.btn_stats.clicked.connect(self.toDefine)

        # Add widgets
        self.layout.addWidget(self.btn_stats, 0, 1)
        self.layout.addWidget(self.btn_cards, 0, 2)

        self.setLayout(self.layout)

    def scoreCards(self):
        dialog = scorecard.ScoreCard()
        dialog.show()
        dialog.exec_()

    def toDefine(self):
        print("Coming soon")

    def addNewCard(self):
        dialog = cardnew.cardDetail()
        dialog.show()
        dialog.exec_()

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)#app = QApplication(sys.argv)

    # Create and show the form
    form = HomePage()
    form.show()

    # Run the main Qt loop
    sys.exit(app.exec_())