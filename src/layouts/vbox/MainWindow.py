# -*- coding: utf-8 -*-
"""QVBoxLayout com QMainWindow."""
import sys

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # Título da janela.
        self.setWindowTitle('QVBoxLayout com QMainWindow.')

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

        # Layout.
        vbox = QVBoxLayout()

        # Widget central.
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        for n in range(1, 5):
            button = QPushButton(f'Button {n}')
            vbox.addWidget(button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
