#!/usr/bin/env bash
pyinstaller --noconfirm --log-level=WARN \
--windowed \
--name="Exemplo" \
--add-data="icons/:icons" \
--add-data="MainWindow.qml/:." \
--hidden-import PySide2.QtXml \
--upx-dir=/usr/local/share/ \
MainWindow.py
