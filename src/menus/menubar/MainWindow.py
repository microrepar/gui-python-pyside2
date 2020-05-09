# -*- coding: utf-8 -*-
"""PySide2 menuBar()."""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox


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
        self.setWindowTitle('PySide2 menuBar()')
        # Ícone da janela principal
        icon = QIcon()
        icon.addPixmap(QPixmap('../../assets/icons/icon.png'))
        self.setWindowIcon(icon)

        # Menubar fica lozalizado na parte superior da janela.
        menu_bar = self.menuBar()

        menu_file = menu_bar.addMenu('Arquivo')
        menu_file.addAction('Sair 1', self.close_app)

        icon_exit = QIcon('../../assets/icons/exit-64x64.png')
        menu_file.addAction(icon_exit, 'Sair 2', self.close_app)

        menu_about = menu_bar.addMenu('Sobre')
        menu_about.addAction('Sobre este app', self.about)

    def close_app(self):
        self.close()

    def about(self):
        icon = QIcon()
        icon.addPixmap(QPixmap('../../assets/icons/icon.png'))

        message_box = QMessageBox()
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
    import sys

    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
