import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from windows.CountriesWindow import CountriesWindow
from windows.TeamWindow import TeamWindow
from windows.PlayersWindow import PlayersWindow
# from windows.PlayersWindow import PlayersWindow


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.initActions()
        self.initMenu()

        # changing the background color to cyan
        self.setStyleSheet("background-color: pink;")

        # creating a label widget
        self.label = QLabel(
            "Assalomu aleykum bu mening Pyqt5dagi proyektim", self)

        # moving position
        self.label.move(10000, 1000)

    def initActions(self):
        self.newAction = QAction("&New...", self)
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)

        self.countriesAction = QAction("&Countries", self)
        self.countriesAction.triggered.connect(self.onCountriesWindow)
        self.teamAction = QAction("&Team", self)
        self.teamAction.triggered.connect(self.onTeamWindow)
        self.playersAction = QAction("&Players")
        self.playersAction.triggered.connect(self.onPlayersWindow)
  
    def initMenu(self):
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)

        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)

        servicesMenu = menuBar.addMenu("&Services")
        servicesMenu.addAction(self.countriesAction)
        servicesMenu.addAction(self.teamAction)
        servicesMenu.addAction(self.playersAction)


        helpMenu = menuBar.addMenu("&Help")

    def onCountriesWindow(self):
        self.regw = CountriesWindow()
        self.regw.show()

    def onTeamWindow(self):
        self.regw = TeamWindow()
        self.regw.show()


    def onPlayersWindow(self):
        self.regw = PlayersWindow()
        self.regw.show()

    # changing the background color to cyan
        self.setStyleSheet("background-color: cyan;")

        # creating a label widget
        self.label = QLabel("Cyan", self)

        # moving position
        self.label.move(100, 100)

        # setting up border
        self.label.setStyleSheet("border: 1px solid black;")

        # show all the widgets
        self.show()


app = QApplication(sys.argv)
w = Window()
w.showMaximized()
app.exec()