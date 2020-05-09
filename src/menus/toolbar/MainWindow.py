# -*- coding: utf-8 -*-
"""PySide2 QToolBar()."""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar


class MainWindow(QMainWindow):

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
        self.setWindowTitle('PySide2 QToolBar()')
        # Ícone da janela principal
        icon = QIcon()
        icon.addPixmap(QPixmap('../../assets/icons/icon.png'))
        self.setWindowIcon(icon)

        # Toolbar pode ser movido para diversas áreas da janela.
        tool_bar = QToolBar()
        tool_bar.setToolTip('Barra de ferramentas')
        self.addToolBar(tool_bar)

        icon_copy = QIcon('../../assets/icons/copy-64x64.png')
        tool_bar.addAction(icon_copy, 'Copiar', self.action_copy).setToolTip('Copiar')

        icon_paste = QIcon('../../assets/icons/paste-64x64.png')
        tool_bar.addAction(icon_paste, 'Colar', self.action_paste).setToolTip('Colar')

    @staticmethod
    def action_copy():
        print('Copiar')

    @staticmethod
    def action_paste():
        print('Colar')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
