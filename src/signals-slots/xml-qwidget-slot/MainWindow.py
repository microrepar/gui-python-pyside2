# -*- coding: utf-8 -*-
"""XML QWidget e Slot.

Lendo arquivo de interface XML QWidget e utilizando o
`Slot()` para executar um callback.

> Ainda não funciona!
"""
from PySide2.QtCore import QObject, QCoreApplication, Qt, Slot
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication


class MainWindow(QObject):
    def __init__(self):
        super().__init__()
        self.window = QUiLoader().load('./MainWindow.xml')

        self.label = self.window.findChild(QObject, 'label')
        self.line_edit = self.window.findChild(QObject, 'line_edit')

        self.window.show()

    @Slot()
    def on_button_clicked(self):
        text = self.line_edit.text()
        if text:
            self.label.setText(text)
        else:
            self.label.setText('Digite algo no campo de texto :)')


if __name__ == "__main__":
    import sys

    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())
