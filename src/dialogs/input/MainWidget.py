# -*- coding: utf-8 -*-
"""PySide2 QInputDialog()."""
import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                               QLabel, QInputDialog, QLineEdit)


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('PySide2 QInputDialog().')

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

        self.label = QLabel('Clique nos botões para abrir os diálogos.')
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        btn_input_text = QPushButton('Abrir diálogo de input de texto')
        btn_input_text.clicked.connect(self.open_input_text_dialog)
        vbox.addWidget(btn_input_text)

        btn_input_mult_line = QPushButton('Abrir diálogo de input de texto multi linha')
        btn_input_mult_line.clicked.connect(self.open_input_mult_line_text_dialog)
        vbox.addWidget(btn_input_mult_line)

        btn_input_int = QPushButton('Abrir diálogo de input de numero intero')
        btn_input_int.clicked.connect(self.open_input_int_dialog)
        vbox.addWidget(btn_input_int)

        btn_input_float = QPushButton('Abrir diálogo de input de numero com ponto flutuante')
        btn_input_float.clicked.connect(self.open_input_float_dialog)
        vbox.addWidget(btn_input_float)

        btn_input_choice = QPushButton('Abrir diálogo de input de seleção de itens')
        btn_input_choice.clicked.connect(self.open_input_choice_dialog)
        vbox.addWidget(btn_input_choice)

    def open_input_text_dialog(self):
        value, response = QInputDialog().getText(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo.',
            # label (str): Texto que será exibido junto com o input.
            'Digite algo no input e clique em OK:',
            # echo (QLineEdit).
            QLineEdit.Normal,
            # text (str): Valor inicial do input.
            'Digite algo',
        )
        if response and value:
            self.label.setText(f'<b>Valor digitado</b>: {value}')

    def open_input_mult_line_text_dialog(self):
        value, response = QInputDialog().getMultiLineText(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo.',
            # label (str): Texto que será exibido junto com o input.
            'Digite algo na caixa de texto e clique em OK:',
            # text (str): Valor inicial do input.
            'Digite algo',
        )
        if response and value:
            self.label.setText(f'<b>Valor digitado</b>: {value}')

    def open_input_int_dialog(self):
        value, response = QInputDialog().getInt(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo.',
            # label (str): Texto que será exibido junto com o input.
            'Digite um numero inteiro e clique em OK:',
            # value (int). Valor inicial do input.
            0,
            # minValue (int). Valor mínimo do input.
            -10,
            # maxValue (int). Valor maximo do input.
            10,
            # step (int). Valor do incremento/decremento.
            2,
        )
        if response and value:
            self.label.setText(f'<b>Valor digitado</b>: {value}')

    def open_input_float_dialog(self):
        value, response = QInputDialog().getDouble(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo.',
            # label (str): Texto que será exibido junto com o input.
            'Digite algo e clique em OK:',
            # value (float): Valor inicial do input.
            0,
            # minValue (float): Valor mínimo do input.
            -10,
            # maxValue (float): Valor maximo do input.
            10,
            # decimals(int): Numero de casas decimais.
            2,
        )
        if response and value:
            self.label.setText(f'<b>Valor digitado</b>: {value:.2f}')

    def open_input_choice_dialog(self):
        value, response = QInputDialog().getItem(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo.',
            # label (str): Texto que será exibido junto com o input.
            'Selecione um dos itens e clique em OK:',
            # items ([str]): Lista com o texto que será exibido.
            ['item 1', 'item 2', 'item 3'],
            # current (int): Valor inicial (index).
            1,
            # editable (bool): Valor determina se o campo pode ser editado.
            False,
        )
        if response and value:
            self.label.setText(f'<b>Valor selecionado</b>: {value}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())
