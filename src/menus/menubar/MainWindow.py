# -*- coding: utf-8 -*-
"""PySide2 QMenuBar()."""
import sys

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # Título da janela.
        self.setWindowTitle('PySide2 QMenuBar().')

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

        # Menubar fica lozalizado na parte superior da janela.
        menu_bar = self.menuBar()

        menu_file = menu_bar.addMenu('Arquivo')
        menu_file.addAction('Sair 1', self.close_app)

        icon_exit = QIcon('../../../images/icons/exit-64x64.png')
        menu_file.addAction(icon_exit, 'Sair 2', self.close_app)

        menu_about = menu_bar.addMenu('Sobre')
        menu_about.addAction('Sobre este app', self.about)

    def close_app(self):
        self.close()

    def about(self):
        icon = QIcon()
        icon.addPixmap(QPixmap('../../../images/icons/icon.png'))

        message_box = QMessageBox(parent=self)
        message_box.setWindowTitle('Título da caixa de texto')
        message_box.setWindowIcon(icon)
        message_box.setText(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do '
            'eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim '
            'ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut '
            'aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit '
            'in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
            'Excepteur sint occaecat cupidatat non proident, sunt in culpa '
            'qui officia deserunt mollit anim id est laborum.'
        )
        message_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
