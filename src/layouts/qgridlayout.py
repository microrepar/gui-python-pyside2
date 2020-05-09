# -*- coding: utf-8 -*-
"""."""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout


class MainWindow(QWidget):

    def __init__(self, screen_size):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('Título da janela')

        # Ícone da janela principal
        icon = QIcon()
        icon.addPixmap(QPixmap('../assets/icons/icon.png'))
        self.setWindowIcon(icon)

        # Tamanho inicial da janela.
        width = screen_size.width()
        height = screen_size.height()
        self.resize(width / 2, height / 2)

        # Tamanho mínimo da janela.
        self.setMinimumSize(width / 2, height / 2)

        # Tamanho maximo da janela.
        self.setMaximumSize(width - 200, height - 200)

        self.create_widgets()

    def create_widgets(self):
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        button1 = QPushButton('Button 1')
        grid_layout.addWidget(button1, 0, 0)

        button2 = QPushButton('Button 2')
        grid_layout.addWidget(button2, 0, 1)

        button3 = QPushButton('Button 3')
        # addWidget(arg__1, row, column, rowSpan, columnSpan, alignment)
        grid_layout.addWidget(button3, 1, 0, 1, 2)

        button4 = QPushButton('Button 4')
        grid_layout.addWidget(button4, 2, 0)

        button5 = QPushButton('Button 5')
        grid_layout.addWidget(button5, 2, 1)


if __name__ == "__main__":
    import sys

    app = QApplication([])

    screen_size = app.desktop().geometry()
    # screen_size = app.primaryScreen().geometry()

    mainwindow = MainWindow(screen_size=screen_size)
    mainwindow.show()
    sys.exit(app.exec_())
