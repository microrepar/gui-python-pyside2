#!/usr/bin/env bash
pyinstaller --noconfirm --log-level=WARN \
--windowed \
--name="Exemplo" \
--add-data="icons/:icons" \
--add-data="MainWidget.ui/:." \
--hidden-import PySide2.QtXml \
--upx-dir=/usr/local/share/ \
MainWidget.py
