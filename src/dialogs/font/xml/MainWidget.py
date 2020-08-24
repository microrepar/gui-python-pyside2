# -*- coding: utf-8 -*-
"""PySide2 QColorDialog()."""
import sys

from PySide2.QtCore import Qt, QCoreApplication, QObject, QDir
from PySide2.QtGui import QFont
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget, QFontDialog


class MainWidget(QWidget):
    # Variável armazena a última fonte selecionada.
    last_font = QFont()

    def __init__(self):
        super(MainWidget, self).__init__()
        # Caminho até o arquivo de interface.
        # path = QDir(__file__).currentPath()
        # ui_file = QDir(path).filePath('MainWindow.ui')
        ui_file = QDir(QDir(__file__).currentPath()).filePath('MainWindow.ui')

        self.ui = QUiLoader().load(ui_file, None)

        # Widgets.
        self.label = self.ui.findChild(QObject, 'label')

        button = self.ui.findChild(QObject, 'button')
        button.clicked.connect(self.open_dialog)

        self.ui.show()

    def open_dialog(self):
        response, font = QFontDialog.getFont(
            self.last_font,
            parent=self.ui,
            title='Configuração da fonte.',
        )
        if response:
            self.label.setText(f'Fonte selecionada: {font.family()}')
            self.label.setFont(font)
            self.last_font = font


if __name__ == "__main__":
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    widget = MainWidget()
    sys.exit(app.exec_())
