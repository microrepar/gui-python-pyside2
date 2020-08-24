# -*- coding: utf-8 -*-
"""QFormLayout com QWidget."""
import sys

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import (QApplication, QFormLayout, QLineEdit,
                               QPushButton, QWidget)


class MainWidget(QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        # Título da janela.
        self.setWindowTitle('QFormLayout com QWidget.')

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
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())
