import sys
import sqlite3
from PySide6.QtWidgets import *
import scorecard

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
        self.menu_carte = self.header.addMenu("Cartes de score")
        self.menu_carte.addAction("Enregistrer une cartes", self.toDefine)
        self.menu_carte.addAction("Mes cartes", self.scoreCards)
        self.menu_stats = self.header.addMenu("Statistiques")
        self.menu_stats.addAction("Ouvrir mes statistiques", self.toDefine)

        # Create layout
        self.layout = QGridLayout()

        # Form structuration
        self.btn_cards = QPushButton('Mes cartes')
        self.btn_stats = QPushButton('Mes Stats')
        self.btn_cards.setMinimumHeight(200)
        self.btn_cards.clicked.connect(self.toDefine)
        self.btn_stats.setMinimumHeight(200)
        self.btn_stats.clicked.connect(self.toDefine)

        # Add widgets
        self.layout.addWidget(self.btn_stats, 1, 2, 1, 2)
        self.layout.addWidget(self.btn_cards, 1, 0, 1, 2)

        self.setLayout(self.layout)

    def scoreCards(self):
        dialog = scorecard.ScoreCard()
        dialog.show()
        dialog.exec_()

    def toDefine(self):
        print("Coming soon")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the form
    form = HomePage()
    form.show()

    # Run the main Qt loop
    sys.exit(app.exec_())