# -*- coding: utf-8 -*-
"""."""
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QFormLayout, QLineEdit


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
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        button1 = QPushButton('Button 1')

        line_edit1 = QLineEdit()
        form_layout.addRow(button1, line_edit1)

        button2 = QPushButton('Button 2')
        line_edit2 = QLineEdit()
        form_layout.addRow(button2, line_edit2)

        button3 = QPushButton('Button 3')
        line_edit3 = QLineEdit()
        form_layout.addRow(button3, line_edit3)


if __name__ == "__main__":
    import sys

    app = QApplication([])

    screen_size = app.desktop().geometry()
    # screen_size = app.primaryScreen().geometry()

    mainwindow = MainWindow(screen_size=screen_size)
    mainwindow.show()
    sys.exit(app.exec_())
