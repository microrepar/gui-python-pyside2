# -*- coding: utf-8 -*-
"""PySide2 QColorDialog()."""
import sys

from PySide2.QtCore import Qt, QCoreApplication, QObject, QDir
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog


class MainWidget(QWidget):
    # Home do usuário.
    home = QDir().home().path()

    def __init__(self):
        super(MainWidget, self).__init__()
        # Caminho até o arquivo de interface.
        # path = QDir(__file__).currentPath()
        # ui_file = QDir(path).filePath('MainWindow.ui')
        ui_file = QDir(QDir(__file__).currentPath()).filePath('MainWindow.ui')

        self.ui = QUiLoader().load(ui_file, None)

        # Widgets.
        self.label = self.ui.findChild(QObject, 'label')

        btn_open_file = self.ui.findChild(QObject, 'btn_open_file')
        btn_open_file.clicked.connect(self.open_file_dialog)

        btn_open_files = self.ui.findChild(QObject, 'btn_open_files')
        btn_open_files.clicked.connect(self.open_files_dialog)

        btn_open_dir = self.ui.findChild(QObject, 'btn_open_dir')
        btn_open_dir.clicked.connect(self.open_dir_dialog)

        btn_save_file = self.ui.findChild(QObject, 'btn_save_file')
        btn_save_file.clicked.connect(self.open_save_dialog)

        self.ui.show()

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
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    widget = MainWidget()
    sys.exit(app.exec_())
