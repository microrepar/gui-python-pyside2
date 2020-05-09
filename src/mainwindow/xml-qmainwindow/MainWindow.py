# -*- coding: utf-8 -*-
"""XML QMainWindow.

Lendo arquivo de interface XML QMainWindow.
"""
from PySide2.QtCore import QObject, QCoreApplication, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication


class MainWindow(QObject):
    def __init__(self):
        super().__init__()
        # Variável **DEVE** utilizar `self`!
        self.window = QUiLoader().load('./MainWindow.ui')

        self.window.show()


if __name__ == "__main__":
    import sys

    # Para evitar o alerta: Qt WebEngine seems to be initialized from a plugin.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())
