# -*- coding: utf-8 -*-
"""QWidget e connect.

Criando uma aplicativo do tipo QWidget com Python e utilizando o
`connect()` para executar um callback.
"""
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        screen_size = app.primaryScreen().geometry()
        width = screen_size.width()
        height = screen_size.height()
        self.resize(int(width / 2), int(height / 2))
        self.setMinimumSize(int(width / 3), int(height / 3))
        self.setWindowTitle('QWidget e connect')
        icon = QIcon()
        icon.addPixmap(QPixmap('../assets/icons/icon.png'))
        self.setWindowIcon(icon)

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
