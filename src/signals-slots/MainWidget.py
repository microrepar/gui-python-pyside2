# -*- coding: utf-8 -*-
"""PySide2 QWidget e connect().

Criando uma aplicativo do tipo QWidget com Python e utilizando o
`connect()` para executar um callback.
"""
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('PySide2 QWidget e connect().')

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

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.label = QLabel('Este texto será alterado quando o botão for clicado!')
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Digite algo')
        vbox.addWidget(self.line_edit)

        push_button = QPushButton('Clique Aqui')
        push_button.clicked.connect(self.on_button_clicked)
        vbox.addWidget(push_button)

    def on_button_clicked(self):
        text = self.line_edit.text()
        if text:
            self.label.setText(text)
        else:
            self.label.setText('Digite algo no campo de texto :)')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())
