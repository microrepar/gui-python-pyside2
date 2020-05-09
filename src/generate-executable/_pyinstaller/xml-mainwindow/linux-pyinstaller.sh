#!/usr/bin/env bash
pyinstaller --noconfirm --log-level=WARN \
--windowed \
--name="Exemplo" \
--add-data="./icons/:icons" \
--add-data="./MainWindow.ui/:." \
--hidden-import PySide2.QtXml \
--upx-dir=/usr/local/share/ \
mainwindow.py
