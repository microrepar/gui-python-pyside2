# -*- coding: utf-8 -*-
"""PySide2 QStatusBar()."""
import sys

from PySide2.QtCore import QCoreApplication, Qt, QObject, QDir
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Caminho até o arquivo de interface.
        # path = QDir(__file__).currentPath()
        # ui_file = QDir(path).filePath('MainWindow.ui')
        ui_file = QDir(QDir(__file__).currentPath()).filePath('MainWindow.ui')

        self.ui = QUiLoader().load(ui_file, None)

        # Acessando a barra de estatus.
        statusbar = self.ui.findChild(QObject, 'statusbar')
        statusbar.setStyleSheet('color: red')
        statusbar.showMessage('Texto que será exibido na barra de estatus.', 5000)

        self.ui.show()


if __name__ == "__main__":
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
