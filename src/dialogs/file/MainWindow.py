# -*- coding: utf-8 -*-
"""PySide2 QFileDialog()."""
import sys

from PySide2.QtCore import QDir
from PySide2.QtGui import QIcon, QPixmap, Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QLabel, QPushButton, QFileDialog)


class MainWindow(QMainWindow):
    # Home do usuário.
    home = QDir().home().path()

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('PySide2 QFileDialog().')

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

        # Widget central.
        widget = QWidget()
        self.setCentralWidget(widget)

        # Widgets.
        vbox = QVBoxLayout()
        widget.setLayout(vbox)

        self.label = QLabel('Clique em um dos botões')
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        btn_open_file = QPushButton('Selecionar arquivo')
        btn_open_file.clicked.connect(self.open_file_dialog)
        vbox.addWidget(btn_open_file)

        btn_open_files = QPushButton('Selecionar arquivos')
        btn_open_files.clicked.connect(self.open_files_dialog)
        vbox.addWidget(btn_open_files)

        btn_open_dir = QPushButton('Selecionar um diretório')
        btn_open_dir.clicked.connect(self.open_dir_dialog)
        vbox.addWidget(btn_open_dir)

        btn_save_file = QPushButton('Salvar um arquivo')
        btn_save_file.clicked.connect(self.open_save_dialog)
        vbox.addWidget(btn_save_file)

    def open_file_dialog(self):
        file = QFileDialog().getOpenFileName(
            parent=self,
            caption='Selecione um arquivo',
            dir=str(self.home),
            filter=('PNG (*.png);;JPG (*.jpg, *.jpeg);;'
                    'TXT (*.txt);;Todos (*.*)'),
        )
        if file[0]:
            self.label.setText(
                f'<b>Arquivo selecionado</b>: {file[0]}<br>'
                f'<b>Filtro utilizado</b>: {file[1]}',
            )

    def open_files_dialog(self):
        files = QFileDialog().getOpenFileNames(
            parent=self,
            caption='Selecione os arquivos',
            dir=str(self.home),
            filter=('PNG (*.png);;JPG (*.jpg, *.jpeg);;'
                    'TXT (*.txt);;Todos (*.*)'),
        )
        if files[0]:
            text = '<b>Arquivos selecionados</b>:<br>'
            for file in files[0]:
                text += f'- {file}<br>'
            text += f'<b>Filtro utilizado</b>: {files[1]}'
            self.label.setText(text)

    def open_dir_dialog(self):
        path = QFileDialog().getExistingDirectory(
            parent=self,
            caption='Selecione um diretório',
            dir=str(self.home),
        )
        if path:
            self.label.setText(f'<b>Diretório selecionado</b>: {path}')

    def open_save_dialog(self):
        file = QFileDialog().getSaveFileName(
            parent=self,
            caption='Salvar arquivo',
            dir=str(self.home),
            filter='.png;;.txt;;.jpg;;',
        )
        if file[0]:
            if file[0].endswith(file[1]):
                text = f'<b>Arquivo salvo em</b>: {file[0]}<br>'
            else:
                text = f'<b>Arquivo salvo em</b>: {file[0]}{file[1]}<br>'
            text += f'<b>Filtro utilizado</b>: {file[1]}'
            self.label.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
