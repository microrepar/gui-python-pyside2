# -*- coding: utf-8 -*-
"""XML QWidget.

Lendo arquivo de interface XML QWidget.
"""
import sys

from PySide2.QtCore import Qt, QCoreApplication, QDir
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        # Caminho até o arquivo de interface.
        # path = QDir(__file__).currentPath()
        # ui_file = QDir(path).filePath('MainWindow.ui')
        ui_file = QDir(QDir(__file__).currentPath()).filePath('MainWindow.ui')

        self.ui = QUiLoader().load(ui_file, None)
        self.ui.show()


if __name__ == "__main__":
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    widget = MainWidget()
    sys.exit(app.exec_())
