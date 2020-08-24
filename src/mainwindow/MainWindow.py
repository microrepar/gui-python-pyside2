# -*- coding: utf-8 -*-
"""QMainWindow."""
import sys

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget


class MainWindow(QMainWindow):
    """Classe MainWindow herda de `QMainWindow()`.

    `QMainWindow()` possui:

    - Barra de menu ``menuBar()``.
    - Barra de status ``statusBar()``.
    - Barra de ferramentas ``addToolBar()``.
    """

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('QMainWindow.')

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

        # Widget central.
        widget = QWidget()
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
