# -*- coding: utf-8 -*-
"""PySide2 QMessageBox()."""
import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                               QLabel, QMessageBox)


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('PySide2 QMessageBox().')

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

        self.label = QLabel('Clique no botão para abrir o diálogo.')
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        btn_dialog = QPushButton('Abrir diálogo do tipo caixa de mensagem')
        btn_dialog.clicked.connect(self.open_dialog)
        vbox.addWidget(btn_dialog)

        btn_dialog_about = QPushButton('Abrir diálogo do tipo sobre (about)')
        btn_dialog_about.clicked.connect(self.open_dialog_about)
        vbox.addWidget(btn_dialog_about)

        btn_dialog_aboutqt = QPushButton('Abrir diálogo do tipo sobre (aboutqt)')
        btn_dialog_aboutqt.clicked.connect(self.open_dialog_aboutqt)
        vbox.addWidget(btn_dialog_aboutqt)

        btn_dialog_critical = QPushButton('Abrir diálogo do tipo crítico (critical)')
        btn_dialog_critical.clicked.connect(self.open_dialog_critical)
        vbox.addWidget(btn_dialog_critical)

        btn_dialog_information = QPushButton('Abrir diálogo do tipo informação (information)')
        btn_dialog_information.clicked.connect(self.open_dialog_information)
        vbox.addWidget(btn_dialog_information)

        btn_dialog_question = QPushButton('Abrir diálogo do tipo questão (question)')
        btn_dialog_question.clicked.connect(self.open_dialog_question)
        vbox.addWidget(btn_dialog_question)

        btn_dialog_warning = QPushButton('Abrir diálogo do tipo alerta (warning)')
        btn_dialog_warning.clicked.connect(self.open_dialog_warning)
        vbox.addWidget(btn_dialog_warning)

    def open_dialog(self):
        dialog = QMessageBox(parent=self)
        dialog.setWindowTitle('Título do diálogo')
        dialog.setText('Texto do diálogo')
        dialog.setInformativeText('Texto informativo do diálogo')
        dialog.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        dialog.setDefaultButton(QMessageBox.Cancel)

        response = dialog.exec()
        if response == QMessageBox.Save:
            print('Botão de SALVAR pressionado')
        elif response == QMessageBox.Discard:
            print('Botão de DESCARTAR pressionado')
        elif response == QMessageBox.Cancel:
            print('Botão de CANCELAR/FECHAR pressionado')

    def open_dialog_about(self):
        QMessageBox().about(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
            # text (str): Texto que será exibido na janela de diálogo.
            'Texto da janela de diálogo',
        )

    def open_dialog_aboutqt(self):
        QMessageBox().aboutQt(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
        )

    def open_dialog_critical(self):
        QMessageBox().critical(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
            # text (str): Texto que será exibido na janela de diálogo.
            'Texto da janela de diálogo',
        )

    def open_dialog_information(self):
        QMessageBox().information(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
            # text (str): Texto que será exibido na janela de diálogo.
            'Texto da janela de diálogo',
        )

    def open_dialog_question(self):
        response = QMessageBox().question(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
            # text (str): Texto que será exibido na janela de diálogo.
            'Texto da janela de diálogo',
        )
        if response == QMessageBox.StandardButton.Yes:
            print('Botão SIM pressionado')
        if response == QMessageBox.StandardButton.No:
            print('Botão NÃO/FECHAR pressionado')

    def open_dialog_warning(self):
        QMessageBox().warning(
            # parent (QWidget): Pai da janela de diálogo.
            self,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
            # text (str): Texto que será exibido na janela de diálogo.
            'Texto da janela de diálogo',
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())
