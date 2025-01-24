import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QMenu, QAction, QDialog, QToolBox, QWidget, QLabel, \
    QDesktopWidget, QToolBar, QPushButton, QMdiArea, QMdiSubWindow, QListWidget
from PyQt5 import QtCore, uic
from PyQt5.QtGui import *

import pyqtgraph as pg


class mySubWindow(QMainWindow):  # Window that is produced from the toolbar

    def __init__(self):
        super().__init__()

        uic.loadUi("subwindow.ui", self)  # Load the UI file and grab its XML.

        # get widget references from the ui file
        self.btnClose = self.findChild(QPushButton, "btnSubClose")
        print(self.btnClose)

        # Events from sub window
        self.btnClose.clicked.connect(self.closeSubWindow)

        self.setupWidgets()
        self.setWindowModality(
            QtCore.Qt.ApplicationModal)  # Sets the window to be a modal, so that you can't click back to the main application.

        self.show()  # Display the subwindow.

    # enddef

    def closeSubWindow(self):
        self.close()  # Closes the child window.

    # end def

    def setupWidgets(self):
        # Set the title of the window created.
        self.setWindowTitle("SubWindow")

        # setting  the geometry of window
        self.setGeometry(299, 200, 400, 300)

        # creating a label widget
        # by default label will display at top left corner
        self.label = QLabel('This is label', self)

    # enddef


# endclass mywindow


class mainWindow(QMainWindow):  # The main window that opens when the application starts

    def __init__(self):
        super().__init__()
        uic.loadUi("mainui.ui", self)  # Load the file

        # Set the number for how many windows are open.
        self.mdi_windows_open = 0

        # Create all the defauls and enable them.
        self.set_window_properties()
        self.create_menus()
        self.create_toolbox()
        self.create_statusbar()

        # get widget references from the ui file
        self.btnOk = self.findChild(QPushButton, "btnOpen")
        self.mdi = self.findChild(QMdiArea, "mdiArea")
        self.lcd = self.findChild(QLCDNumber, "lcdNumber")
        self.lcd.setDigitCount(2)

        # Events from main window
        self.btnOk.clicked.connect(self.new_mdiWindow)

    # enddef

    def set_window_properties(self):
        # set window size and position settings
        self.height = 300
        self.width = 300
        self.top = 150
        self.left = 150

    # enddef

    def create_menus(self):
        # Menu Bar Settings
        action = self.findChild(QAction, "menu_WindowNew")
        action.triggered.connect(self.openSubWindow)

    # enddef

    def openSubWindow(self):
        self.newWin = mySubWindow()

    # enddef

    def create_toolbox(self):
        pass

    # enddef

    def create_statusbar(self):
        # Status Bar Settings
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("This is an status message.", 5000)
        label = QLabel("permanent status")
        self.statusBar.addPermanentWidget(label)

    # enddef

    def new_mdiWindow(self):
        new = QMdiSubWindow()

        # graph = pg
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
        #
        # graph.plot(x, y)

        new.setWidget(pg.plot(x, y))
        new.setWindowTitle("new")
        self.mdi.addSubWindow(new)

        self.mdi_windows_open += 1

        self.lcd.display(self.mdi_windows_open)
        self.lcd.update()

        new.show()

    # enddef


# endclass MainWindow


# main starts here
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()

    sys.exit(app.exec_())
