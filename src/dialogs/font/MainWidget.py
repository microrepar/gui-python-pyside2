# -*- coding: utf-8 -*-
"""PySide2 QFontDialog()."""
import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFontDialog


class MainWidget(QWidget):
    # Variável armazena a última fonte selecionada.
    last_font = QFont()

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('PySide2 QFontDialog().')

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
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.label = QLabel('Fonte selecionada')
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        button = QPushButton('Abrir diálogo de seleção de fonte')
        button.clicked.connect(self.open_dialog)
        vbox.addWidget(button)

    def open_dialog(self):
        response, font = QFontDialog().getFont(
            self.last_font,
            parent=self,
            title='Configuração da fonte.',
        )
        if response:
            self.label.setText(f'Fonte selecionada: {font.family()}')
            self.label.setFont(font)
            self.last_font = font


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())
