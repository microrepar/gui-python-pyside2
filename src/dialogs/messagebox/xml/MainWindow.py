# -*- coding: utf-8 -*-
"""PySide2 QInputDialog()."""
import sys

from PySide2.QtCore import QCoreApplication, Qt, QObject, QDir
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

        # Widgets.
        self.label = self.ui.findChild(QObject, 'label')

        btn_dialog = self.ui.findChild(QObject, 'btn_dialog')
        btn_dialog.clicked.connect(self.open_dialog)

        btn_dialog_about = self.ui.findChild(QObject, 'btn_dialog_about')
        btn_dialog_about.clicked.connect(self.open_dialog_about)

        btn_dialog_aboutqt = self.ui.findChild(QObject, 'btn_dialog_aboutqt')
        btn_dialog_aboutqt.clicked.connect(self.open_dialog_aboutqt)

        btn_dialog_critical = self.ui.findChild(QObject, 'btn_dialog_critical')
        btn_dialog_critical.clicked.connect(self.open_dialog_critical)

        btn_dialog_information = self.ui.findChild(QObject, 'btn_dialog_information')
        btn_dialog_information.clicked.connect(self.open_dialog_information)

        btn_dialog_question = self.ui.findChild(QObject, 'btn_dialog_question')
        btn_dialog_question.clicked.connect(self.open_dialog_question)

        btn_dialog_warning = self.ui.findChild(QObject, 'btn_dialog_warning')
        btn_dialog_warning.clicked.connect(self.open_dialog_warning)

        self.ui.show()

    def open_dialog(self):
        dialog = QMessageBox(parent=self.ui)
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
            self.ui,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
            # text (str): Texto que será exibido na janela de diálogo.
            'Texto da janela de diálogo',
        )

    def open_dialog_aboutqt(self):
        QMessageBox().aboutQt(
            # parent (QWidget): Pai da janela de diálogo.
            self.ui,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
        )

    def open_dialog_critical(self):
        QMessageBox().critical(
            # parent (QWidget): Pai da janela de diálogo.
            self.ui,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
            # text (str): Texto que será exibido na janela de diálogo.
            'Texto da janela de diálogo',
        )

    def open_dialog_information(self):
        QMessageBox().information(
            # parent (QWidget): Pai da janela de diálogo.
            self.ui,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
            # text (str): Texto que será exibido na janela de diálogo.
            'Texto da janela de diálogo',
        )

    def open_dialog_question(self):
        response = QMessageBox().question(
            # parent (QWidget): Pai da janela de diálogo.
            self.ui,
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
            self.ui,
            # title (str): Título da janela de diálogo.
            'Título da janela de diálogo',
            # text (str): Texto que será exibido na janela de diálogo.
            'Texto da janela de diálogo',
        )


if __name__ == "__main__":
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
