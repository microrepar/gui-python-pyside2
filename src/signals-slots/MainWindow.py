# -*- coding: utf-8 -*-
"""PySide2 QMainWindow e connect().

Criando uma aplicativo do tipo QMainWindow com Python e utilizando o
`connect()` para executar um callback.
"""
import sys

from PySide2.QtGui import QIcon, QPixmap, Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QLabel, QLineEdit, QPushButton)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('PySide2 QMainWindow e connect().')

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

        vbox = QVBoxLayout()
        widget.setLayout(vbox)

        # Widgets
        self.label = QLabel('Este texto será alterado quando o botão for clicado!')
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Digite algo')
        vbox.addWidget(self.line_edit)

        push_button = QPushButton('Clique Aqui')
        # Conectando o callback com o evento de clique do botão.
        push_button.clicked.connect(self.on_button_clicked)
        vbox.addWidget(push_button)

    def on_button_clicked(self):
        text = self.line_edit.text()
        if text:
            self.label.setText(text)
        else:
            self.label.setText('Digite algo no campo de texto :)')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
