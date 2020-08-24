# -*- coding: utf-8 -*-
"""PySide2 QInputDialog()."""
import sys

from PySide2.QtCore import QCoreApplication, Qt, QObject, QDir
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # Caminho até o arquivo de interface.
        # path = QDir(__file__).currentPath()
        # ui_file = QDir(path).filePath('MainWindow.ui')
        ui_file = QDir(QDir(__file__).currentPath()).filePath('MainWindow.ui')

        self.ui = QUiLoader().load(ui_file, None)

        # Widgets.
        self.label = self.ui.findChild(QObject, 'label')

        btn_input_text = self.ui.findChild(QObject, 'btn_input_text')
        btn_input_text.clicked.connect(self.open_input_text_dialog)

        btn_input_mult_line = self.ui.findChild(QObject, 'btn_input_mult_line')
        btn_input_mult_line.clicked.connect(self.open_input_mult_line_text_dialog)

        btn_input_int = self.ui.findChild(QObject, 'btn_input_int')
        btn_input_int.clicked.connect(self.open_input_int_dialog)

        btn_input_float = self.ui.findChild(QObject, 'btn_input_float')
        btn_input_float.clicked.connect(self.open_input_float_dialog)

        btn_input_choice = self.ui.findChild(QObject, 'btn_input_choice')
        btn_input_choice.clicked.connect(self.open_input_choice_dialog)

        self.ui.show()

    def open_input_text_dialog(self):
        value, response = QInputDialog().getText(
            # parent (QWidget): Pai da janela de diálogo.
            self.ui,
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
            self.ui,
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
            self.ui,
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
            self.ui,
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
            self.ui,
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
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
