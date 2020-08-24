# -*- coding: utf-8 -*-
"""QVBoxLayout com QWidget."""
import sys

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout)


class MainWidget(QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        # Título da janela.
        self.setWindowTitle('QVBoxLayout com QWidget.')

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

        # Widgets.
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        for n in range(1, 5):
            button = QPushButton(f'Button {n}')
            vbox.addWidget(button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())
