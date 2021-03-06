# -*- coding: utf-8 -*-
"""XML QWidget.

Lendo arquivo de interface XML QWidget.
"""
import sys

from PySide2.QtCore import Qt, QCoreApplication, QDir, QObject
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        # Caminho até o arquivo de interface.
        # path = QDir(__file__).currentPath()
        # ui_file = QDir(path).filePath('MainWindow.ui')
        ui_file = QDir(QDir(__file__).currentPath()).filePath('MainWindow.ui')

        self.ui = QUiLoader().load(ui_file, None)

        # Widgets.
        self.label = self.ui.findChild(QObject, 'label')
        self.line_edit = self.ui.findChild(QObject, 'line_edit')
        push_button = self.ui.findChild(QObject, 'push_button')
        push_button.clicked.connect(self.on_button_clicked)

        self.ui.show()

    def on_button_clicked(self):
        text = self.line_edit.text()
        if text:
            self.label.setText(text)
        else:
            self.label.setText('Digite algo no campo de texto :)')


if __name__ == "__main__":
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    widget = MainWidget()
    sys.exit(app.exec_())
