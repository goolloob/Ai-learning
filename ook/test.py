import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import ook.Ui_test as Ui_test

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_test.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())