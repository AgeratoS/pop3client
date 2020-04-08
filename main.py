import os

from PyQt5 import QtWidgets, QtCore

import mainWindow

class Browser(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    browser = Browser()
    browser.showMaximized()
    sys.exit(app.exec_())
