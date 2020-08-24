# -*- coding: utf-8 -*-
"""PySide2 QMenuBar()."""
import sys

from PySide2.QtCore import QCoreApplication, Qt, QObject, QDir
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Caminho até o arquivo de interface.
        # path = QDir(__file__).currentPath()
        # ui_file = QDir(path).filePath('MainWindow.ui')
        ui_file = QDir(QDir(__file__).currentPath()).filePath('MainWindow.ui')

        self.ui = QUiLoader().load(ui_file, None)

        # Acessando o menu e conectando os métodos.
        action_sair_1 = self.ui.findChild(QObject, 'action_sair_1')
        action_sair_1.triggered.connect(self.close_app)

        action_sair_2 = self.ui.findChild(QObject, 'action_sair_2')
        action_sair_2.triggered.connect(self.close_app)

        action_sobre = self.ui.findChild(QObject, 'action_sobre')
        action_sobre.triggered.connect(self.about)

        self.ui.show()

    def close_app(self):
        self.ui.close()

    def about(self):
        icon = QIcon()
        icon.addPixmap(QPixmap('../../../images/icons/icon.png'))

        message_box = QMessageBox(parent=self)
        message_box.setWindowTitle('Título da caixa de texto')
        message_box.setWindowIcon(icon)
        message_box.setText(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do '
            'eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim '
            'ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut '
            'aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit '
            'in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
            'Excepteur sint occaecat cupidatat non proident, sunt in culpa '
            'qui officia deserunt mollit anim id est laborum.'
        )
        response = message_box.exec()
        message_box.close()


if __name__ == "__main__":
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
