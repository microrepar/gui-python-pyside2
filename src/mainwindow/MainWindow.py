# -*- coding: utf-8 -*-
"""QMainWindow.

Criando uma aplicativo do tipo QMainWindow com Python.
"""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    """Classe MainWindow herda de `QMainWindow()`.

    `QMainWindow()` possui:

    - Barra de menu ``menuBar()``.
    - Barra de status ``statusBar()``.
    - Barra de ferramentas ``addToolBar()``.
    """

    def __init__(self):
        super().__init__()
        # Resolução do monitor.
        screen_size = app.primaryScreen().geometry()
        width = screen_size.width()
        height = screen_size.height()
        # Tamanho inicial da janela.
        self.resize(int(width / 2), int(height / 2))
        # Tamanho mínimo da janela.
        self.setMinimumSize(int(width / 3), int(height / 3))
        # Título da janela.
        self.setWindowTitle('PySide2 janela QMainWindow()')
        # Ícone da janela principal
        icon = QIcon()
        icon.addPixmap(QPixmap('../assets/icons/icon.png'))
        self.setWindowIcon(icon)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
