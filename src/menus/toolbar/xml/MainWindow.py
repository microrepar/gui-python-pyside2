# -*- coding: utf-8 -*-
"""PySide2 QToolBar()."""
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

        # Acessando a barra de ferramentas.
        # Toolbar pode ser movido para diversas áreas da janela.
        action_copiar = self.ui.findChild(QObject, 'action_copiar')
        action_copiar.triggered.connect(self.action_copy)

        action_colar = self.ui.findChild(QObject, 'action_colar')
        action_colar.triggered.connect(self.action_paste)

        self.ui.show()

    @staticmethod
    def action_copy():
        print('Copiar')

    @staticmethod
    def action_paste():
        print('Colar')


if __name__ == "__main__":
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
