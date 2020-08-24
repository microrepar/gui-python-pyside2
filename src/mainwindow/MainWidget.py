# -*- coding: utf-8 -*-
"""QWidget."""
import sys

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QWidget


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('QWidget.')

        # Ícone da janela principal
        icon = QIcon()
        icon.addPixmap(QPixmap('../../images/icons/icon.png'))
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())
