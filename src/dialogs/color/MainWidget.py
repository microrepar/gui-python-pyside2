# -*- coding: utf-8 -*-
"""PySide2 QColorDialog()."""
import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap, QPalette
from PySide2.QtWidgets import QApplication, QWidget, QColorDialog, QPushButton, QVBoxLayout, QLabel


class MainWidget(QWidget):
    # Variável armazena a última cor selecionada.
    last_color = Qt.white

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('PySide2 QColorDialog().')

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

        self.label = QLabel('Cor selecionada')
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        button = QPushButton('Abrir diálogo de seleção de cor')
        button.clicked.connect(self.open_dialog)
        vbox.addWidget(button)

    def open_dialog(self):
        color = QColorDialog().getColor(
            parent=self,
            title='Selecione uma cor',
            initial=self.last_color,
        )
        if color.isValid():
            self.last_color = color
            palette = self.label.palette()
            palette.setColor(QPalette.Background, color)
            self.label.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())
