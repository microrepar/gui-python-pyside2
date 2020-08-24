# -*- coding: utf-8 -*-
"""PySide2 QColorDialog()."""
import sys

from PySide2.QtCore import QCoreApplication, Qt, QObject, QDir
from PySide2.QtGui import QPalette
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QColorDialog


class MainWindow(QMainWindow):
    last_color = Qt.white

    def __init__(self):
        super(MainWindow, self).__init__()
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
        color = QColorDialog().getColor(
            parent=self.ui,
            title='Selecione uma cor',
            initial=self.last_color,
        )
        if color.isValid():
            self.last_color = color
            palette = self.label.palette()
            palette.setColor(QPalette.Background, color)
            self.label.setPalette(palette)


if __name__ == "__main__":
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
