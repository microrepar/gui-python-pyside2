# -*- coding: utf-8 -*-
"""PySide2 drag and drop.

| Tester 	 | Getter 	   | Setter 	    | MIME Types          |
| ---------- | ----------- | -------------- | ------------------- |
| hasText()  | text() 	   | setText() 	    | text/plain          |
| hasHtml()  | html() 	   | setHtml() 	    | text/html           |
| hasUrls()  | urls() 	   | setUrls() 	    | text/uri-list       |
| hasImage() | imageData() | setImageData() | image/ *            |
| hasColor() | colorData() | setColorData() | application/x-color |

- `QDrag`: Support for MIME-based drag and drop data transfer.
- `QDragEnterEvent`: Event which is sent to a widget when a drag and drop action enters it.
- `QDragLeaveEvent`: Event that is sent to a widget when a drag and drop action leaves it.
- `QDragMoveEvent`: Event which is sent while a drag and drop action is in progress.
- `QDropEvent`: Event which is sent when a drag and drop action is completed.
"""

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, \
    QListWidgetItem


class MainWidget(QWidget):
    icons = ['applications-accessories', 'applications-development',
             'applications-engineering', 'applications-games',
             'applications-graphics']

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('QWidget.')

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

        # Widgets
        hbox = QHBoxLayout()
        self.setLayout(hbox)

        list_widget = QListWidget()
        list_widget.setAcceptDrops(True)
        list_widget.setDragEnabled(True)
        hbox.addWidget(list_widget)

        list_widget_icon_mode = QListWidget()
        list_widget_icon_mode.setViewMode(QListWidget.IconMode)
        list_widget_icon_mode.setAcceptDrops(True)
        list_widget_icon_mode.setDragEnabled(True)
        hbox.addWidget(list_widget_icon_mode)

        for index, icon in enumerate(self.icons):
            widget_item = QListWidgetItem(
                QIcon.fromTheme(icon),
                f'Ícone {index}',
            )
            list_widget.insertItem(index, widget_item)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())
