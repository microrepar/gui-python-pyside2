# -*- coding: utf-8 -*-
"""PySide2 QToolBar()."""
import sys

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # Título da janela.
        self.setWindowTitle('PySide2 QToolBar().')

        # Ícone da janela principal
        icon = QIcon()
        icon.addPixmap(QPixmap('../../../images/icons/icon.png'))
        self.setWindowIcon(icon)

        # Tamanho inicial da janela.
        screen_size = app.desktop().geometry()
        # screen_size = app.primaryScreen().geometry()
        width = screen_size.width()
        height = screen_size.height()
        self.resize(width / 2, height / 2)

        # Tamanho mínimo da janela.
        self.setMinimumSize(width / 2, height / 2)

        # Tamanho maximo da janela.
        self.setMaximumSize(width - 200, height - 200)

        # Acessando a barra de ferramentas.
        # Toolbar pode ser movido para diversas áreas da janela.
        tool_bar = QToolBar()
        tool_bar.setToolTip('Barra de ferramentas')
        self.addToolBar(tool_bar)

        icon_copy = QIcon('../../../images/icons/copy-64x64.png')
        tool_bar.addAction(icon_copy, 'Copiar', self.action_copy).setToolTip('Copiar')

        icon_paste = QIcon('../../../images/icons/paste-64x64.png')
        tool_bar.addAction(icon_paste, 'Colar', self.action_paste).setToolTip('Colar')

    @staticmethod
    def action_copy():
        print('Copiar')

    @staticmethod
    def action_paste():
        print('Colar')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
